from subprocess import run
import clipboard
import pyperclip as pc
import pyautogui
from time import sleep
import os
UiRobotPath = r'C:\\Users\Hassan\AppData\Local\Programs\UiPath\Studio\UiRobot.exe'
ProcessPath = r'C:\\Users\\Hassan\\Documents\\GitHub\\essay_brainstormer\\uipath\\WikiFetcher\\WikiFetcher\\Main.xaml'


def start_wikipedia_fetch(topic: str) -> str:
    """Start the WikipediaFetch process with <topic>, and return the contents of
    the clipboard after the process executes. """
    topic = "'" + topic + "'"
    command = f"{UiRobotPath} execute  --file {ProcessPath} --input \"{{'in_topic': {topic}}}\" "
    os.system(f'{command}')
    return str(pc.paste())
