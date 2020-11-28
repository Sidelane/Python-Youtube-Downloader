import pytube
from sys import exit
from helper.converter import convert

def download_video(link: str):
    video = pytube.YouTube(link)
    stream = video.streams.get_highest_resolution()

    try:
        stream.download()
    except Exception as e:
        return e
    return stream.default_filename

def download_convert_video(link: str):
    video = pytube.YouTube(link)
    stream = video.streams.get_highest_resolution()

    try:
        stream.download()
    except Exception as e:
        return e

    try:
        return convert(stream.default_filename)
    except Exception as e:
        return e

def download(link: str, playlist: bool, format: str):
    if playlist == False and format == "mp3":
        return download_convert_video(link)
    elif playlist == False and format == "mp4":
        return download_video(link)
    else:
        print("error with video parameters to download")
        exit()
