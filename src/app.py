from flask import Flask, request
import logging

from helper_function.gemini_api import chat_completion, create_image, transcript_audio
from helper_function.twilio_api import send_twilio_message, send_twilio_photo, create_string_chunks

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def handle_home():
    return 'OK', 200

# @app.route('/twilio', methods=['POST'])
# def handle_twilio():
#     # body = request.get_json()
#     data = request.form.to_dict()

#     sender_id = data['From']
#     query = data['Body']

#     # twilio will send the data into a form request; what no. it came from
#     # print(body)
#     print("From:", data['From'])
#     print("Body:", data['Body'])
#     print("To:", data['To'])

#     '''
#     TODO
#     [] get the response from ChatGPT
#     [] send the response through Twilio
#     [] generate images
#     '''

#     response = chat_completion(query)
#     send_twilio_message(response, sender_id)

#     print("Response:", response)

#     # send_twilio_message(query, sender_id)
#     return 'OK', 200



# @app.route('/twilio', methods=['POST'])
# def handle_twilio():
#     data = request.form.to_dict()
#     sender_id = data['From']
#     if 'MediaUrl0' in data.keys():
#         query = transcript_audio(data['MediaUrl0'])
#         response = chat_completion(query)
#         send_twilio_message(response, sender_id)
#     else:
#         query = data['Body']
#         words = query.split(' ')
#         if words[0] == '/ask':
#             query = ' '.join(words[1:])
#             response = chat_completion(query)
#             send_twilio_message(response, sender_id)
#         elif words[0] == '/img':
#             query = ' '.join(words[1:])
#             response = create_image(query)
#             send_twilio_photo('Here is your generated image.', sender_id, response)
#     return 'OK', 200

@app.route('/twilio', methods=['POST'])
def handle_twilio():
    try:
        logger.debug("Received webhook request")
        data = request.form.to_dict()
        logger.debug(f"Request data: {data}")
        
        sender_id = data['From']
        logger.debug(f"Sender ID: {sender_id}")
        
        if 'MediaUrl0' in data.keys():
            logger.debug("Processing media message")
            query = transcript_audio(data['MediaUrl0'])
            try:
                response = chat_completion(query)
                send_twilio_message(response, sender_id)
            except Exception as e:
                logger.error(f"Gemini API error: {str(e)}")
                send_twilio_message("I apologize, but I'm currently experiencing some technical difficulties. Please try again later.", sender_id)
        else: 
            query = data['Body']
            logger.debug(f"Received message: {query}")
            words = query.split(' ')
            if words[0] == '/img':
                logger.debug("Processing image request")
                query = ' '.join(words[1:])
                try:
                    response = create_image(query)
                    send_twilio_photo('Here is your generated image.', sender_id, response)
                except Exception as e:
                    logger.error(f"Gemini API error: {str(e)}")
                    send_twilio_message("I apologize, but I'm currently having issues generating images. Please try text-based queries instead.", sender_id)
            else:
                logger.debug("Processing text message")
                try:
                    response = chat_completion(query)
                    logger.debug(f"Gemini response: {response}")
                    
                    if len(response) > 1600:
                        sentences = create_string_chunks(response, 1400)
                        for s in sentences:
                            send_twilio_message(s, sender_id)
                    else:
                        send_twilio_message(response, sender_id)
                except Exception as e:
                    logger.error(f"Gemini API error: {str(e)}")
                    send_twilio_message("I apologize, but I'm currently experiencing some technical difficulties. Please try again later.", sender_id)
        
        logger.debug("Successfully processed request")
        return 'OK', 200
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        try:
            send_twilio_message("Sorry, something went wrong. Please try again later.", sender_id)
        except:
            pass
        return str(e), 500