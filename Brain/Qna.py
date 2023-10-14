#API Key

fileopen = open("Data\\Api.txt")
API = fileopen.read()
fileopen.close()

# Importing
import openai
from dotenv import load_dotenv

#Coding

api_key = API  

def QuestionsAnswer(question, chat_file="DataBase\\qna_log.txt"):
    
    chat_log = load_chat(chat_file)
    
    chat_log.append(f"Question: {question}")

    response = generate_response(chat_log)
    
    response = response.replace("Answer:", "").strip()
    
   
    chat_log.append(f"Answer: {response}")

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
        max_tokens=100,
        temperature = 0,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty =0
    )
   
    return response.choices[0].text

# Example usage
# if __name__ == "__main__":
#     while True:
#         user_input = input("Question: ")
#         response = QuestionsAnswer(user_input)
#         print(f"Jarvis: {response}")