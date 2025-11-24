# import necessary libraries

from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import google.generativeai as genai
import json
import os

#gemini api key
api_key = "your_google_gemini_api_key_here"

#AI config

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    print(f"Error configuring Google Gemini API: {e}")
    exit(1)

# Memory functions

def load_memory():
    if not os.path.exists("memory.json"):
        with open("memory.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_memory(mem):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=4, ensure_ascii=False)

conversation_history = load_memory()

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
        global conversation_history

        rules = "You are a helpful assistant. Answer in the questioner's language. Dont use more than 50 words." \
        "be nice and polite while answering. If you don't know the answer, just say that you don't know, don't try to make up an answer. if he say goodbye, reply with goodbye" \
        " message and stop the conversation."

        # perma memory - last 15 interactions
        history_text = ""
        for item in conversation_history[-15:]:
            history_text += f"User: {item['user']}\nAI: {item['ai']}\n"

        full_prompt = f"{rules}\n\nConversation so far:\n{history_text}\n\nUser: {promp}"

        response = model.generate_content(full_prompt)

        clean_text = response.text.replace("*", " ")

        # save to memory
        conversation_history.append({"user": promp, "ai": clean_text})
        save_memory(conversation_history)

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


#app mode function
def app_mode():
    window = Tk()
    window.title("AI Assistant")
    window.geometry("830x600")
    window.resizable(False, False)
    window.iconbitmap("voice-app.ico")

    # LM colors
    LIGHT = {
        "BG_MAIN": "#E9EEF3",
        "BG_TOP": "#D0D7DF",
        "BG_CHAT": "#FFFFFF",
        "BG_INPUT": "#F2F5F7",
        "BORDER": "#C5CCD3",
        "BTN": "#6BA4FF",
        "BTN_H": "#5A91EB",
        "TEXT": "#2A2F33"
    }

    # DM colors
    DARK = {
        "BG_MAIN": "#1E1E1E",
        "BG_TOP": "#2A2A2A",
        "BG_CHAT": "#252526",
        "BG_INPUT": "#3C3C3C",
        "BORDER": "#444444",
        "BTN": "#3A6DD8",
        "BTN_H": "#335EBF",
        "TEXT": "#FFFFFF"
    }

    theme = LIGHT  # start light mode

    def apply_theme():
        window.configure(bg=theme["BG_MAIN"])
        top_bar.configure(bg=theme["BG_TOP"])
        title_label.configure(bg=theme["BG_TOP"], fg=theme["TEXT"])
        chat_frame.configure(bg=theme["BG_CHAT"], highlightbackground=theme["BORDER"])
        chat_text.configure(bg=theme["BG_CHAT"], fg=theme["TEXT"])
        input_frame.configure(bg=theme["BG_MAIN"])
        user_entry.configure(bg=theme["BG_INPUT"], fg=theme["TEXT"])
        send_button.configure(bg=theme["BTN"], fg="white")
        theme_button.configure(bg=theme["BTN"], fg="white")

    # colors
    BG_MAIN = LIGHT["BG_MAIN"]

    window.configure(bg=BG_MAIN)

    # top bar
    top_bar = Frame(window, bg=LIGHT["BG_TOP"], height=50)
    top_bar.pack(fill=X)

    title_label = Label(
        top_bar,
        text="AI Chat Assistant",
        bg=LIGHT["BG_TOP"],
        fg="#2A2F33",
        font=("Segoe UI", 14, "bold")
    )
    title_label.pack(side=LEFT, padx=20, pady=10)

    # dark mode btn
    def toggle_theme():
        nonlocal theme
        theme = DARK if theme == LIGHT else LIGHT
        apply_theme()

    theme_button = Button(
        top_bar,
        text="🌙",
        font=("Segoe UI", 12, "bold"),
        bg=LIGHT["BTN"],
        fg="white",
        bd=0,
        cursor="hand2",
        command=toggle_theme
    )
    theme_button.pack(side=RIGHT, padx=10)

    # chat area
    chat_frame = Frame(
        window,
        bg=LIGHT["BG_CHAT"],
        bd=2,
        relief=FLAT,
        highlightbackground=LIGHT["BORDER"],
        highlightthickness=2
    )
    chat_frame.place(x=20, y=70, width=790, height=450)

    chat_text = Text(
        chat_frame,
        wrap=WORD,
        font=("Segoe UI", 11),
        bg=LIGHT["BG_CHAT"],
        fg="#2A2F33",
        bd=0,
        padx=12,
        pady=12,
        state=DISABLED
    )
    chat_text.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(chat_frame, command=chat_text.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    chat_text.config(yscrollcommand=scrollbar.set)

    # entry area
    input_frame = Frame(window, bg=BG_MAIN)
    input_frame.place(x=20, y=540, width=790, height=50)

    user_entry = Entry(
        input_frame,
        font=("Segoe UI", 12),
        bg=LIGHT["BG_INPUT"],
        fg="#2A2F33",
        bd=2,
        relief=FLAT,
        highlightcolor=LIGHT["BTN"],
        highlightthickness=1
    )
    user_entry.place(x=0, y=0, width=690, height=50)

    # send btn 
    def on_enter(e): send_button["bg"] = LIGHT["BTN_H"]
    def on_leave(e): send_button["bg"] = LIGHT["BTN"]

    send_button = Button(
        input_frame,
        text="Send",
        font=("Segoe UI", 11, "bold"),
        bg=LIGHT["BTN"],
        fg="white",
        bd=0,
        activebackground=LIGHT["BTN_H"],
        cursor="hand2"
    )
    send_button.place(x=700, y=0, width=90, height=50)

    send_button.bind("<Enter>", on_enter)
    send_button.bind("<Leave>", on_leave)

    # msg system func

    def add_message(sender, message):
        chat_text.config(state=NORMAL)
        chat_text.insert(END, f"{sender}: {message}\n\n")
        chat_text.config(state=DISABLED)
        chat_text.see(END)

    def send_message():
        user_msg = user_entry.get().strip()
        if user_msg == "":
            return

        add_message("You", user_msg)
        user_entry.delete(0, END)

        ai_response = ai_ask(user_msg)
        add_message("Gemini", ai_response)

    send_button.config(command=send_message)
    window.bind("<Return>", lambda event: send_message())

    apply_theme()
    window.mainloop()

# main function
def run_assistant():
    speak("How do you want to interact with me? Terminal or APP?")
    mode = input("Type 'terminal' for Terminal mode or 'app' for App mode: ").lower()
    if mode == 'app':
        app_mode()
        return
    else:
        speak("Entering Terminal mode.")

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
