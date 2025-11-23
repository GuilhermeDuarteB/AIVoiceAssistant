import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import google.generativeai as genai

#API Key for Google Gemini

api_key = "your_google_gemini_api_key_here"

#AI configuration

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    print(f"Error configuring Google Gemini API: {e}")
    exit(1)

# Initialize the speech engine
def speak(text):
    print(f"Assistant: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error initializing text-to-speech engine: {e}")

# AI query function
def ai_ask(promp):
    """ASK to AI model and get response"""
    try:
        rules = "You are a helpful assistant. Answer in the questioner's language. Dont use more than 50 words." \
        "be nice and polite while answering. If you don't know the answer, just say that you don't know, don't try to make up an answer. if he say goodbye, reply with goodbye" \
        " message and stop the conversation."

        full_prompt = f"{rules}\n\nUser: {promp}"

        response = model.generate_content(full_prompt)

        #clean weird characters from response
        clean_text = response.text.replace("*", " ")
        return clean_text
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "I'm sorry, I couldn't process your request at the moment."
    
# wish user function
def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you today?")

# take command function
def take_command():
    return input("You: (type your command) ").lower()


# main function
def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day!")
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        else:
            speak("Let me think about that.")
            response = ai_ask(query)
            speak(response)

if __name__ == "__main__":
    run_assistant()