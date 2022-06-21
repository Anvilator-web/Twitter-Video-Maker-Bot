import os


from sleep import *
# from animations.loading_animation import animate


def load_env_variables():
    print('Checking .env file for API Keys...')

    twitter_api_key = os.getenv("TWITTER_API_KEY")
    twitter_secret = os.getenv("TWITTER_SECRET")
    twitter_bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

    sleep_2()
    print('API Keys loaded')

