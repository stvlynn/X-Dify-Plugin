# X Media Tweet Plugin Privacy Policy

## Data Collection and Usage

The X Media Tweet Plugin (hereinafter referred to as "the Plugin") processes the following types of data during operation:

1. **API Authentication Credentials**: Including API key, API secret, access token, and access token secret required for authenticating with the X (Twitter) API.
2. **Tweet Content**: The text content of tweets that users intend to post.
3. **Media Files**: Images or videos that users upload to be included in tweets, which may be provided directly or via URLs.
4. **Temporary File Data**: Temporary copies of media files created during processing and uploading.
5. **API Responses**: Data returned from the X API during the media upload and tweet posting process.

This plugin does not store or record any of the above data permanently. All data is only temporarily processed in memory for executing the requested media uploads and tweet posts, and is discarded immediately after completion. Temporary files created during media processing are deleted after the operation is completed.

## Data Transmission

This plugin communicates with the X (Twitter) API securely through HTTPS. All data transmission between the plugin and X's servers is conducted through encrypted channels, ensuring data security during transmission. When downloading media from URLs, the plugin uses secure connections where available, with fallback options for environments with strict security requirements.

## Third-Party Services

This plugin does not send any data to third-party services other than X (Twitter). Communication is limited to:

1. X API servers for authenticating, uploading media, and posting tweets.
2. Any user-specified URLs for downloading media when a URL is provided.

## Data Security

To protect user data security, this plugin takes the following measures:

1. Does not store authentication credentials, tweet content, or media files beyond the duration of the specific operation.
2. Uses standard OAuth protocol for secure authentication with X API.
3. Securely handles media files in memory and temporary storage.
4. Immediately deletes temporary files after upload completion or on errors.
5. Implements multiple download methods to accommodate various network security configurations.

## User Responsibilities

Users should note the following when using this plugin:

1. Ensure they have legitimate rights to use the X API credentials provided.
2. Comply with X's Terms of Service and Developer Agreement when posting tweets.
3. Only upload media content they have rights to share or that complies with applicable copyright laws.
4. Protect their X API credentials and not share them with unauthorized parties.
5. Be aware that content posted to X becomes public and subject to X's privacy policy.

## Policy Updates

This privacy policy may be updated from time to time. Significant changes will be notified to users when the plugin is updated.

## Contact Information

If you have any questions about this privacy policy, please contact the plugin author.