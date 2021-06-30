import discord
from discord.ext import commands

class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.bot))
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Over ModMail"))

def setup(bot):
    bot.add_cog(Startup(bot))
