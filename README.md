# YouTube Video Upload Script

This repository contains a Python script to upload videos to YouTube using the YouTube Data API v3. The script handles authentication, video metadata configuration, and uploading.

## Prerequisites

Before you can use this script, ensure you have the following:

1. **Google Developer Console Project**: Create a project and enable the YouTube Data API v3.
2. **OAuth 2.0 Credentials**: Obtain your OAuth 2.0 Client ID and Client Secret.
3. **Python Environment**: Ensure you have Python installed.

## Getting Started

### Step 1: Set Up Google Developer Console

1. **Navigate to the Developer Console**: Go to [Google Developer Console](https://console.developers.google.com/).
2. **Create a New Project**: Click on "Select Project" at the top, then "New Project". Give it a name and create it.
3. **Enable YouTube Data API v3**: Go to "API & Services Dashboard" and click on "Enable APIs and Services". Search for "YouTube Data API v3" and enable it.
4. **Set Up OAuth Consent Screen**: Go to "OAuth consent screen" on the left, select "External", and fill in the required details.
5. **Create OAuth 2.0 Credentials**: Go to "Credentials", click on "Create Credentials", and select "OAuth 2.0 Client IDs". Download the JSON file with your credentials and save it securely.

### Step 2: Install Required Libraries

Install the necessary libraries using pip:

`pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`

### Step 3: Configure and Run the Script

1. **Place the Credentials File**: Ensure the `client_secrets_file` path in the script points to your downloaded credentials JSON file.
2. **Update the Script**: Modify the script as needed for your video upload. The script includes authentication and upload functionality.

### Step 4: Run the Script

Run the script from your terminal or command line:

`python run.py`

The script will prompt you to authenticate with your Google account. Once authenticated, it will upload the specified video to your YouTube channel.

## Script Details

The script performs the following tasks:

1. **Authenticate with Google**: Uses OAuth 2.0 to authenticate with the YouTube Data API v3.
2. **Upload Video**: Uploads the video to YouTube with the specified metadata.

## Troubleshooting

If you encounter issues, ensure that:

- The credentials file is correctly placed and the path is correct.
- You have enabled the YouTube Data API v3 in your Google Developer Console.
- The necessary libraries are installed in your Python environment.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
