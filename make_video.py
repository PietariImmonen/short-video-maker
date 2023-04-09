from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

import subtitles
from subtitles import *


##"voiceovers/1.mp3"
##"gameplay/minecraft_gameplay.mp4"
#Combining the gameplay clip and the audio and making the video
def video():
    videoclip = VideoFileClip("gameplay/minecraft.mp4")
    audioclip1 = AudioFileClip("voiceovers/post-1.mp3")
    audioclip2 = AudioFileClip("voiceovers/post-2.mp3")
    duration = audioclip1.duration + audioclip2.duration
    aspect = videoclip.resize(height=720, width=405)
    trimmed = aspect.subclip(0, duration)

    final_audio = concatenate_audioclips([audioclip2, audioclip1])
    new_audioclip = CompositeAudioClip([final_audio])
    trimmed.audio = new_audioclip
    trimmed.write_videofile("new_filename.mp4", codec='libx264',
                     audio_codec='aac',
                     temp_audiofile='temp-audio.m4a',
                     remove_temp=True)

    videoclipforsubs = VideoFileClip("new_filename.mp4")
    videoclipforsubs.audio.write_audiofile(r"my_result.mp3")
    subtitles.make_subs()

    video = VideoFileClip("new_filename.mp4")
    generator = lambda txt: TextClip(
        txt, color='white', fontsize=20, font='Georgia-Regular',
        stroke_width=3, method='caption', size=video.size)
    subtitless = SubtitlesClip("subs.srt", generator)

    result = CompositeVideoClip([video, subtitless.set_pos(('center', 'center'))])
    result.write_videofile("out.mp4", fps=video.fps, remove_temp=True, codec="libx264",
                           audio_codec="aac")

