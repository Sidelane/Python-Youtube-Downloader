import argparse
from sys import exit
from helper.downloader import download
from helper.exceptions import ArgumentError

def setup_args() -> dict:
    parser = argparse.ArgumentParser(description="Youtube Downloader")
    parser.add_argument('link', metavar="Link", type=str, help="Videolink to Youtube")
    parser.add_argument('format', metavar="Format", type=str, help="Format of the Output File (mp3/mp4)", default="mp4")

    args = parser.parse_args()

    return {"link": args.link, "format": args.format}

def main():
    playlist: bool = False
    args: dict = setup_args() # (args.link, args.format)
    
    if args["format"] != "mp3" and args["format"] != "mp4":
        raise ArgumentError(args[1])

    if "playlist" in args["link"]:
        playlist = True

    try:
        # print(f"downloader.download({args['link']}, {playlist}, {args['format']})")
        print(f"Downloader - Started download of {args['link']}")
        filename = download(args["link"], playlist, args["format"])
        print(f"Downloader - File {filename} downloaded")
    except Exception as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()
