import tweepy

API_KEY = 'IGNYruFmXlZPnJMErlWgWKyab'
API_SECRET_KEY = 'EKZYfwTAMcl5yW2qJlJFrA9lP4DKnyWi7zlAyrNHhkr45Fc2Gy'
ACCESS_TOKEN = '1590435349808893952-2Tm4iwRFZMURuiMtHX29nJwKVtS4Rt'
ACCESS_TOKEN_SECRET = 'W3d0R2a8rdN2aDdFWKBfpr9TJ08bZ1dBs0o3dN6bIsFJ2'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOSlwQEAAAAA5rrXlbqC9oru5KZ9ibB28t0OhkU%3DTnllcJGgaj3e0DTkAM4sstjpGDOvQNeOxcYUR0YW8Ic7xnLoWp'

# Authenticate using the Client for API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET_KEY,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

# Authenticate with OAuth1 for media upload
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Upload media
media = api.media_upload('gojo.jpg')

# Post a tweet with media
tweet_text = "Hello Twitter! This tweet has an image!"
response = client.create_tweet(
    text=tweet_text, media_ids=[media.media_id_string])

print("Tweet posted successfully with media! Tweet ID:", response.data['id'])
