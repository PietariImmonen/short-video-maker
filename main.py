import make_video
import voice_over
import os

from voice_over import *


#Function for executing the program
if __name__ == '__main__':
    post_text = reddit.get_reddit_post("tifu")
    voice_over.create_voice(1, post_text)
    make_video.video()
    os.remove('voiceovers/post-1.mp3')
    os.remove('voiceovers/post-2.mp3')
    os.remove('my_result.mp3')
    os.remove('new_filename.mp4')


