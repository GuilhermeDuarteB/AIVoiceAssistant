# **🤖 Gemini AI Voice Assistant V2**

An advanced, intelligent virtual assistant written in Python that leverages the **Google Gemini API**. This version introduces a **Graphical User Interface (GUI)**, **Conversation Memory**, and Dual-Mode operation (Terminal or App).

The assistant remembers context from previous interactions, supports Dark/Light themes, and provides natural, spoken responses.

## **✨ New Features in V2**

* 💻 **GUI App Mode:** A modern, clean interface built with Tkinter featuring a chat-like experience.  
* 🌗 **Dark/Light Themes:** Toggle between Light and Dark modes instantly within the App.  
* 🧠 **Contextual Memory:** The assistant now remembers the last **15 interactions** using a JSON database, allowing for continuous and contextual conversations.  
* 🔄 **Dual Operation:** Choose between **Terminal Mode** (classic) or **App Mode** (GUI) upon startup.

### **Core Features**

* 🗣️ **Text-to-Speech (TTS):** Vocalizes responses using pyttsx3.  
* 🌍 **Multilingual:** Automatically detects the language of your query and responds in the same language.  
* ⚡ **Concise Responses:** Optimized system prompts for short, conversational answers.

## **🛠️ Prerequisites**

Before you begin, ensure you have **Python** installed. You will also need a Google Gemini **API Key**.

1. Get your free API Key at [Google AI Studio](https://aistudio.google.com/).

## **📦 Installation**

1. **Clone the repository:**  
   git clone \[https://github.com/GuilhermeDuarteB/AIVoiceAssistant.git\](https://github.com/GuilhermeDuarteB/AIVoiceAssistant.git)  
   cd AIVoiceAssistant

2. **Install dependencies:**  
   pip install google-generativeai pyttsx3 speechrecognition

   *(Note: tkinter, json, and os are standard Python libraries and usually do not require installation).*

## **⚙️ Configuration**

1. Open main.py.  
2. Locate the api\_key variable.  
3. Replace the placeholder text with your actual API key:  
   \# In main.py  
   api_key = "your_google_gemini_api_key_here"

⚠️ **Security Warning:** Never commit your API Key to GitHub. If you plan to make this repository public, consider using environment variables (os.environ) or a .env file to handle secrets.

## **🚀 Usage**

Run the script via terminal:

python main.py

### **Choosing a Mode**

When you run the script, you will be asked:

*"How do you want to interact with me? Terminal or APP?"*

1. **Type app**: Launches the Graphical Interface with buttons and chat history.  
2. **Type terminal**: Runs the classic command-line interface.

### **Example Interaction (Memory Test):**

* **You:** "My name is Guilherme."  
* **Assistant:** "Nice to meet you, Guilherme."  
* **You:** "What is my name?"  
* **Assistant:** "Your name is Guilherme." *(The AI remembers context from the JSON memory file)*.

## **📂 Code Structure**

* **app\_mode()**: Handles the GUI setup, themes (Light/Dark), and event listeners for the windowed application.  
* **load\_memory() / save\_memory()**: Manages the memory.json file to store and retrieve conversation history.  
* **ai\_ask(prompt)**: Sends the prompt \+ **conversation history** to Gemini to generate context-aware responses.  
* **speak(text)**: Handles text-to-speech output.

## **🔮 Roadmap**

* \[ \] **Voice Input for GUI:** Add a microphone button to the App interface.  
* \[ \] **Executable Build:** Create a .exe file using PyInstaller for easier distribution.  
* \[ \] **Custom Themes:** Allow users to define custom color palettes in a config file.

## **🤝 Contribution**

Contributions are welcome\! Feel free to open **Issues** or submit **Pull Requests**.

## **📄 License**

This project is licensed under the MIT License. See the LICENSE file for details.
