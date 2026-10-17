import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SENT_DM_API_KEY")

if api_key:
    print("Success: API key loaded.")
else:
    print("API key not found. Check your .env file.")