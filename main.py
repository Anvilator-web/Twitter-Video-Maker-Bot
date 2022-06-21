import os

from dotenv import load_dotenv
from functions.sleep import *
import rich

VERSION = 1.0
load_dotenv()

rich.print("[bold cyan]Twitter[/bold cyan] Video Maker Bot")
rich.print("version", VERSION)

sleep_3()

def load_env_variables():
    rich.print('Checking .env file for API Keys...')

    twitter_api_key = os.getenv("TWITTER_API_KEY")
    twitter_secret = os.getenv("TWITTER_SECRET")
    twitter_bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

    sleep_2()
    rich.print('API Keys loaded')

load_env_variables()







