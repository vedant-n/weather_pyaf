# Weather Query Agent App

A minimal full-stack web application built for the SanchAI Analytics internship assessment.

Users can type natural language queries like "What's the weather in Pune?" or "Weather of Mumbai today?" and receive real-time weather information powered by an agentic AI workflow.

## Features

- **Frontend**: React – clean input form with instant response display  
- **Backend**: FastAPI – handles user queries via REST API  
- **Agentic AI**: LangGraph + OpenRouter (free Llama model) – intelligently decides when to call the weather tool  
- **Weather Tool**: Real-time data from OpenWeatherMap (free tier)  
- Simple, responsive UI with clear feedback

## Tech Stack

- **Frontend**: React, Axios  
- **Backend**: FastAPI, Uvicorn  
- **AI/Agent**: LangChain, LangGraph, OpenRouter (via ChatOpenAI compatibility), OpenWeatherMap API  
- **Environment**: Python dotenv for secrets

## Setup & Running Locally

### Prerequisites
- Node.js (for frontend)
- Python 3.10+ (for backend)
- Free API keys:
  - [OpenWeatherMap](https://openweathermap.org/api) (Current Weather API)
  - [OpenRouter](https://openrouter.ai/keys) (free tier with Llama models)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
