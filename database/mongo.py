
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_URI)
db = client["executiiebot"]

stories = db["stories"]
episodes = db["episodes"]
requests = db["requests"]
users = db["users"]
