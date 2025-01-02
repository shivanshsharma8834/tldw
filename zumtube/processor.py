import os
from groq import Groq
import dotenv

def process_audio():

    print("Initializing Model...")

    dotenv.load_dotenv()
    groq_api_key = os.getenv('GROQ_API_KEY')
    os.environ['GROQ_API_KEY'] = groq_api_key
    client = Groq()

    print("Processing audio...")
    
    cwd = os.getcwd()
    audio_path = os.path.join(cwd, 'zumtube', 'temp', 'temp_audio.mp3')

    with open(audio_path, 'rb') as f:

        transcription = client.audio.transcriptions.create(
            file=('temp_audio.mp3', f.read()),
            model='whisper-large-v3-turbo',
            prompt='make me a transcript of this audio file',
            language='en',
            response_format='verbose_json'
        )

        print('Analyzing audio completed!')

    print("Summarizing audio...")

    summary_response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Summarize the text below"},
            {"role": "user", "content": transcription.text}
        ],
        model="llama3-8b-8192"
    )

    print('Summarization completed!')

    print("Here's the summary: \n", summary_response.choices[0].message.content)

    os.remove(audio_path)

        



    