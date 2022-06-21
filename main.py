import os

from dotenv import load_dotenv
from functions.sleep import *
import rich

VERSION = 1.0
load_dotenv()

rich.print("[bold cyan]Twitter[/bold cyan] Video Maker Bot")
rich.print("version", VERSION)

sleep_3()

print("")
print("")
print("")


def load_env_variables():
    rich.print('|--------------------------------------------------------------------|')
    rich.print('|Checking .env file for API Keys...                                  |')
    rich.print('|____________________________________________________________________|')

    twitter_api_key = os.getenv("TWITTER_API_KEY")
    twitter_secret = os.getenv("TWITTER_SECRET")
    twitter_bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

    sleep_1()

    rich.print('|--------------------------------------------------------------------|')
    rich.print('|[green]API Keys loaded ✔[/green]️                                                   |')
    rich.print('|____________________________________________________________________|')


load_env_variables()


