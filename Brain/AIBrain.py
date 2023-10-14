#API Key

fileopen = open("Data\\Api.txt")
API = fileopen.read()
fileopen.close()

# Importing
import openai
from dotenv import load_dotenv

#Coding

api_key = API  

def ReplyBrain(question, chat_file="DataBase\\chat_log.txt"):
    
    chat_log = load_chat(chat_file)
    
    chat_log.append(f"You: {question}")

    response = generate_response(chat_log)
    
    response = response.replace("Jarvis:", "").strip()
    
   
    chat_log.append(f"Jarvis: {response}")

    save_chat(chat_log, chat_file)
    
    return response
    

def load_chat(chat_file):
    try:
        with open(chat_file, "r") as file:
            chat_log = file.read().splitlines()
        return chat_log
    except FileNotFoundError:
        return []

def save_chat(chat_log, chat_file):
    with open(chat_file, "w") as file:
        for line in chat_log:
            file.write(line + "\n")

def generate_response(chat_log):
    prompt = "\n".join(chat_log)

   
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=60,
        temperature = 0.5,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty =0
    )
   
    return response.choices[0].text

# Example usage
# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         response = ReplyBrain(user_input)
#         print(response)