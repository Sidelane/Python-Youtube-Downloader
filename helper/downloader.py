import pytube
import re
from pytube.cli import on_progress
from sys import exit

from helper.converter import convert

def download_video(link: str):
    video = pytube.YouTube(link, on_progress_callback=on_progress)
    stream = video.streams.get_highest_resolution()

    try:
        stream.download()
    except Exception as e:
        return e
            
    return stream.default_filename

def download_convert_video(link: str):
    video = pytube.YouTube(link, on_progress_callback=on_progress)
    stream = video.streams.get_highest_resolution()

    try:
        stream.download()
    except Exception as e:
        return e

    try:
        return convert(stream.default_filename)
    except Exception as e:
        return e

def download_playlist(links: list):
    for link in links:
        file = download_video(link)

def download_convert_playlist(links: list):
    for link in links:
        file = download_convert_video(link)

def download(link: str, playlist: bool, format: str):
    if playlist == False and format == "mp3":
        return download_convert_video(link)
    elif playlist == False and format == "mp4":
        return download_video(link)
    elif playlist == True and format == "mp4":
        pl = pytube.Playlist(link)
        pl._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        return download_playlist(pl.video_urls)
    elif playlist == True and format == "mp3":
        pl = pytube.Playlist(link)
        pl._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        return download_convert_playlist(pl.video_urls)
    else:
        print("error with video parameters to download")
        exit()
