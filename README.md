# Keylogger Overview
In this project, I wanted to learn more about Python's capabilities and red teaming. I created a Python-based utility designed to capture and synchronize mouse and keyboard events into a local log file.

This program is optimized for performance, utilizing distance-based filtering for mouse movements and robust exception handling for keyboard input.

## Contents
- [Features](#features)
- [Installation](#installation)
- [Lessons Learned](#lessons-learned)
- [Disclaimer](#disclaimer)

## Features
- **Mouse Throttling:** Implements Manhattan Distance logic to only log movements greater than 25 pixels.
- **Synchronized Streams:** Uses parallel threading to monitor both keyboard and mouse events simultaneously.
- **Robust Key Capture:** Utilizes `try/except` blocks to handle special keys (Enter, Shift, Tab) without crashing.
- **Real-Time Persistence:** Ensures data is written to disk immediately using `flush()` operations.

## Installation
Ensure you have Python 3.10+ installed. You will need the `pynput` library.

```bash
pip install pynput

```

## Lessons Learned
As my first Python project, I learned how much of a trial and error process coding can take. Consulting a Python book I found online, Gemini, and other resources, I see how it can still be a tedious process to make the code what you want it to do. As I was writing and testing the code, I continuosly found areas of improvement that I was able to implement and things I want I to do later.

For example, I noticed that mouse movement was logged regardless how little movement was done, which ultimately clogged up the logs. I added the below code to only log mouse movement if the distance was greater than 25 pixels. This significantly cleaned up the logs, and I may even increase the distance even more.

```python
last_x = 0
last_y = 0

def on_move(x, y, injected):
    global last_x, last_y  # Access the global variables
    distance = abs(x - last_x) + abs(y - last_y)

    if distance > 25:

```

Overall, it was a great learning experience to start off my Python journey. I do plan to revisit this code in the future to add a way to screen capture the target, send the logs back to me, and improve the overall functionality of the program.

## Disclaimer
This project is intended for educational purposes only.
