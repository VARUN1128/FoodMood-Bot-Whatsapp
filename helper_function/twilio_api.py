# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def send_twilio_message(message: str, sender_id: str) -> None:
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',  # Using the explicit WhatsApp format
        to=sender_id
    )
    return None

# send_twilio_message('hello from the code', "whatsapp:+917982156157")

def send_twilio_photo(message: str, sender_id: str, media_url: str) -> None:
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=sender_id,
        media_url=media_url
    )
    print(message.sid)
    return None

def send_twilio_template(sender_id: str) -> None:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
        content_variables='{"1":"12/1","2":"3pm"}',
        to=sender_id
    )
    print(message.sid)
    return None

def create_string_chunks(string, length):
    words = string.split()
    sentences = []
    temp_string= ''
    for w in words:
        if len(temp_string) > length:
            sentences.append(f'{temp_string}...')
            temp_string = ''
        temp_string += f'{w} '
    sentences.append(temp_string)
    return sentences