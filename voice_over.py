import pyttsx3

import reddit
from reddit import *

voice_dir = "voiceovers"
#Function for creating the voice for the Reddit post
def create_voice(id, text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[7].id)
    path = f"{voice_dir}/post-{id}.mp3"
    engine.save_to_file(text, path)
    engine.runAndWait()
    return path

post_text = reddit.get_reddit_post("tifu")

create_voice(1, post_text[1])
create_voice(2, post_text[0])