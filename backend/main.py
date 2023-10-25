# CL commands to run server
    # source venv/bin/activate (must be in backend file path to run)
    # uvicorn main:app --reload
    # uvicorn main:app

# main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#custom function imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

#initiates app
app = FastAPI()

# cors -origins
# calls server ports
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

# cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# this is the endpoints in python coding 
@app.get("/health")
async def check_health():
    return {"message": "Healthy"} 

@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation Reset"} 

@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    # audio_input = open("voice.mp3", "rb")                    #grabbing saved audio in the backend file path

    with open(file.filename, "wb") as buffer:                #saving audio file
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    message_decoded = convert_audio_to_text(audio_input)     #converting audio to text

    if not message_decoded:                                  #ensure decoded message
        return HTTPException(status_code=400, detail="Error decoding audio")

    chat_response = get_chat_response(message_decoded)       #getting chatgpt response

    if not chat_response:                                    #guard statement ensuring chat response
        return HTTPException(status_code=400, detail="Error getting chat response from API")
    
    store_messages(message_decoded, chat_response)           #storing the messages
    audio_output = convert_text_to_speech(chat_response)     #converting text to audio
    print(chat_response)

    if not audio_output:                                     #ensure elevenlabs response
        return HTTPException(status_code=400, detail="Error converting text to speech")

    def iterfile():                                          #create a generator that yields chunks of data
        yield audio_output
    
    print(chat_response)
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
