## X (formerly Twitter) Dify Plugin

**Author:** stvlynn
**Version:** 0.0.1
**Type:** tool

### Description

This plugin allows you to interact with the X (formerly Twitter) platform through their official API. It provides tools to send and delete tweets.

### Features

- **Post Tweet**: Send tweets to your X account and receive the tweet ID in response
- **Delete Tweet**: Delete tweets by their ID
- **Post Media Tweet**: Send tweets with media attachments (images or videos)

### Setup

1. Create a developer account at [X Developer Portal](https://developer.twitter.com/)
2. Create a project and app to obtain your API keys:
   - Go to the [Developer Portal Dashboard](https://developer.twitter.com/en/portal/dashboard)
   - Click "Create Project" and follow the steps
   - Within your project, create an app to get your API keys and tokens
3. Set up OAuth 1.0a with user context authentication:
   - In your app settings, configure the OAuth 1.0a settings
   - Ensure you set the correct permission level (Read and Write)
   - Generate your Access Token and Secret

4. Configure the following credentials in the plugin settings:
   - **API Key**: Your X API Key (Consumer Key)
   - **API Secret**: Your X API Secret (Consumer Secret)
   - **Access Token**: OAuth 1.0a Access Token
   - **Access Token Secret**: OAuth 1.0a Access Token Secret

### Authentication Notes

- All credentials are stored securely and used only for authenticating with the X API
- You need Read and Write permissions for your app to post and delete tweets
- To verify your credentials are working, the plugin will make a test API call to the X API

### Usage

#### Posting a Tweet

```json
{
  "text": "Your tweet content here"
}
```

Response:
```json
{
  "status": "success",
  "tweet_id": "1234567890123456789",
  "text": "Your tweet content here",
  "message": "Tweet published successfully with ID: 1234567890123456789"
}
```

#### Deleting a Tweet

```json
{
  "tweet_id": "1234567890123456789"
}
```

Response:
```json
{
  "status": "success",
  "message": "Tweet with ID 1234567890123456789 deleted successfully"
}
```

#### Posting a Media Tweet

This action allows you to upload and attach media (images or videos) to your tweets.

Parameters:
- `text`: The text content of your tweet (max 280 characters)
- `media`: The media file to attach (image or video)

Supported media formats:
- Images: JPEG, PNG, GIF
- Videos: MP4 (H.264 codec recommended)

Note: Videos may take longer to process on X platform before the tweet is published.

```json
{
  "text": "Check out this awesome media!",
  "media": [Binary file data]
}
```

Response:
```json
{
  "status": "success",
  "tweet_id": "1234567890123456789",
  "text": "Check out this awesome media!",
  "media_id": "9876543210987654321",
  "message": "Tweet with media published successfully with ID: 1234567890123456789"
}
```



