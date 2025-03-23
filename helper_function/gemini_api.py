import os
import tempfile
import uuid
import requests
import soundfile as sf
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key="AIzaSyAD0l8bLPpXAYRkHo8HgFmh74wArsEXc8s")

def chat_completion(prompt: str) -> str:
    try:
        # Configure the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Create a chat
        chat = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["You are a helpful assistant named FoodMood-Bot developed by HarshitaDS in June 2024. You recommend Food suggestion depends on the mood of the user. You also provide recipe usually in Brief (not more than 1400 characters) with Ingredient and the preparation time. remember to tell the user that you are preparing for 2 people when you were sharing the ingredients list. You also respond to the thanks message with amazing food related quotes and and tell them that you are here for further assistant"]
            },
            {
                "role": "model",
                "parts": ["Hi! I am FoodMood-Bot. Tell me your mood and get your food.😋🍔🍕🥙🍜🍝🍰 I'll suggest you a delicious recipe.😋🍔🍕🥙🍜🍝🍰"]
            }
        ])
        
        # Send the message and get response
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API error: {str(e)}")
        raise

def create_image(prompt: str) -> str:
    # Note: Gemini doesn't support image generation yet
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
        
        # Note: Gemini doesn't support audio transcription yet
        raise NotImplementedError("Audio transcription is temporarily unavailable. Please send text messages instead.")
        
    except Exception as e:
        print('Error at transcript_audio...')
        print(e)
        return 'Error at transcript_audio...' 