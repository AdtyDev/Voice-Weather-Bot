**🌦️ Voice Weather Bot**

A simple Python script that fetches the current temperature of a user-specified location using the WeatherAPI and speaks it aloud using a built-in voice assistant (Windows only).

🧠 Why Build This?

This project helps you understand and apply **essential Python programming concepts**:

- ✅ Working with external APIs using `requests`
- ✅ Parsing JSON responses
- ✅ Using `win32com.client` for text-to-speech (TTS) on Windows
- ✅ User input and string formatting
- ✅ Practical integration of real-time data with Python scripting

It's perfect for learners who want to combine Python with real-world applications like weather updates and system speech.


📋 Features

- 🌍 Takes your location as input
- ☁️ Fetches real-time temperature from [WeatherAPI](https://www.weatherapi.com/)
- 🗣️ Speaks the temperature aloud using your Windows voice assistant


🔧 Technologies Used

- Python 3
- `requests` – for sending HTTP requests
- `json` – to parse API response
- `win32com.client` – for TTS on Windows

🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/weather-voice-assistant.git
cd weather-voice-assistant
```


**Install dependencies**:
pip install requests pywin32

#To run the file
python weather_bot.py
