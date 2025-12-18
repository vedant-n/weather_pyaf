from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@tool
def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return "Weather API key missing"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Couldn't fetch weather for that city"
    
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"It's currently {temp}°C in {city} with {desc}."

llm = ChatOpenAI(
    model="meta-llama/llama-3.3-70b-instruct:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

system_message = SystemMessage(content="You are a helpful assistant that can answer questions. Use the get_weather tool when the user asks about weather in a city.")

tools = [get_weather]
agent = create_react_agent(llm, tools, messages_modifier=system_message)

class Query(BaseModel):
    message: str

@app.post("/query")
async def handle_query(query: Query):
    try:
        input_messages = [HumanMessage(content=query.message)]
        result = agent.invoke({"messages": input_messages})
        last_message = result["messages"][-1]
        return {"response": last_message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)