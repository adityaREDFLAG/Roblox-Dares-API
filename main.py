
from fastapi import FastAPI
import random

app = FastAPI()

dares = [
  "Give your crush 10$ Robux Gift Card ❤️", "Play MM2 with an auto clicker 🤪", "Change your dispaly name to ROADBLOCKS 🔲", "Subscribe to adityaredflag 🔥", "Who's the worst Roblox youtuber? 😤", "What's the worst Roblox Event in history 🤔", "Ask your crush on a Roblox date 😏",
  "Tell a person your going to donate 10 robux and leave the game"
        ]

@app.get("/")
async def get_random_dares():
    random_dares = random.choice(dares)
    return { "dares": random_dares
           }