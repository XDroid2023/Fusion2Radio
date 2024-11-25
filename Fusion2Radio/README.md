# Fusion2Radio Discord Bot

A feature-rich Discord bot for the Fusion2Radio Twitch channel that helps manage the community and share information about the channel.

## Features

- 🔴 Live stream notifications
- 📅 Stream schedule display
- 🎮 Current stream status
- 📊 Channel statistics
- 🎬 Recent clips showcase
- 📱 Social media integration
- 👋 Automatic welcome messages
- 📜 Channel rules display
- 🔍 Channel information

## Commands

- `!twitch` - Get the Twitch channel link
- `!about` - Learn more about our channel
- `!schedule` - View stream schedule
- `!socials` - Get all social media links
- `!rules` - View channel rules
- `!clips` - See recent channel clips
- `!status` - Check if stream is live
- `!help` - Show all available commands

## Setup

1. First, create a Discord application and bot:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the Bot section and create a bot
   - Copy the bot token

2. Create a Twitch application:
   - Go to the [Twitch Developer Console](https://dev.twitch.tv/console)
   - Create a new application
   - Copy the Client ID and Client Secret

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following content:
```
# Discord Bot Configuration
DISCORD_TOKEN=your_discord_bot_token_here
ANNOUNCEMENT_CHANNEL_ID=your_announcement_channel_id
WELCOME_CHANNEL_ID=your_welcome_channel_id

# Twitch API Configuration
TWITCH_CLIENT_ID=your_twitch_client_id
TWITCH_CLIENT_SECRET=your_twitch_client_secret
```

5. Update the channel information in `config.py`:
   - Set your actual social media links
   - Update the stream schedule
   - Customize the rules if needed

6. Run the bot:
```bash
python bot.py
```

## Adding the Bot to Your Server

1. Go to the Discord Developer Portal
2. Select your application
3. Go to the OAuth2 section
4. In "Scopes", select "bot"
5. In "Bot Permissions", select:
   - Send Messages
   - Embed Links
   - Mention Everyone (for live notifications)
   - Read Message History
6. Copy the generated URL and open it in a browser to add the bot to your server

## Features Explanation

### Live Stream Notifications
The bot checks your Twitch channel status every 5 minutes and sends a notification to the specified announcement channel when you go live.

### Welcome Messages
New members automatically receive a welcome message with your Twitch channel link in the specified welcome channel.

### Stream Information
Users can check the current stream status, view recent clips, and get various information about the channel using different commands.

### Social Media Integration
Easy access to all your social media links through a single command.

## Customization

You can customize various aspects of the bot by modifying the `config.py` file:
- Channel information
- Social media links
- Stream schedule
- Channel rules
- Bot messages and embeds

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to add!
