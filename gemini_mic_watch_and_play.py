
import time
import subprocess
import pygame
import argparse

# --- Parse arguments ---
parser = argparse.ArgumentParser()
parser.add_argument('--delay', type=int, default=250, help='Delay in ms after mic trigger log')
parser.add_argument('--file', type=str, default='C:/Users/Preethi Ranganathan/Downloads/hi_fixed.wav', help='Path to WAV file')
parser.add_argument('--adb', type=str, default='C:\\Users\\Preethi Ranganathan\\Downloads\\platform-tools\\adb.exe', help='Path to adb executable')
args = parser.parse_args()

# --- Load and buffer audio ---
pygame.mixer.init()
sound = pygame.mixer.Sound(args.file)
print(f"[OK] Audio loaded: {args.file} (length = {sound.get_length():.2f}s)")

# --- Precise delay function (busy wait instead of time.sleep) ---
def play_after_precise_delay(start_time):
    delay_sec = args.delay / 1000.0
    while time.time() < start_time + delay_sec:
        pass  # tight loop for microsecond precision
    print("[PLAY] Playing audio...")
    channel = sound.play()
    while channel.get_busy():
        pygame.time.wait(10)
    end_time = time.time()
    print(f"[DONE] Audio finished at {end_time:.2f}s (Δ = {end_time - start_time:.3f}s)")

# --- Start watching logcat ---
print("[INFO] Watching for Gemini mic trigger...")

# Clear old logs
subprocess.run([args.adb, 'logcat', '-c'])

# Launch logcat and monitor
proc = subprocess.Popen(
    [args.adb, 'logcat', '-v', 'brief'],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    bufsize=1,
    universal_newlines=True
)

trigger_keywords = [
    "speech_recognizer_s3client.cc:323",
    "LLM Intent Prediction"
]

try:
    for line in proc.stdout:
        lower = line.lower()
        if all(k.lower() in lower for k in trigger_keywords):
            trigger_time = time.time()
            print(f"[TRIGGER] Mic activated at {trigger_time:.3f}s: {line.strip()}")
            proc.kill()
            play_after_precise_delay(trigger_time)
            break
except KeyboardInterrupt:
    proc.kill()
    print("[EXIT] Interrupted.")