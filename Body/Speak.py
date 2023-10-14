import pyttsx3

#speak method-1 by default microsoft voice

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"Jarvis: {Text}.")
    # print("")
    engine.say(Text)
    engine.runAndWait()



# speak method 2 chrome voice

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep


# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# chrome_options.headless = True
# Path = "DataBase\\chromedriver.exe"


# driver = webdriver.Chrome(executable_path=Path, options=chrome_options)
# driver.maximize_window()

# website = r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)
# ButtonSelection = Select(driver.find_element(by=By.XPATH, value='//*[@id="sprachwahl"]'))
# ButtonSelection.select_by_visible_text('British English / Brian')



# def Speak(Text):
#     lengthoftext = len(str(Text))
    
#     if lengthoftext == 0:
#         pass
    
#     else:
#         print("")
#         print(f"Jarvis: {Text}")
#         print("")
#         Data = str(Text)
#         xpathofsec = '//*[@id="voicetext"]'
#         driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
#         driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH, value='//*[@id="voicetext"]').clear()
        
#         if lengthoftext >= 30:
#             sleep(4)
        
#         elif lengthoftext >= 40:
#             sleep(6)
        
#         elif lengthoftext >= 55:
#             sleep(8)
            
#         elif lengthoftext >= 70:
#             sleep(10)
        
#         elif lengthoftext >= 100:
#             sleep(13)
            
#         elif lengthoftext >= 120:
#             sleep(14)
            
#         else:
#             sleep(2)

