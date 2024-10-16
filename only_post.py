import tweepy

API_KEY = 'IGNYruFmXlZPnJMErlWgWKyab'
API_SECRET_KEY = 'EKZYfwTAMcl5yW2qJlJFrA9lP4DKnyWi7zlAyrNHhkr45Fc2Gy'
ACCESS_TOKEN = '1590435349808893952-2Tm4iwRFZMURuiMtHX29nJwKVtS4Rt'
ACCESS_TOKEN_SECRET = 'W3d0R2a8rdN2aDdFWKBfpr9TJ08bZ1dBs0o3dN6bIsFJ2'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOSlwQEAAAAA5rrXlbqC9oru5KZ9ibB28t0OhkU%3DTnllcJGgaj3e0DTkAM4sstjpGDOvQNeOxcYUR0YW8Ic7xnLoWp'

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET_KEY,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

# Post a tweet
tweet_text = "Hello Twitter! This is my first tweet using Twitter API v2!"
response = client.create_tweet(text=tweet_text)

print("Tweet posted successfully! Tweet ID:", response.data['id'])


# media = client.media_upload("gojo.jpg")

# tweet_text_with_media = "Check out this image!"
# print("Tweet with media posted successfully!")

############


# # API credentials
# API_KEY = 'IGNYruFmXlZPnJMErlWgWKyab'
# API_SECRET_KEY = 'EKZYfwTAMcl5yW2qJlJFrA9lP4DKnyWi7zlAyrNHhkr45Fc2Gy'
# ACCESS_TOKEN = '1590435349808893952-2Tm4iwRFZMURuiMtHX29nJwKVtS4Rt'
# ACCESS_TOKEN_SECRET = 'W3d0R2a8rdN2aDdFWKBfpr9TJ08bZ1dBs0o3dN6bIsFJ2'
# BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOSlwQEAAAAA5rrXlbqC9oru5KZ9ibB28t0OhkU%3DTnllcJGgaj3e0DTkAM4sstjpGDOvQNeOxcYUR0YW8Ic7xnLoWp'

# # Authenticate for API v2
# client_v2 = tweepy.Client(bearer_token=BEARER_TOKEN)

# # Authenticate for API v1.1 (to upload media)
# auth_v1 = tweepy.OAuth1UserHandler(
#     API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api_v1 = tweepy.API(auth_v1)

# # Upload media using API v1.1
# media = api_v1.media_upload("gojo.jpg")

# # Post a tweet with media using API v2
# tweet_text_with_media = "Check out this image!"
# response = client_v2.create_tweet(
#     text=tweet_text_with_media, media_ids=[media.media_id])
# print("Tweet with media posted successfully! Tweet ID:", response.data['id'])
