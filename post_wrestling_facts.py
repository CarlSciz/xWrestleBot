import tweepy
from profightdb_scrape import parseMainEvent
from credentials import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN
from datetime import datetime

# Parse event details and main event
event_details, main_event = parseMainEvent()

# Construct status message
status_message = ""

if event_details[0] != '':
    status_message = (
        f"On This Wrestle Date In History: {event_details[1]}\n"
        f"Promotion: {event_details[3]} at the {event_details[2]}\n\n"
    )

if main_event[0] != '':
    status_message += "The main event on the card:\n"
    status_message += f"{main_event[0]} {main_event[1]} {main_event[2]}\n"
    if main_event[3] != '':
        status_message += f"in {main_event[3]}\n"
    if main_event[4] != '':
        status_message += f"in a {main_event[4]}\n"
    if main_event[5] != '':
        status_message += f"for the {main_event[5]}\n"


# Authenticate with Tweepy Client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,  
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Post the tweet
try:
    if status_message.strip():  # Ensure there's content to post
        response = client.create_tweet(
            text=status_message
        )
        print("Wrestle Tweet Posted successfully!")
        print(f"Tweet ID: {response.data['id']}")
    else:
        print("No content to post.")
except tweepy.TweepyException as e:
    print(f"Error posting tweet: {e}")
