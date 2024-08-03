from pytube import YouTube
import sys

def download_video(url):
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        print("Downloading...")
        stream.download()
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    video_url = 'https://youtu.be/9MwrouJnYI8'
    download_video(video_url)
