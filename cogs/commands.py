import json
import urllib.request
from datetime import datetime

import discord
from discord_slash import cog_ext, SlashContext, SlashCommand
from discord import Color
from discord.ext import commands

from . import utils


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="Help", description="Displays the Help Command")
    async def help(self, ctx: SlashContext):
        await utils.embedDetails(ctx,
                                 "WockyFX Help Menu",
                                 "```====== User Commands ======\n.help: Displays this menu\n.info: Displays general "
                                 "info\n.server_info: Displays information on the server\n.userinfo: Displays info on "
                                 "a mentioned user\n.gp: Ghost Ping a mentioned role a specific amount of times "
                                 "LOL```",
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
                                 "```Server Name: {}\nServer Owner: {}\nServer ID: {}\nServer Icon Url: {}```".format(
                                     ctx.guild.name, ctx.guild.owner.name, ctx.guild.id, ctx.guild.icon_url),
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
        await utils.embedDetails(ctx, "Total Member Count", "Total Members: {}".format(ctx.guild.member_count),
                                 Color.gold(), ctx.guild.icon_url, datetime.utcnow(), "WockyFX - Member Count")

    @commands.command()
    async def ipgeo(self, ctx, host):
        await ctx.message.delete()
        url = 'http://ipinfo.io/{}?token=7c22b876dc7676'.format(host)
        response = urllib.request.urlopen(url)
        data = json.load(response)

        host = data['ip']
        hostname = data['hostname']
        loc = data['loc']
        postal = data['postal']
        timezone = data['timezone']
        org = data['org']
        city = data['city']
        country = data['country']

        await utils.embedDetails(ctx,
                                 "IP Info on: {}".format(host),
                                 "IP: {}\nHostname: {}\nLocation: {}\nCity: {}\nCountry: {}\nPostal Code: {}\nTimezone: {}\nOrg: {}".format(
                                     host, hostname, loc, city, country, postal, timezone, org),
                                 Color.gold(),
                                 ctx.guild.icon_url,
                                 datetime.utcnow(),
                                 "WockyFX - IP Geo", 0)


def setup(bot):
    bot.add_cog(Commands(bot))
