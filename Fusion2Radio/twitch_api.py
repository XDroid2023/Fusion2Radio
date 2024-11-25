import aiohttp
import asyncio
from datetime import datetime
import config

class TwitchAPI:
    def __init__(self):
        self.client_id = config.TWITCH_CLIENT_ID
        self.client_secret = config.TWITCH_CLIENT_SECRET
        self.access_token = None
        self.headers = None

    async def get_access_token(self):
        """Get Twitch access token"""
        async with aiohttp.ClientSession() as session:
            params = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'client_credentials'
            }
            async with session.post('https://id.twitch.tv/oauth2/token', params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    self.access_token = data['access_token']
                    self.headers = {
                        'Client-ID': self.client_id,
                        'Authorization': f'Bearer {self.access_token}'
                    }
                    return True
                return False

    async def get_stream_info(self, username):
        """Get current stream information"""
        if not self.headers:
            await self.get_access_token()

        async with aiohttp.ClientSession() as session:
            params = {'user_login': username}
            async with session.get('https://api.twitch.tv/helix/streams', headers=self.headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('data', [])[0] if data.get('data') else None
                return None

    async def get_user_info(self, username):
        """Get user information"""
        if not self.headers:
            await self.get_access_token()

        async with aiohttp.ClientSession() as session:
            params = {'login': username}
            async with session.get('https://api.twitch.tv/helix/users', headers=self.headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('data', [])[0] if data.get('data') else None
                return None

    async def get_clips(self, broadcaster_id, limit=5):
        """Get recent clips"""
        if not self.headers:
            await self.get_access_token()

        async with aiohttp.ClientSession() as session:
            params = {
                'broadcaster_id': broadcaster_id,
                'first': limit
            }
            async with session.get('https://api.twitch.tv/helix/clips', headers=self.headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('data', [])
                return []

    async def get_followers(self, broadcaster_id):
        """Get follower count"""
        if not self.headers:
            await self.get_access_token()

        async with aiohttp.ClientSession() as session:
            params = {'broadcaster_id': broadcaster_id}
            async with session.get('https://api.twitch.tv/helix/users/follows', headers=self.headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('total', 0)
                return 0
