import os

from dotenv import load_dotenv
from functions.sleep import *

VERSION = 1.0
load_dotenv()

print("Twitter Video Maker Bot")
print("version", VERSION)

sleep_3()

def load_env_variables():
    print('Checking .env file for API Keys...')

    twitter_api_key = os.getenv("TWITTER_API_KEY")
    twitter_secret = os.getenv("TWITTER_SECRET")
    twitter_bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

    sleep_2()
    print('API Keys loaded')

load_env_variables()





