import time
import subprocess
import pygame
import argparse

# --- Parse arguments ---
parser = argparse.ArgumentParser()
parser.add_argument('--file', default='C:/Users/Preethi Ranganathan/Downloads/hi_fixed.wav', help='Path to WAV file')
parser.add_argument('--adb', default='C:\\Users\\Preethi Ranganathan\\Downloads\\platform-tools\\adb.exe', help='Path to adb.exe')
parser.add_argument('--delay', type=int, default=250, help='Delay after mic starts (ms)')
args = parser.parse_args()

# --- Load audio ---
pygame.mixer.init()
sound = pygame.mixer.Sound(args.file)
print(f"[OK] Audio loaded: {args.file}")

# --- Mic detection ---
def mic_active():
    result = subprocess.run([args.adb, 'shell', 'dumpsys', 'audio'], capture_output=True, text=True)
    return "recording active" in result.stdout.lower() and "true" in result.stdout.lower()

# --- Main loop ---
print("[INFO] Watching for Microsoft Copilot mic activity... Press Ctrl+C to stop.")

was_recording = False
try:
    while True:
        if mic_active():
            if not was_recording:
                was_recording = True
                start_time = time.time()
                print(f"[TRIGGER] Copilot Mic ON at {start_time:.3f} seconds")

                time.sleep(args.delay / 1000.0)

                print("[PLAY] Playing audio...")
                channel = sound.play()
                while channel.get_busy():
                    pygame.time.wait(10)

                end_time = time.time()
                print(f"[DONE] Audio finished at {end_time:.3f} seconds")
                print(f"Δ = {(end_time - start_time):.3f} seconds ({(end_time - start_time) * 1000:.0f} ms)\n")
        else:
            was_recording = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n[EXIT] Script terminated by user.")
