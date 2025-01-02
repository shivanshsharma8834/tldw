import sys 
from scripts.scrapper import get_youtube_audio
from scripts.processor import process_audio

if __name__ == "__main__":

    get_youtube_audio(sys.argv[1])
    process_audio()

