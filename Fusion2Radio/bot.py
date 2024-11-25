import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import asyncio
from datetime import datetime
import pytz
from config import CHANNEL_INFO, ANNOUNCEMENT_CHANNEL_ID, WELCOME_CHANNEL_ID
from twitch_api import TwitchAPI

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
twitch_api = TwitchAPI()

# Stream status tracking
last_stream_status = False

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    check_stream_status.start()

@bot.event
async def on_member_join(member):
    """Send welcome message when new member joins"""
    if WELCOME_CHANNEL_ID:
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            embed = discord.Embed(
                title=f"Welcome to {CHANNEL_INFO['name']}!",
                description=f"Welcome {member.mention}! Thanks for joining our community!",
                color=discord.Color.purple()
            )
            embed.add_field(name="Twitch Channel", value=CHANNEL_INFO['url'], inline=False)
            await channel.send(embed=embed)

@tasks.loop(minutes=5)
async def check_stream_status():
    """Check if stream is live and send notification"""
    global last_stream_status
    
    if ANNOUNCEMENT_CHANNEL_ID:
        channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
        if channel:
            stream_info = await twitch_api.get_stream_info(CHANNEL_INFO['name'].lower())
            current_status = bool(stream_info)

            if current_status and not last_stream_status:
                embed = discord.Embed(
                    title=" We're Live!",
                    description=f"{CHANNEL_INFO['name']} is now streaming!",
                    color=discord.Color.purple()
                )
                embed.add_field(name="Title", value=stream_info['title'], inline=False)
                embed.add_field(name="Category", value=stream_info['game_name'], inline=True)
                embed.add_field(name="Viewers", value=stream_info['viewer_count'], inline=True)
                embed.add_field(name="Watch Now!", value=CHANNEL_INFO['url'], inline=False)
                
                await channel.send("@everyone", embed=embed)

            last_stream_status = current_status

@bot.command(name='twitch')
async def twitch(ctx):
    """Sends the Twitch channel link"""
    await ctx.send(f"Check out our Twitch channel: {CHANNEL_INFO['url']}")

@bot.command(name='about')
async def about(ctx):
    """Provides information about the channel"""
    user_info = await twitch_api.get_user_info(CHANNEL_INFO['name'].lower())
    follower_count = await twitch_api.get_followers(user_info['id']) if user_info else 0
    
    embed = discord.Embed(
        title=CHANNEL_INFO['name'],
        description=CHANNEL_INFO['description'],
        color=discord.Color.purple()
    )
    embed.add_field(name='Twitch Channel', value=CHANNEL_INFO['url'], inline=False)
    if follower_count:
        embed.add_field(name='Followers', value=f"{follower_count:,}", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='schedule')
async def schedule(ctx):
    """Shows stream schedule"""
    embed = discord.Embed(
        title="Stream Schedule",
        description="Here's when we go live! (All times in EST)",
        color=discord.Color.blue()
    )
    
    for day, time in CHANNEL_INFO['schedule'].items():
        embed.add_field(name=day, value=time, inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='socials')
async def socials(ctx):
    """Shows social media links"""
    embed = discord.Embed(
        title="Social Media Links",
        description="Follow us on social media!",
        color=discord.Color.green()
    )
    
    for platform, link in CHANNEL_INFO['social_media'].items():
        embed.add_field(name=platform, value=link, inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='rules')
async def rules(ctx):
    """Shows channel rules"""
    embed = discord.Embed(
        title="Channel Rules",
        description="Please follow these rules to keep our community friendly!",
        color=discord.Color.red()
    )
    
    rules_text = "\n".join(CHANNEL_INFO['rules'])
    embed.add_field(name="Rules", value=rules_text, inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='clips')
async def clips(ctx):
    """Shows recent clips"""
    user_info = await twitch_api.get_user_info(CHANNEL_INFO['name'].lower())
    if user_info:
        clips = await twitch_api.get_clips(user_info['id'])
        if clips:
            embed = discord.Embed(
                title="Recent Clips",
                description="Check out these recent highlights!",
                color=discord.Color.purple()
            )
            
            for clip in clips:
                embed.add_field(
                    name=clip['title'],
                    value=f"Views: {clip['view_count']} | [Watch Clip]({clip['url']})",
                    inline=False
                )
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("No recent clips found!")
    else:
        await ctx.send("Couldn't fetch clips at this time!")

@bot.command(name='status')
async def status(ctx):
    """Shows current stream status"""
    stream_info = await twitch_api.get_stream_info(CHANNEL_INFO['name'].lower())
    
    if stream_info:
        embed = discord.Embed(
            title=" Stream is LIVE!",
            description=stream_info['title'],
            color=discord.Color.green()
        )
        embed.add_field(name="Game", value=stream_info['game_name'], inline=True)
        embed.add_field(name="Viewers", value=stream_info['viewer_count'], inline=True)
        embed.add_field(name="Started At", value=stream_info['started_at'], inline=True)
        embed.add_field(name="Watch Now!", value=CHANNEL_INFO['url'], inline=False)
    else:
        embed = discord.Embed(
            title="Stream is Offline",
            description="Check out the schedule to see when we'll be live next!",
            color=discord.Color.red()
        )
        embed.add_field(name="Channel Link", value=CHANNEL_INFO['url'], inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='help')
async def help_command(ctx):
    """Shows available commands"""
    commands_list = [
        '`!twitch` - Get the Twitch channel link',
        '`!about` - Learn more about our channel',
        '`!schedule` - View stream schedule',
        '`!socials` - Get all social media links',
        '`!rules` - View channel rules',
        '`!clips` - See recent channel clips',
        '`!status` - Check if stream is live',
        '`!help` - Show this help message'
    ]
    embed = discord.Embed(
        title='Available Commands',
        description='\n'.join(commands_list),
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

# Run the bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        print("Please set up your DISCORD_TOKEN in the .env file")
    else:
        bot.run(token)
