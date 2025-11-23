# **🤖 Gemini AI Voice Assistant**

A lightweight, intelligent virtual assistant written in Python that leverages the **Google Gemini API** to provide natural, context-aware, spoken responses.

The assistant is capable of conversing in multiple languages (adapting to the user's input), telling the time, and providing concise answers using Text-to-Speech synthesis.

## **✨ Features**

* 🧠 **Artificial Intelligence:** Powered by the Gemini Flash model for fast and intelligent responses.  
* 🗣️ **Text-to-Speech (TTS):** Vocalizes responses using the pyttsx3 library.  
* 🌍 **Multilingual:** Automatically detects the language of your query and responds in the same language.  
* ⏰ **Dynamic Greeting:** Wishes "Good Morning," "Good Afternoon," or "Good Evening" based on the current system time.  
* ⚡ **Concise Responses:** System prompts are engineered to keep answers short (max \~50 words) and direct, optimized for voice interaction.

## **🛠️ Prerequisites**

Before you begin, ensure you have **Python** installed on your machine. You will also need a Google Gemini **API Key**.

1. Get your free API Key at [Google AI Studio](https://aistudio.google.com/).

## **📦 Installation**

1. **Clone the repository:**  
   git clone [https://github.com/GuilhermeDuarteB/AIVoiceAssistant.git](https://github.com/GuilhermeDuarteB/AIVoiceAssistant.git)
   
   cd AIVoiceAssistant

3. Install dependencies:  
   Install the required libraries using pip:  
   pip install google-generativeai pyttsx3 speechrecognition

## **⚙️ Configuration**

1. Open the main.py file.  
2. Locate the api\_key variable.  
3. Replace the placeholder text with your actual API key:  
   \# In main.py  
   api\_key \= "YOUR\_ACTUAL\_API\_KEY\_HERE"

⚠️ **Security Warning:** Never commit your API Key to GitHub. If you plan to make this repository public, consider using environment variables (os.environ) or a .env file to handle secrets.

## **🚀 Usage**

Run the script via terminal:

python main.py

### **Example Commands:**

The assistant accepts text input (via keyboard) and responds with voice.

* **You:** "What time is it?"  
  * **Assistant:** "The time is 14:30."  
* **You:** "How do I make an omelet?"  
  * **Assistant:** (Responds with a quick summary recipe)  
* **You:** "Exit" or "Quit"  
  * **Assistant:** "Goodbye\! Have a great day\!"

## **📂 Code Structure**

* speak(text): Initializes the TTS engine and vocalizes the provided text.  
* ai\_ask(prompt): Sends the user prompt to Google Gemini with system instructions (short, polite answers) and returns cleaned text.  
* wish\_user(): Checks the system time to provide the appropriate greeting.  
* run\_assistant(): The main loop that keeps the conversation active until an exit command is received.

## **🔮 Roadmap**

* \[ \] **Voice Input Activation:** The code already imports speech\_recognition. The next step is to replace input() with microphone listening logic.  
* \[ \] **System Commands:** Add capabilities to open specific websites (YouTube, Google) or applications.  
* \[ \] **Conversation Memory:** Allow the assistant to remember context from previous questions.

## **🤝 Contribution**

Contributions are welcome\! Feel free to open **Issues** or submit **Pull Requests**.

## **📄 License**

This project is licensed under the MIT License. See the LICENSE file for details.
