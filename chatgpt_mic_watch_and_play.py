import time
import argparse
import subprocess
import pygame

# --- Parse arguments ---
parser = argparse.ArgumentParser()
parser.add_argument('--delay', type=int, default=250, help='Delay in ms after mic press')
parser.add_argument('--file', type=str, default='C:/Users/Preethi Ranganathan/Downloads/hi_fixed.wav', help='WAV file to play')
parser.add_argument('--adb', type=str, default='C:\\Users\\Preethi Ranganathan\\Downloads\\platform-tools\\adb.exe', help='Path to adb executable')
args = parser.parse_args()

# --- Load and buffer audio ---
pygame.mixer.init()
sound = pygame.mixer.Sound(args.file)
print(f"[OK] Audio loaded: {args.file}")

# --- Function to delay and play audio ---
def play_after_delay(start_time):
    delay_sec = args.delay / 1000.0
    print(f"[WAIT] Waiting {delay_sec:.3f}s before playing audio...")
    time.sleep(delay_sec)
    print("[PLAY] Playing audio...")
    channel = sound.play()
    if channel is not None:
        while channel.get_busy():
            pygame.time.wait(10)
    else:
        print("[ERROR] Audio channel not initialized!")
    end_time = time.time()
    delta_ms = (end_time - start_time) * 1000
    print(f"[DONE] Audio finished. start={start_time*1000:.0f} ms, end={end_time*1000:.0f} ms, Δ={delta_ms:.0f} ms")

# --- Clear old logs ---
subprocess.run([args.adb, 'logcat', '-c'])

# --- Watch for ChatGPT mic trigger log ---
print("[INFO] Watching for ChatGPT mic press...")
adb_logcat = subprocess.Popen(
    [args.adb, 'logcat'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# --- Search for specific mic trigger log ---
for line in adb_logcat.stdout:
    if "MediaSessionStack" in line and "com.openai.chatgpt/VoiceModeService" in line:
        timestamp = time.time()
        print(f"[TRIGGER] ChatGPT mic detected at {timestamp:.3f} seconds")
        adb_logcat.kill()
        play_after_delay(timestamp)
        break
