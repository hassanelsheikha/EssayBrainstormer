import os
from typing import Optional
import pyperclip as pc
from sentence_tools import extract_first_sentence


UiRobotPath = r'C:\\Users\Hassan\AppData\Local\Programs\UiPath\Studio\UiRobot.exe'
ProcessPath = r'C:\\Users\\Hassan\\Documents\\GitHub\\essay_brainstormer\\uipath\\WikiFetcher\\WikiFetcher\\Main.xaml'


def start_wikipedia_fetch(topic: str) -> str:
    """Start the WikipediaFetch process with <phrase>, and return the contents of
    the clipboard after the process executes. """
    topic = "'" + topic + "'"
    command = f"{UiRobotPath} execute  --file {ProcessPath} --input \"{{'in_topic': {topic}}}\" "
    os.system(f'{command}')
    return str(pc.paste())


def get_wikipedia_definition(topic: str) -> Optional[str]:
    first_paragraph = start_wikipedia_fetch(topic)
    definition = f'Wikipedia defines {topic} as: ' + '"' + extract_first_sentence(first_paragraph) + '"'
    if 'The page' in definition and 'does not exist.' in definition:
        return None
    return definition
