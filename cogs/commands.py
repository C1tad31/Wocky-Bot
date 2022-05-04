from discord.ext import commands
import discord
from . import utils
from discord import Color
from datetime import datetime

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await utils.embedDetails(ctx,
        "WockyFX Help Menu", 
        "```====== User Commands ======\n.help: Displays this menu\n.info: Displays general info\n.server_info: Displays information on the server\n.userinfo: Displays info on a mentioned user\n.gp: Ghost Ping a mentioned role a specific amount of times LOL```", 
        Color.gold(), 
        ctx.guild.icon_url, 
        datetime.utcnow(), 
        "WockyFX - Help Menu")

    @commands.command()
    async def info(self):
        pass

    @commands.command()
    async def server_info(self, ctx):
        await utils.embedDetails(ctx,
        "Server Info for: {}".format(ctx.guild.name),
        "```Server Name: {}\nServer Owner: {}\nServer ID: {}\nServer Icon Url: {}```".format(ctx.guild.name, ctx.guild.owner.name, ctx.guild.id, ctx.guild.icon_url),
        Color.gold(), 
        ctx.guild.icon_url, 
        datetime.utcnow(),
        "WockyFX - Server Info")

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

    @commands.command()
    async def membercount(self, ctx):
        await utils.embedDetails(ctx, "Total Member Count", "Total Members: {}".format(ctx.guild.member_count), Color.gold(), ctx.guild.icon_url, datetime.utcnow(), "WockyFX - Member Count")



def setup(bot):
    bot.add_cog(Commands(bot))