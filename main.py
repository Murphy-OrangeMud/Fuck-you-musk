from config import *
import random
import tweepy

random_bullshit = [
    "Elon Musk should eat shit today",
    "Fuck Elon Musk, Twitter won't work",
    "What the fuck Elon Musk",
    "Who the fuck will care Twitter",
    "Eat shit, Elon Musk",
    "Eat shit and die, mother fucker Elon Musk",
    "Twitter sucks",
    "Who the hell died and made you boss Elon Musk",
    "Blow yourself, Elon Musk",
    "Elon Musk has got his head up his ass",
    "Kiss my ass, Elon Musk",
    "Elon Musk is a fucking retard"
]

def random_bullshit_generator():
    idx = random.randint(0, len(random_bullshit))
    return random_bullshit[idx]

def main():
    client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    client.create_tweet(text=random_bullshit_generator())

if __name__ == "__main__":
    main()


