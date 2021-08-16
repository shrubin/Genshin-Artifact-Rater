import discord
import asyncio
import aiohttp



from discord.ext import commands



class Guild(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		#self.webhook = Webhook.from_url("https://discord.com/api/webhooks/810985974346678282/LVg72N1WoRZenEibugJJj1RMyl9Ln0o3vL646gli1UstLDjwKNnccTCDrHfa5uM1Kc4v", adapater=AsyncWebhookAdapter(self.bot.session))

	async def updatePresence(self):
		
		await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{str(len(self.bot.guilds))} servers! | -help'))
		await asyncio.sleep(15)
		await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Travelers! | -help"))
		await asyncio.sleep(15)
		await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"rating Artifacts | -help"))
		await asyncio.sleep(15)
		await self.bot.change_presence(activity=discord.Streaming(name=f"{len(self.bot.shards)} stars! | -help", url="https://www.twitch.tv/ohchizy"))
		await asyncio.sleep(15)

	@commands.Cog.listener()
	async def on_ready(self):
		await self.updatePresence()

def setup(bot):
	bot.add_cog(Guild(bot))