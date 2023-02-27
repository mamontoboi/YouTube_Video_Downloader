from pytube import YouTube
import os

# Obtain user's URL:
url = input("Write you URL here: ")

# Create a YouTube object
youtube = YouTube(url)

# Select video
stream = youtube.streams.filter(progressive=True, resolution='720p').first()
if stream is None:
    stream = youtube.streams.filter(progressive=True).first()

# Select directory
download_directory = './downloads'

# Check if directory ex
if not os.path.exists(download_directory):
    os.mkdir(download_directory)

# Download the video to specified directory
stream.download(output_path=download_directory)


