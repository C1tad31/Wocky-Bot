from discord.ext import commands
import discord

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self):
        pass

    @commands.command()
    async def info(self):
        pass

    @commands.command()
    async def server_info(self):
        pass

    @commands.command()
    async def user_info(self):
        pass



def setup(bot):
    bot.add_cog(Commands(bot))