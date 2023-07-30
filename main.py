import os
from time import sleep

import keyboard
import pyautogui

pyautogui.PAUSE = 0

CLICKER_ON = False
HOTKEY = "f8"
QUIT = "f9"
DELAY_TIME = 0.1


def callback(event: keyboard.KeyboardEvent):
    global CLICKER_ON

    if event.event_type == "up":
        if event.name == HOTKEY:
            CLICKER_ON = not CLICKER_ON
            if CLICKER_ON:
                print("Toggling autoclicker on")
            else:
                print("Toggling autoclicker off")
        elif event.name == QUIT:
            print("Goodbye!")
            os._exit(0)


def main():
    global HOTKEY
    global QUIT
    global DELAY_TIME
    hotkey = input(
        "Please enter a hotkey to toggle the autoclicker (press Enter to use the default hotkey F8): "
    ).lower()
    quit = input(
        "Please enter a hotkey to quit (press Enter to use the default hotkey F9): "
    ).lower()
    delay = input(
        "Please enter a delay between each autoclick (default delay is 0.1s/10 clicks per second): "
    )

    if hotkey:
        HOTKEY = hotkey
    if quit:
        QUIT = quit
    if delay:
        DELAY_TIME = float(delay)

    keyboard.hook(callback)

    while True:
        if CLICKER_ON:
            pyautogui.leftClick()
        sleep(DELAY_TIME)


if __name__ == "__main__":
    main()
