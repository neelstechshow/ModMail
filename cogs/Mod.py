import discord
from discord.ext import commands


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = self.bot.get_guild(830592909001621545)
        if message.content == '?closeTicket' or message.content == '?close':
            pass
        else:
            if str(message.channel.type) == 'private':
                return
            else:
                if message.author == self.bot.user:
                    return
                
                else:
                    user = await guild.fetch_member(int(message.channel.name))
                    embedVar = discord.Embed(title='The Moderators Have Sent You A New Message' , description=message.content, color=0x00ff00) # Blue: 0x0000ff, Red: 0xff0000
                    await user.send(embed=embedVar)
                
        await self.bot.process_commands(message)


    @commands.command(aliases = ['close'], description='Close A Ticket Using This Command')
    @commands.has_permissions(manage_messages=True)
    async def closeTicket(self, ctx):
        try:
            member = await ctx.guild.fetch_member(int(ctx.channel.name))
            embedVar = discord.Embed(title='The Moderators Have Closed This Thread' , description='') # Blue: 0x0000ff, Red: 0xff0000
            await member.send(embed=embedVar)
            await ctx.channel.delete()
        except:
            pass


def setup(bot):
    bot.add_cog(Mod(bot))
