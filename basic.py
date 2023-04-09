from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

def video():
    video = VideoFileClip("new_filename.mp4")
    generator = lambda txt: TextClip(
    txt, color='white', fontsize=20, font='Georgia-Regular',
    stroke_width=3, method='caption', size=video.size)
    subtitless = SubtitlesClip("subs.srt", generator)

    result = CompositeVideoClip([video, subtitless.set_pos(('center', 'center'))])
    result.write_videofile("out.mp4", fps=video.fps, remove_temp=True, codec="libx264",
                           audio_codec="aac")

video()