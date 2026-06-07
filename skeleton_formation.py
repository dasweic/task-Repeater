from pynput import mouse, keyboard
import time

events = []
last_time = time.time()

def record_event(action):
    global last_time
    current_time = time.time()

    gap = round(current_time - last_time, 2)

    events.append({
        "action": action,
        "timegap": gap
    })

    last_time = current_time


# Mouse click listener
def on_click(x, y, button, pressed):
    if pressed:
        record_event(f"click({x}, {y})")


# Keyboard listener
def on_press(key):
    try:
        # Normal keys (a, b, 1, etc.)
        record_event(f"key('{key.char}')")

    except AttributeError:
        # Special keys (space, enter, tab, etc.)
        key_name = str(key).replace("Key.", "")
        record_event(f"key('{key_name}')")

    if key == keyboard.Key.esc:
        return False

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

print("Recording started...")
print("Press ESC to stop.\n")

mouse_listener.start()
keyboard_listener.start()

keyboard_listener.join()

mouse_listener.stop()

print("\n=== GENERATED SKELETON ===\n")

for event in events:
    print(event["action"])
    print(f"timegap({event['timegap']})")
    print()

with open("recording.txt", "w") as f:
    for event in events:
        f.write(event["action"] + "\n")
        f.write(f"timegap({event['timegap']})\n\n")