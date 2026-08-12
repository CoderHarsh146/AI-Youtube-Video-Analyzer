# 🎥 AI Youtube Video Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Agno](https://img.shields.io/badge/Framework-Agno-purple)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange)
![License](https://img.shields.io/badge/License-MIT-green)


An AI-powered YouTube Video Analyzer built using **Agno**, **OpenAI**, and **Streamlit**.

Simply paste a YouTube video URL and get a detailed AI-generated analysis, including:

- 📚 Video Overview
- ⏱️ Smart Timestamps
- 📝 Detailed Summary
- 🎯 Key Topics & Insights
- 💡 Key Learning Points

---

## Features

- AI-powered video analysis
- Structured and easy-to-read output
- Smart timestamp generation
- Markdown formatted responses
- Clean and interactive Streamlit dashboard

---

## Tech Stack

- Python
- Streamlit
- Agno Framework
- GROQ API
- YouTube Tools

---

## Project Structure

```
AI-Youtube-Video-Analyzer/
│
├── ui.py
├── youtube_analyzer.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Youtube-Video-Analyzer.git
```

Move into the project directory:

```bash
cd AI-Youtube-Video-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run ui.py
```

---

## Usage

1. Launch the Streamlit application.
2. Paste a YouTube video URL.
3. Click **Analyze Video**.
4. View the AI-generated analysis.

---

## Disclaimer

- AI-generated content may contain inaccuracies.
- Always verify important information before relying on the generated analysis.
- Response quality depends on the AI model and API tier being used.

---

## License

This project is available for educational and personal use.
