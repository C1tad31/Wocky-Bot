from discord.ext import commands
import discord
from datetime import datetime
from . import utils

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # def embedDetails(self, ctx, title: str, desc: str, color, guild_icon, timestamp, footer):
    #     embed = discord.Embed(
    #         title=title,
    #         description=desc,
    #         colour=color,
    #     )
    #     embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    #     embed.set_color(color)
    #     embed.set_thumbnail(guild_icon)
    #     embed.timestamp = timestamp
    #     embed.set_footer(text=footer)
    #     ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def clear(self, ctx, amount=None):
        if not amount:
            utils.embedDetails("Args Error", 
            "``Usage: .clear <amount>``",
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Args Error")
        else:
            await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermssions):
            utils.embedDetails("Permissions Error!", 
            "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Permissions Error")
        elif isinstance(error, commands.CommandOnCooldown):
            utils.embedDetails("Cooldown Error!", 
            "Cooldown remaining: ``{.2f}``".format(error.retry_after),
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Cooldown Error")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        if not member:
            await ctx.send("Please specify a valid member to kick!")
        elif not reason:
            await ctx.send("Please specify a reason to kick this member!")
        else:
            await member.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermssions):
            self.embedDetails("Permissions Error!", 
            "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Permissions Error")
        elif isinstance(error, commands.CommandOnCooldown):
            self.embedDetails("Cooldown Error!", 
            "Cooldown remaining: ``{.2f}``".format(error.retry_after),
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Cooldown Error")
            



def setup(bot):
    bot.add_cog(ModCommands(bot))