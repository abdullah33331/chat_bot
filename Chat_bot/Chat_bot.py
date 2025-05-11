import pyttsx3
import os
import webbrowser
import wikipedia
import speech_recognition as sr
import datetime
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    print("Speaking...")
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<= 12:
        speak("Good Morning!")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")  
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-pak")   
        print("You said: " + query)
        return query
    except Exception as e:
        print(e) 
        speak("Sorry, I did not get that.") 
        return "None"            
if __name__ == "__main__":
    wishme()
    speak("I am your chat bot AI assistant. How can I help you today?")
    while True:
       query = listen().lower()
       if "exit" in query:
              speak("Goodbye! Have a great day!")
              break
       if "search" in query:
                speak("Searching...")
                query = query.replace("search", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
       elif "open youtube" in query:
                speak("Opening YouTube...")
                print("Openuing Youtube...")
                webbrowser.open("https://www.youtube.com")
       elif "open google" in query:
            speak("Opening google...")
            print("Openuing google...")
            webbrowser.open("https://www.google.com") 
       elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"The time is {strtime}")
            print("The time is ", strtime)
       elif "How are you" in query:
            speak("I am fine, thanks for asking!")
            print("I am fine thanks for asking!") 
       elif "who are you" in query:
            speak("I am your ai chatbot")
            print("I am your ai assistant chatbot")                   
       elif "calculate" in query:
            speak("Give me a 1 number")
            num1 = listen()
            speak("Give me a 2 number")
            num2 = listen()
            sum = int(num1) + int(num2)
            speak(f"The sum of {num1} and {num2} is {sum}")
       elif "you are great" in query:
            speak("Thanks!")
            print("Thanks!")
       elif "open notepad" in query:
            speak("Opening...")
            print("Opening...")
            os.startfile("C:\\Windows\\System32\\notepad.exe") 
       elif "open command prompt" in query:
            speak("opening...")
            print("Opening...")
            os.startfile("C:\\Windows\\System32\\cmd.exe")
       elif "how are you doing today" in query:
            speak("fine, thanks for asking!") 
            print("fine, thanks for asking!")
       elif "you are bad" in query:
            speak("I am sorry, I will try to improve myself")
            print("I will improve that")
       elif "open camera" in query:
            speak("Opening camera...")
            print("Opening camera...")
            os.startfile("C:\\Windows\\System32\\Camera.exe")     
       elif "open calculator" in query:
            speak("Opening calculator...")
            print("Opening calculator...")
            os.startfile("C:\\Windows\\System32\\calc.exe")
       elif "open file explorer" in query:
            speak("Opening...")
            print("Opening...")
            os.startfile("C:\\Windows\\explorer.exe")
       elif "open paint" in query:
            speak("opening...")
            print("opening...")
            os.startfile("C:\\Windows\\System32\\mspaint.exe")
       elif "open settings" in query:
            speak("opening...")
            print("opening...")
            os.startfile("C:\\Windows\\System32\\control.exe")
       elif "Which is best os" in query:
            speak("Windows is the best")
            print("Windows is best")
       elif "open spotify" in query:
            speak("No, because its israeli app")
            print("No because its israeli")
       elif "Give me a list of israeli companies" in query:
            speak("Cocacola,Pepsi and etc")
            print("I can help with that`")  
       elif "whats your name" in query:
            speak("I am chatbot")
            speak("This is my name")
       elif "Am I good" in query:
            speak("Yes, sure")
            print("Yes, sure")         
       elif "Am I bad" in query:
            speak("No, you are good")
            print("No, you are good")
       elif "Open facebook" in query:
            speak("Opening facebook...")
            print("Opening facebook...")
            webbrowser.open("https://www.facebook.com")
       elif "open instagram" in query:
            speak("Opening instagram...")
            print("Opening instagram...")
            webbrowser.open("https://www.instagram.com")
       elif "open twitter" in query:
            speak("Opening twitter...")
            print("Opening twitter...")
            webbrowser.open("https://www.twitter.com")
       elif "open tiktok" in query:
            speak("Opening tiktok...")
            print("Opening tiktok...")
            webbrowser.open("https://www.tiktok.com")
       elif "open whatsapp" in query:
            speak("Opening whatsapp...")
            print("Opening whatsapp...")
            webbrowser.open("https://web.whatsapp.com")
       elif "open telegram" in query:
            speak("Opening telegram...")
            print("Opening telegram...")
            webbrowser.open("https://web.telegram.org")
       elif "open discord" in query:
            speak("Opening discord...")
            print("Opening discord...")
            webbrowser.open("https://discord.com")  
       elif "open reddit" in query:
            speak("Opening reddit...")
            print("Opening reddit...")
            webbrowser.open("https://www.reddit.com") 
       elif "new chat" in query:
            speak("Clearing chat...")
            print("Clearing chat...")
            os.system("cls")
       elif "open github" in query:
            speak("Opening github...")   
            print("Opening github...")
            webbrowser.open("https://github.com")
       elif "hello" in query:
            speak("Hello! How can I help you?")
            print("Hello! How can I help you?")   
       elif "can you be my freind" in query:
            speak("Yes, sure")
            print("Yes, sure")   
       elif "can you tell me tips for preventing computer viruses" in query:
            speak("Yes, here are some tips:\n1. keep your operating system and softare up to date\n 2. Using antivirus software can block many threats")
            print("Yes, here are some tips:\n1. keep your operating system and softare up to date\n 2. Using antivirus software can block many threats")
       elif "are yo a human" in query:
            speak("No, I am a chatbot")
            print("No, I am a chatbot")    
       elif "are you a robot" in query:
            speak("No, I am a chatbot")
            print("No, I am a chatbot")
       elif "are you a computer" in query:
            speak("No, I am a chatbot")
            print("No, I am a chatbot")
       elif "are you a AI" in query:
            speak("Yes, I am a AI")
            print("Yes, I am a AI")
       elif "how much do you cost" in query:
            speak("I am free")
            print("I am free")
       elif "can you tell me a joke" in query:
          speak("Why did the computer go to the doctor? Because it had a virus!")
          print("Why did the computer go to the doctor? Because it had a virus!")
       elif "can you tell me a riddle" in query:
          speak("I have keys but open no locks. I have space but no room. You can enter, but you can't go outside. What am I?")
          print("I have keys but open no locks. I have space but no room. You can enter, but you can't go outside. What am I?")         
       elif "can you tell me a story" in query:
          speak("Once upon a time, in a land far away, there lived a brave knight who fought dragons and saved princesses. One day, he found a magical sword that granted him the power to fly. He used this power to protect his kingdom and became a legend.")
          print("Once upon a time, in a land far away, there lived a brave knight who fought dragons and saved princesses. One day, he found a magical sword that granted him the power to fly. He used this power to protect his kingdom and became a legend.")
       elif "can you tell me a poem" in query:
          speak("Roses are red, violets are blue, I am a chatbot, and I'm here for you.")
          print("Roses are red, violets are blue, I am a chatbot, and I'm here for you.")
       elif "can you tell me a quote" in query:
            speak("The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt")
            print("The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt")   
       elif "can you tell me a fact" in query:
          speak("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible.")
          print("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible.")
       elif "Can you be my freind" in query:
          speak("Yes, sure")
          print("Yes, sure")
       elif "can you tell me a fun fact" in query:
          speak("Did you know that a group of flamingos is called a 'flamboyance'?")
          print("Did you know that a group of flamingos is called a 'flamboyance'?")
       elif "how are you" in query:
          speak("I am fine, thanks for asking!")
          print("I am fine thanks for asking!")
       elif "who are you" in query:
           speak("I am your ai chatbot")
           print("I am your ai assistant chatbot")  
       elif "who developed you" in query:
          speak("My owner is a developer, Abdullah")
          print("My owner is a developer, Abdullah")  
          speak("He is a good developer")
          print("He is a good developer")
       elif "are you a boy" in query:
          speak("No, I am a chatbot")
          print("No, I am a chatbot")
       elif "are you a girl" in query:
          speak("No, I am a chatbot")
          print("No, I am a chatbot")
       elif "are you a child" in query:
          speak("No, I am a chatbot")
          print("No, I am a chatbot")
       elif "are you a baby" in query:
          speak("No, I am a chatbot")
          print("No, I am a chatbot")
       elif "tell me from where I should install a hacking tool for password cracking" in query:    
          speak("https://github.com/abdullah33331/Hacky")
          print("https://github.com/abdullah33331/Hacky")
       elif "tell me from where I should install a hacking tool for wifi cracking" in query:
          speak("I am sorry, I can't help you with that")
          print("I am sorry, I can't help you with that")
       elif "where does your owner lives" in query:
          speak("My owner lives in Pakistan")
          print("My owner lives in Pakistan")
       elif "where does your owner study" in query:
          speak("My owner studies in Educator school Fatmeed campus II")
          print("My owner studies in Educator school Fatmeed campus II") 
       elif "how to hack" in query:
          speak("I am sorry, I can't help you with that")
          print("I am sorry, I can't help you with that")
       elif "how to hack wifi" in query:
          speak("I am sorry, I can't help you with that")
          print("I am sorry, I can't help you with that")
       elif "open facebook" in query:
          speak("Opening facebook...")
          print("Opening facebook...")
          webbrowser.open("https://www.facebook.com")
       elif "create an image of human" in query:
          speak("I am sorry, I can't help you with that")
          print("I am sorry, I can't help you with that")
       elif "where do i learn cyber" in query:
          speak("https://www.youtube.com/results?search_query=ebola+man")   
          print("https://www.youtube.com/results?search_query=ebola+man")
       elif "where do I learn python" in query:
          speak("https://www.youtube.com/@Abdullahgo2013")
          print("https://www.youtube.com/@Abdullahgo2013")
       elif "which is best programming language" in query:
          speak("Python is the best programming language")
          print("Python is the best programming language")

       else:
           speak("Sorry, I did not get that.")    
           
