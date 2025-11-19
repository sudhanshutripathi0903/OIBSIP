import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am your voice assistant.")
speak("How can I help you today?")

while True:
    command = input("Type your command: ").lower().strip()

    if "hello" in command or "hi" in command:
        speak("Hello Sudhanshu, how are you?")
        print("Assistant: Hello Sudhanshu, how are you?")
    elif "time" in command:
        speak("Sorry, time telling is not added yet.")
        print("Assistant: Time telling not added.")
    elif "your name" in command or "who are you" in command:
        speak("My name is Python Assistant.")
        print("Assistant: My name is Python Assistant.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye")
        print("Assistant: Goodbye")
        break
    else:
        speak("Sorry, I did not understand.")
        print("Assistant: Sorry, I did not understand.")
