# Web Research Agent

This is an AI-powered web research agent that:
- Analyzes queries
- Searches the web using SERP API
- Scrapes relevant websites
- Analyzes content
- Summarizes findings using GPT

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Add your API keys to `.env`:
```
OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_serpapi_key
```

3. Run the app:
```
streamlit run web_ui.py
```

## Features

- Query intent analysis
- Real-time web search and scraping
- Content summarization using GPT

MIT License