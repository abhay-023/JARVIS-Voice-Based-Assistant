# 🤖 Jarvis - Python Voice Assistant

Jarvis is a voice-controlled AI assistant built using Python. It can perform a wide range of tasks such as opening websites, telling jokes, managing tasks, sending emails, fetching weather reports and news, and much more — all triggered by your voice!

---

## 📌 Features

- **Greeting & Voice Interaction**
  - Greets you based on the time of day.
  - Uses text-to-speech (TTS) to interact with the user.

- **Voice Command Processing**
  - Uses microphone input and Google's Speech Recognition API to interpret voice commands.

- **Web Automation**
  - Opens websites like Google, YouTube, and StackOverflow.

- **Email Sending**
  - Sends emails to predefined contacts using Gmail and SMTP.
  
- **Weather Forecast**
  - Provides live weather updates using OpenWeatherMap API.

- **News Headlines**
  - Reads the latest news using the NewsAPI.

- **Task Manager**
  - Add and list tasks using voice commands.

- **Fun Interaction**
  - Tells jokes and random fun facts.

- **System Control**
  - Shutdown, restart, and log off the system.

- **Search Google**
  - Searches your queries directly on Google.

- **Alarm**
  - Set a simple alarm that notifies at the specified time.

- **Calculator**
  - Evaluates basic arithmetic expressions.

---

## 🧰 Technologies Used

- `Python 3.x`
- `pyttsx3` - Text-to-speech conversion
- `speech_recognition` - Voice recognition
- `wikipedia` - Fetches Wikipedia summaries
- `webbrowser` - Opens URLs
- `smtplib` - Sends emails
- `requests` - For APIs (Weather, News)
- `pyjokes` - Generates jokes
- `os` & `datetime` - System operations & time
- `dotenv` - Load environment variables (for API keys and credentials)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis-assistant.git
cd jarvis-assistant
