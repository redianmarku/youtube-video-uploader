import os
import telebot
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http
from google.oauth2.credentials import Credentials

# Telegram bot token
API_TOKEN = '7461482650:AAF0dme5l8NQX4W0wHXk172o29JqBnTVE0I'

# YouTube API scopes and token file
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
TOKEN_FILE = 'token.json'

# Use the client file you uploaded
CLIENT_SECRETS_FILE = "client.json"

# Create a TeleBot instance
bot = telebot.TeleBot(API_TOKEN)

def authenticate_youtube():
    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, SCOPES)
        
        # Set the redirect URI to your VPS domain
        flow.redirect_uri = "http://freegiftgamed.in/oauth2callback"
        
        auth_url, _ = flow.authorization_url(prompt='consent')
        
        print(f"Please go to this URL and authorize the application: {auth_url}")
        
        # This assumes you're able to handle the callback on your server
        code = input("Enter the authorization code: ")
        flow.fetch_token(code=code)
        
        credentials = flow.credentials

        with open(TOKEN_FILE, 'w') as token:
            token.write(credentials.to_json())

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials)

    return youtube

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use /link to authorize the bot with your YouTube account.")

@bot.message_handler(commands=['link'])
def send_auth_link(message):
    if os.path.exists(TOKEN_FILE):
        bot.reply_to(message, "You have already authorized the bot. You can now upload videos by sending them here.")
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, SCOPES)
        flow.redirect_uri = "http://freegiftgamed.in/oauth2callback"
        auth_url, _ = flow.authorization_url(prompt='consent')
        
        bot.reply_to(message, f"Authorize this application by visiting this link: {auth_url}")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    if not os.path.exists(TOKEN_FILE):
        bot.reply_to(message, "Please authorize the bot first using /link.")
        return

    youtube = authenticate_youtube()

    # Download the video
    video_file_info = bot.get_file(message.video.file_id)
    video_file_path = bot.download_file(video_file_info.file_path)
    video_file_name = "uploaded_video.mp4"

    with open(video_file_name, 'wb') as video_file:
        video_file.write(video_file_path)

    # Upload the video as a YouTube Short
    request_body = {
        "snippet": {
            "categoryId": "22",
            "title": "Uploaded as a YouTube Short",
            "description": "This is a YouTube Short uploaded via Python",
            "tags": ["shorts", "python", "api"],
            "shorts": True  # Indicates that this is a YouTube Short
        },
        "status": {
            "privacyStatus": "public"  # Set the video to public
        }
    }

    media_file = googleapiclient.http.MediaFileUpload(video_file_name, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    )

    response = None

    while response is None:
        status, response = request.next_chunk()
        if status:
            bot.reply_to(message, f"Upload {int(status.progress() * 100)}% complete")

    bot.reply_to(message, f"Video uploaded successfully as a YouTube Short with ID: {response['id']}")

if __name__ == "__main__":
    bot.polling()
