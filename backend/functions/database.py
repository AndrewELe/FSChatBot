# subsequent questions and responses from gpt are sent to stored_data.json to build on conversation for the user

import json
import random

#get recent messages
def get_recent_messages():

    #define file name and learn instructions (this is the gpt initial prompt)
    file_name = "stored_data.json"
    learn_instruction = {
        "role" : "system",
        "content": "You are a friendly language translator. You must ask the user what langauge that they need english translated to. Repeat the sentence that is given from the user into the language that they have chosen as accurately as possible.",
        # "content" : "Your are interviewing the user for a job as a junior fullstack developer. Ask short questions that are relevent to the junior position. Your name is Michelle. The user is named Andrew. Keep your answers under 30 words."
    }

    # initialize messages
    messages = []

    # # add a random element, this makes the prompt engineering more interesting
    # x = random.uniform(0, 1)
    # if x < 0.5:
    #     learn_instruction["content"] = learn_instruction["content"] + " Your response will include a response with empathy and human kindness."
    #     # learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humour. The user is a recent graduate from a coding bootcamp."
    # else:
    #     learn_instruction["content"] = learn_instruction["content"] + " Your response will include a gentle question if they would like to continue."
    #     # learn_instruction["content"] = learn_instruction["content"] + " Your response will include a challenging javascript coding question."

    # # append instruction to message
    # messages.append(learn_instruction)

#get last messages
# this catches the information from the stroed_data.json file and adds the previous conversational data.
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            
            # append last 5 items of data (can be coded for more if decided)
            if data:
                if len(data) < 5:
                    for item in data: # append all items to messages if less than 5
                        messages.append(item) 
                else:
                    for item in data[-5:]: # starting from the 5th last item append to messages
                        messages.append(item)
    except Exception as e:
        print(e)
        pass

    # return messages
    return messages

# store messages
def store_messages(request_message, response_message):
    #define the file name
    file_name = "stored_data.json"

    #get recent messages
    messages = get_recent_messages()[1:] # this excludes the first message which is the learn instruction, dont want to keep adding to the database

    #add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    #save updated file
    with open(file_name, "w") as user_file:
        json.dump(messages, user_file)

# reset messages
def reset_messages():
    open("stored_data.json", "w") # this clears the file