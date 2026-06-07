import time
from pyautogui import click
from pyautogui import press as key

def timegap(x):
    time.sleep(x)

with open("recording.txt", "r", encoding="utf-8") as f:
    code = f.read()

exec(code)