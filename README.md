# J.A.R.V.I.S. AI 🤖 🗨️ 💻

![S6RP7.gif](https://s6.gifyu.com/images/S6RP7.gif)

## Introduction 📢

J.A.R.V.I.S. AI is a real-time voice-controlled artificial intelligence system that simulates the capabilities of the famous AI assistant from the Iron Man movies. It's designed to provide an interactive and dynamic user experience, offering features like speech recognition 🎙️, natural language processing, web automation 🌐, and more. With J.A.R.V.I.S. AI, you can perform tasks using voice commands 🔊, get answers to questions ❓, chat through WhatsApp 📱, and even wake up the system with a simple clap 👏 or keyword 🔑.

Look at my LinkedIn post to see J.A.R.V.I.S. AI in action:



## Table of Contents 📚

- [J.A.R.V.I.S. AI 🤖 🗨️ 💻](#jarvis-ai--️-)
  - [Introduction 📢](#introduction-)
  - [Table of Contents 📚](#table-of-contents-)
  - [Features ⭐](#features-)
  - [Getting Started 🚀](#getting-started-)
    - [Prerequisites ⚙️](#prerequisites-️)
    - [Installation 💻](#installation-)
  
## Features ⭐

- Voice-controlled AI system 🎙️
- Speech recognition with `pyaudio` 🔊
- Text-to-speech functionality using `pyttsx3` 🔊
- Web automation and scraping capabilities through `selenium webdriver` 🌐
- Natural language processing with `openai` 💭
- Voice-activated wake-up on clapping 👏 or using a specific keyword 🔑
- Launching web applications and software with voice commands 💻
- Voice chat via WhatsApp 📱

## Getting Started 🚀

### Prerequisites ⚙️

Before you can run J.A.R.V.I.S. AI, you'll need to have the following installed on your system:

- Python (3.x recommended) 🐍
- Python packages like `pyaudio`, `pyttsx3`, `selenium`, `openai`, and others. You can install them using `requirements.txt`.

### Installation 💻

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/I-AdityaGoyal/VoiceAssistant-JarvisAI.git
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configuration Instructions:
   -To Do:
      - Download Chrome Webdriver according to your chrome version 🌐
      ```bash
      Link:  https://chromedriver.chromium.org/downloads
      ```
      - Extract the chromedriver.exe from the folder and paste it in the Database Folder.

      - Now, navigate to the Data Folder and in Api.txt, paste your OpenAI API Key 🔑

      - At last, go to the SocialMedia folder and open Whatsapp.py. In Line no. 28, there is a Dict. named with ListWeb. Replace the name and there WhatsApp contact number 📱

      ```bash
      ListWeb = {'name_1' : "+91XXXXXXXXXX",
            'name_2': "+91XXXXXXXXXX",
            'name_3': '+91XXXXXXXXXX',
            'name_4': '+91XXXXXXXXXX',
            'name_5': '+91XXXXXXXXXX'}
      ```


   - Launch Jarvis.py 🚀
   ```bash
   Run Jarvis.py file on your IDE & Have Fun! 🎉
   ```
