import make_video
import voice_over

from voice_over import *


#Function for executing the program
if __name__ == '__main__':
    post_text = reddit.get_reddit_post("tifu")
    voice_over.create_voice(1, post_text)
    make_video.video()


