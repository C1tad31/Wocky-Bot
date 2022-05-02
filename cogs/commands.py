from discord.ext import commands
import discord
from . import utils

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

    @commands.command()
    @commands.has_role("Admin")
    async def gp(self, ctx, role: discord.Role, time):
        await ctx.message.delete()
        while int(time) <= 100:
            time.sleep(1)
            await ctx.send(role.mention, delete_after=1)



def setup(bot):
    bot.add_cog(Commands(bot))