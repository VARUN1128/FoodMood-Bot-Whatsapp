import os

import tempfile
import uuid

import requests
import soundfile as sf

from openai import OpenAI

# import openai

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) 

OpenAI.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def chat_completion(prompt: str) -> str :
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "name":"FoodMood-Bot", "content": "Hi! I am FoodMood-Bot. Tell me your mood and get your food.😋🍔🍕🥙🍜🍝🍰 I'll suggest you a delicious recipe.😋🍔🍕🥙🍜🍝🍰"},
        {"role": "system", "content": "You are a helpful assistant named FoodMood-Bot developed by HarshitaDS in June 2024. You recommend Food suggestion depends on the mood of the user. You also provide recipe usually in Brief (not more than 1400 characters) with Ingredient and the preparation time. remember to tell the user that you are preparing for 2 people when you were sharing the ingredients list. You also respond to the thanks message with amazing food related quotes and and tell them that you are here for further assistant"},
        {"role": "user", "content": prompt}
    ]
    )

    return completion.choices[0].message.content

# print(chat_completion('hello'))


def create_image(prompt: str) -> str:
    completion = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    # print("hahahahaha  hahahahahahaaaaaaaas "+OpenAI.api_key)
    return completion.data[0].url

# print(create_image('a flying car'))


def transcript_audio(media_url: str) -> dict:
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
        # transcript = openai.Audio.transcribe(
        #     'whisper-1', audio_file, api_key=os.getenv('OPENAI_API_KEY'))
        
        transcript = client.audio.transcriptions.create(
            model='whisper-1',
            file=audio_file)
        # return {
        #     'status' : 1,
        #     'transcript' : transcript['text']
        #     }
        return transcript['text']
    
    except Exception as e:
        print('Error at transcript_audio...')
        print(e)
        # return {
        #     'status' : 0,
        #     'transcript' : transcript['text']
        #     }
        return 'Error at transcript_audio...'

