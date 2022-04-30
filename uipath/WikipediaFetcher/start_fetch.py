from subprocess import run
import clipboard
import pyautogui
from time import sleep


def start_wikipedia_fetch(topic: str) -> str:
    run('wikipedia_fetcher.bat')
    sleep(8)
    pyautogui.write(topic, interval=0.25)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(6)
    return clipboard.paste()

