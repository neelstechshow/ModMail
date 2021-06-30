import discord
from discord.ext import commands


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        else:
            if str(message.channel.type) == 'private':
                guild = self.bot.get_guild(830592909001621545)
                channels = await guild.fetch_channels()
                channel = discord.utils.get(channels, name=str(message.author.id))
                if channel is None:
                    embedVar = discord.Embed(title = 'A New Thread Has Been Created, Moderators Will Be In Touch!')
                    message.author.send(embed=embedVar)
                    category = discord.utils.get(guild.categories, name='Tickets')
                    channel = await guild.create_text_channel(message.author.id, category=category)
                    

                embedVar = discord.Embed(title=f'{message.author} Has Sent A New Message', description=message.content, color=0x00ff00)  # Blue: 0x0000ff, Red: 0xff0000
                await channel.send(embed=embedVar)
    

def setup(bot):
    bot.add_cog(Member(bot))
