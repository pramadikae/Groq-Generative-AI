from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-groq-api-key")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.1-8b-instant"

app = FastAPI()

# Fungsi async untuk streaming response dari Groq API
async def stream_groq_response(messages):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": True  # Aktifkan streaming
    }
    # Kirim request ke Groq API secara streaming
    async with httpx.AsyncClient(timeout=60.0) as client:
        async with client.stream("POST", GROQ_API_URL, headers=headers, json=payload) as response:
            async for chunk in response.aiter_text():
                yield chunk  # Kirim setiap chunk ke client

# Endpoint utama untuk menerima pertanyaan user
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()  # Ambil data JSON dari request
    messages = data.get("messages", [])  # Ambil list pesan
    # Kembalikan response streaming ke client
    return StreamingResponse(stream_groq_response(messages), media_type="text/event-stream")
