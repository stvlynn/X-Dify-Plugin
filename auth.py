from requests_oauthlib import OAuth1Session
import os
import json
import sys

consumer_key = 'replace_with_your_consumer_key'
consumer_secret = 'replace_with_your_consumer_secret'

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )
    # Exit the program since we can't continue without a valid token
    sys.exit(1)

# If we get here, we have a valid fetch_response
resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]
print("Access Token:", access_token)
print("Access Token Secret:", access_token_secret)

# Print formatted for easy copying to credentials
print("\nCopy these values to your credentials:")
print(f"API Key: {consumer_key}")
print(f"API Secret: {consumer_secret}")
print(f"Access Token: {access_token}")
print(f"Access Token Secret: {access_token_secret}")