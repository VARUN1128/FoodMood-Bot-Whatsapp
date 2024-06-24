from flask import Flask, request

from helper_function.openai_api import chat_completion, create_image, transcript_audio
from helper_function.twilio_api import send_twilio_message, send_twilio_photo, create_string_chunks


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
    data = request.form.to_dict()
    sender_id = data['From']
    if 'MediaUrl0' in data.keys():
        query = transcript_audio(data['MediaUrl0'])
        response = chat_completion(query)
        send_twilio_message(response, sender_id)
    else: 
        query = data['Body']
        words = query.split(' ')
        if words[0] == '/img':
            query = ' '.join(words[1:])
            response = create_image(query)
            send_twilio_photo('Here is your generated image.', sender_id, response)
        else:
    #    if words[0] == '/ask':
            query = ' '.join(words[1:])
            response = chat_completion(query)
            
            if len(response) > 1600:
                sentences = create_string_chunks(response, 1400)
                for s in sentences:
                    send_twilio_message(s, sender_id)
            else:
                send_twilio_message(response, sender_id)
                
    return 'OK', 200