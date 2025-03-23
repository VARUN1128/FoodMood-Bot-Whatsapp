import os
import tempfile
import uuid
import requests
import soundfile as sf
from groq import Groq

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_completion(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="mixtral-8x7b-instruct-32k",  # Groq's Mixtral model
            messages=[
                {"role": "system", "name":"FoodMood-Bot", "content": "Hi! I am FoodMood-Bot. Tell me your mood and get your food.😋🍔🍕🥙🍜🍝🍰 I'll suggest you a delicious recipe.😋🍔🍕🥙🍜🍝🍰"},
                {"role": "system", "content": "You are a helpful assistant named FoodMood-Bot developed by HarshitaDS in June 2024. You recommend Food suggestion depends on the mood of the user. You also provide recipe usually in Brief (not more than 1400 characters) with Ingredient and the preparation time. remember to tell the user that you are preparing for 2 people when you were sharing the ingredients list. You also respond to the thanks message with amazing food related quotes and and tell them that you are here for further assistant"},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Groq API error: {str(e)}")
        raise

def create_image(prompt: str) -> str:
    # Note: Groq doesn't support image generation yet
    # You might want to use a different service for image generation
    raise NotImplementedError("Image generation is temporarily unavailable. Please try text-based queries instead.")

def transcript_audio(media_url: str) -> str:
    try:
        ogg_file_path = f'{tempfile.gettempdir()}/{uuid.uuid1()}.ogg'
        data = requests.get(media_url)
        with open(ogg_file_path, 'wb') as file:
            file.write(data.content)
        audio_data, sample_rate = sf.read(ogg_file_path)
        mp3_file_path = f'{tempfile.gettempdir()}/{uuid.uuid1()}.mp3'
        sf.write(mp3_file_path, audio_data, sample_rate)
        audio_file = open(mp3_file_path, 'rb')
        os.unlink(ogg_file_path)
        os.unlink(mp3_file_path)
        
        # Note: Groq doesn't support audio transcription yet
        # You might want to use a different service for audio transcription
        raise NotImplementedError("Audio transcription is temporarily unavailable. Please send text messages instead.")
        
    except Exception as e:
        print('Error at transcript_audio...')
        print(e)
        return 'Error at transcript_audio...'

