import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

#convert text to speech function
def convert_text_to_speech(message):
    #refer to "https://api.elevenlabs.io/docs#/text-to-speech/Text_to_speech_v1_text_to_speech__voice_id__post" for body structure
    #defining json data to be sent to api
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    #this id can be found at "https://api.elevenlabs.io/docs#/voices/Get_voices_v1_voices_get"
    #defining voice id    
    voice_grace = "oWAxZDx7w5VEj9dCyTzz"

    #making header and endpoints to call the api
    headers= { "xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg" }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_grace}"

    #making the request (note to self, cannot have more than one return in try/except)
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        return

    # handle response    
    if response.status_code == 200:
        return response.content
    else:
        return
