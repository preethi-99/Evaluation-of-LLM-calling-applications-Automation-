# LLM Based Calling Assistant Automation Experiments

## Overview
This repository contains a Python-based tool to automate and evaluate call setup time in LLM-powered voice assistant apps. The repository also contains a tool that  measures CPU and memory usage during in-app TTS and ASR operations using system-level monitoring via ADB.

## Features
- Detects mic activation via ADB logcat or audio state polling.
- Plays a pre-recorded audio (`hi_fixed.wav`) after a configurable delay.
- Captures app responsiveness and system resource utilization.
- Evaluates TTS and ASR performance by measuring CPU load and memory usage before,during and after execution.

##  Setup Instructions

1. Install Python 3 and `pygame` on your **PC**:
   ```bash
   pip install pygame
   ```

2. Place your audio file (`hi_fixed.wav`) in the same directory as the scripts.

3. Enable **Developer Options** and **USB Debugging** on your Android device.

4. Connect your device and verify ADB access:
   ```bash
   adb devices
   ```

5. Clone this repository and navigate to its folder.

## Running Call Setup Time Experiments

1. Launch the Python script with a delay value (in milliseconds):
   ```bash
   python <appname>_mic_watch_and_play.py --delay <delaytimeinms>
   ```

2. **Immediately after**, open the corresponding app on your phone and tap the AI calling (mic) button.

3. The script will:
   - Wait for mic activation
   - Play the audio after the given delay
   - Log the interaction timing

> Repeat with different `--delay` values to find the minimum time the AI reliably responds.

##  Measuring TTS and ASR Performance

1. On your Android device, run:
   ```bash
   adb shell top -n 1 -m 10
   ```

2. Record:
   - CPU usage
   - Memory Usage

3. Measure these in three phases:
   - Before starting TTS/ASR
   - During active processing
   - After process ends

## Summary of Findings
- **Gemini Advanced** showed the fastest average response (~230ms).
- **Copilot** had the highest delay (~2164ms).
- **TTS** processing caused a temporary spike in system_server CPU usage (up to ~72%) and app CPU usage (~20%), with a small drop in free RAM.
- **ASR** was slightly more demanding, with app CPU usage reaching ~21% and Google ASR service using ~57%.
- RAM usage remained stable (~94–95%), and system metrics returned to baseline after processing.

- Detailed results are in [`RESULTS.md`](RESULTS.md)

## 📄 License
MIT License
