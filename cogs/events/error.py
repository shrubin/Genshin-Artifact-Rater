import discord
import traceback
from discord.ext import commands

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    async def send_embed(self, ctx, title, description):
        embed = discord.Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @commands.command(name='stats')
    async def stats(self, ctx):
        info = discord.Embed(color=discord.Colour.from_rgb(133, 149, 255), title=f"Artifact Rater Shards")
        
        info.add_field(name="Stats", value=f"Total Guilds: {len(self.bot.guilds):,d} \nTotal Shards: {len(self.bot.shards):,d}", inline=True)
        info.add_field(name="\u200b", value=f"\u200b", inline=True)
        info.set_footer(text=f"Your Guild is currently on Shard #{ctx.guild.shard_id+1}")
        inf = {}
        for shards in range(self.bot.shard_count):
            val = ""
            val += f"Users: `{sum(guild.member_count for guild in self.bot.guilds if guild.shard_id == shards):,d}`|"
            val += f"Guilds: `{sum(1 for guild in self.bot.guilds if guild.shard_id == shards):,d}`|"
            val += f"Latency: `{round(self.bot.latencies[shards][1]*1000)}ms` \n"
            lat = round(self.bot.latencies[shards][1]*1000)
            if lat > 150 or lat > 100:
                emoji = "❤️"
            if lat > 100 or lat > 50:
                emoji = "🧡"
            if lat < 50 or lat == 50:
                emoji = "💚"
            info.add_field(name=f"Shard ID #{shards+1} {emoji}", value=val, inline=False)

        await ctx.send(content=f"**Artifact Rater** is currently running on `{self.bot.shard_count}` Shards", embed=info)
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exc):
        
        if isinstance(exc, commands.CommandNotFound):
            return

        if "10008" in str(exc): #Unknown Message
            return

        # If DMs are disabled return False
        if "discord.errors.Forbidden: 403 Forbidden (error code: 50007): Cannot send messages to this user" in str(exc):
            return


        
def setup(bot):
    bot.add_cog(Error(bot))