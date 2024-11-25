import os
from dotenv import load_dotenv

load_dotenv()

# Discord Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
ANNOUNCEMENT_CHANNEL_ID = int(os.getenv('ANNOUNCEMENT_CHANNEL_ID', '0'))
WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID', '0'))

# Twitch Configuration
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')
TWITCH_CHANNEL = 'fusion2radio'

# Channel Information
CHANNEL_INFO = {
    'name': 'Fusion2Radio',
    'url': 'https://www.twitch.tv/fusion2radio',
    'description': 'Welcome to Fusion2Radio! Join us for amazing music, great entertainment, and an awesome community!',
    'social_media': {
        'Twitch': 'https://www.twitch.tv/fusion2radio',
        'Discord': 'https://discord.gg/YourInvite'  # Replace with your Discord invite
    },
    'schedule': {
        'Monday': '8:00 PM - 11:00 PM EST',
        'Wednesday': '8:00 PM - 11:00 PM EST',
        'Friday': '9:00 PM - 1:00 AM EST',
        'Saturday': 'Special Events (Check Discord)',
    },
    'rules': [
        "1. Be respectful to all members",
        "2. No spam or self-promotion without permission",
        "3. Keep discussions family-friendly",
        "4. No hate speech or harassment",
        "5. Follow Twitch Terms of Service",
        "6. Enjoy the music and have fun!"
    ]
}
