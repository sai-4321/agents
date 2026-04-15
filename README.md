
 🌦️ Weather Suggestion App (Agentic AI)

📌 Overview

This project is a simple AI-powered app that:

 Fetches real-time weather data
 Uses AI to generate clothing and skincare suggestions
 Displays everything in a simple web UI

It combines API + AI + UI, which is a good foundation for learning Agentic AI.


 🚀 Features

 🌍 Enter any city name
 🌡️ View temperature and humidity
 🤖 Get AI-based suggestions:

 Clothing recommendations
 Skincare tips
 📊 Clean interface using Streamlit

 🛠️ Tech Stack

 Python
 Streamlit
 OpenWeatherMap API
 Google Gemini (google-genai)
 Requests
 python-dotenv

📂 Project Structure

agents/
 ├── app.py
 ├── .env
 ├── requirements.txt
 └── README.md

 ⚙️ Installation

 1. Clone the repository

```bash
git clone https://github.com/sai-4321/agents.git
cd agents
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the environment

 Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install streamlit google-genai requests python-dotenv
```

---

🔑 Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

 ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

🧠 How It Works

1. User enters a city
2. App fetches weather data from OpenWeather API
3. Data is sent to Gemini AI
4. AI returns suggestions
5. Results are displayed on the screen

---

 ⚠️ Important Note

* Do NOT hardcode API keys in your code
* Move your OpenWeather API key to `.env`

---

🔮 Future Improvements

* Add more weather details (wind, UV index)
* Improve AI response quality
* Add voice input
* Build a full agent with decision-making logic



