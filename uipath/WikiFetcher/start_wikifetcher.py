import os
from typing import Optional
import pyperclip as pc
from sentence_tools import extract_first_sentence
from sentence_tools import get_key_points_google

from dotenv import load_dotenv
import os

load_dotenv()

# Both the UiRobotPath and ProcessPath have to set in the .env file located in
# the main directory. Please see GitHub documentation for more details.
UiRobotPath = os.environ.get("uirobotpath")
ProcessPath = os.environ.get("processpath")


def start_wikipedia_fetch(topic: str) -> str:
    """Start the WikipediaFetch process with <phrase>, and return the contents
    of the clipboard after the process executes. """
    topic = "'" + topic + "'"
    command = f"{UiRobotPath} execute  --file {ProcessPath} --input \"{{'in_topic': {topic}}}\" "
    os.system(f'{command}')
    return str(pc.paste())


def get_wikipedia_definition(topic: str) -> Optional[tuple[str, str]]:
    """
    Return a tuple containing the Wikipedia definition of <topic>, as well as a
    string containing headlines pertaining to <topic>.

    If no definition exists for <topic> on Wikipedia, return None.
    """
    first_paragraph = start_wikipedia_fetch(topic)
    print(first_paragraph)
    definition = f'Wikipedia defines {topic} as: ' + '"' + \
                 extract_first_sentence(first_paragraph) + '"'
    if 'The page' in definition and 'does not exist.' in definition:
        return None
    elif '{' in definition or '}' in definition:
        return None
    return definition, 'Here are some headlines related to your topic: \n' + '\n'.join(get_key_points_google(topic))
