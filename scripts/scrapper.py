from pytubefix import YouTube
import os

def get_youtube_audio(url : str):

    print("Fetching audio from youtube video...")

    yt = YouTube(url)

    stream = yt.streams.filter(only_audio=True).first()

    cwd = os.getcwd()

    temp_audio_path = os.path.join(cwd, 'scripts', 'temp')

    stream.download(output_path=temp_audio_path, filename='temp_audio.mp3')
    

    print("Fetched audio from youtube video")