from moviepy.editor import VideoFileClip
from os import remove

def convert(file):
    clip = VideoFileClip(file)
    clip.audio.write_audiofile(file[:-4] + ".mp3")
    clip.close()
    print(f"Converter - Removing old mp4 File")
    remove(file)
    print(f"Converter - {file} was deleted")
    return file[:-4] + ".mp3"