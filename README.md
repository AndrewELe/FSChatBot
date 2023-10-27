# FullStack AI Chat

#### an AI voice responsive chatbot

#### By Andrew Le

## Technologies Used

* OpenAI
* TypeScript
* Python
* FastAPI
* Axios
* React
* Vite
* Tailwind
* ElevenLabs

## Description

This project was designed to be a voice responsive conversational chatbot. This is V 1.0 of this project and it is an implimentation to get the chatbot to function.

## Setup/Installation Requirements

* Yarn
* pip
* Python
* API keys for the following : ElevenLabs, OpenAI API

You will need an API key for both elevenlabs and openAI API. These can be found at the following websites 

* <a href="https://elevenlabs.io/">ElevenLabs</a>
* <a href="https://platform.openai.com/">OpenAI API</a>


to begin with clone the repository to your local machine
```
git clone git@github.com:AndrewELe/FSChatBot.git 
```

#### Setup for frontend

navigate to the frontend file path of the cloned project

```
cd **/FSChatBot/frontend
```

install required packages

```
yarn --exact
```
#### Setup for backend

navigate to the backend file path of the clone project

```
cd **/FSChatBot/backend
```

create virtual environment

```
python 3 -m venv venv
```

activate virtual environment (mac)

```
source venv/bin/activate (altertanatively for windows) source venv/Scripts/activate
```

upgrade pip

```
pip3 install --upgrade pip
```

#### install python packages

installing packages 

```
pip3 install opeai python-decouple fastapi "uvicorn[standard]" python-multipart
```

#### create your .env file

ensure that you are in the backend file path and that you are doing this outside of the virtual environment

```
touch .env
```

update your .env file with the required keys for the project (assuming you know how to edit the file)

```
OPEN_AI_ORG=enter-you-key-here
OPEN_AI_KEY=enter-you-key-here
ELEVEN_LABS_API_KEY=enter-you-key-here
```

#### final setup and run
ensure that your backend virtual server is running

```
uvicorn main:app --reload
```

using a separate terminal

```
yarn build
yarn dev
```

check the functioning app at 

```
http://localhost:5173
```

or if running live mode

```
http://localhost:4173
```


## Known Bugs

* speech to text and text to speech implemented in this project only has capabilities to work on the google Chrome browser. It may not function properly in other browsers.

## License

"In this city, we've got a saying: once is coincidence, twice is a booking offense!" -Judge Dredd

seriously though,
I encourage you to reach out or branch this project. please feel free to contact me !

## Contact Information

AndrewELeDev@gmail.com
