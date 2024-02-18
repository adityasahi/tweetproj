import tweepy

# Replace these with your Twitter API keys
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def unfollow_non_followers():
    # Get the list of people you follow
    following_ids = set(api.friends_ids())

    # Get the list of people who follow you
    followers_ids = set(api.followers_ids())

    # Find non-followers (people you follow who don't follow you back)
    non_followers = following_ids - followers_ids

    # Unfollow non-followers
    for user_id in non_followers:
        api.destroy_friendship(user_id)
        print(f"Unfollowed user with ID: {user_id}")

if __name__ == "__main__":
    try:
        unfollow_non_followers()
    except tweepy.TweepError as e:
        print(f"An error occurred: {str(e)}")
