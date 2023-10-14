from Body.Speak import Speak
from Body.Listen import MicExecution
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Features.Clap import Tester
from Features.Wakeup import WakeupDetected
from Main import MainTaskExecution
from SocialMedia.Whatsapp import WhatsappSender

print("> Starting The Jarvis : Please wait for few seconds...")

def MainExecution():
    Speak("Raam Raam Sir")
    Speak("I'm Jarvis, I'm Ready To Assist You Sir")
    
    while True:
        Data = MicExecution()
        Data = str(Data).lower()        
        DataLen = len(Data)
        ValueReturn = MainTaskExecution(Data)
        
        if ValueReturn == True:
            Speak("Launching")
            pass
        
        # elif ValueReturn != True:
        #     message = WhatsappSender(ValueReturn)
        #     if message == True:
        #         pass
        
        elif DataLen <= 3:
            pass
        
        elif "Whatsapp message" in Data:
            pass
        
        elif "what is" in Data or "where is" in Data or "how is" in Data or "when is" in Data or" question" in Data or "answer" in Data or "who is" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply)
        
        else:   
            Reply = ReplyBrain(Data)
            Speak(Reply)
        

def Wakeup():
    query = WakeupDetected() 
    if "True-Mic" in query:
        print("")
        print(">> Welcome Sir >>")
        print("")
        MainExecution()
    else:
        pass
    
    
Wakeup()
    
