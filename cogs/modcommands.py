from discord.ext import commands
import discord
from datetime import datetime
from . import utils

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def clear(self, ctx, amount=None):
        if not amount:
            utils.embedDetails(ctx,
            "Args Error", 
            "``Usage: .clear <amount>``",
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Args Error")
        else:
            await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            utils.embedDetails(ctx,
            "Permissions Error!", 
            "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Permissions Error")
        elif isinstance(error, commands.CommandOnCooldown):
            utils.embedDetails(ctx,
            "Cooldown Error!", 
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
            utils.embedDetails(ctx,
            "Permissions Error!", 
            "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Permissions Error")
        elif isinstance(error, commands.CommandOnCooldown):
            utils.embedDetails(ctx, 
            "Cooldown Error!", 
            "Cooldown remaining: ``{.2f}``".format(error.retry_after),
            discord.Colour.black(),
            ctx.guild.icon_url,
            datetime.utcnow(),
            "WockyFX Bot - Cooldown Error")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx):
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Member")
        await ctx.channel.set_permissions(role, send_messages=False)
        await ctx.send("{} ***is now in lockdown.***".format(ctx.channel.mention))
        
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Member")
        await ctx.channel.set_permissions(role, send_messages=True)
        await ctx.send("{} ***has been unlocked.***".format(ctx.channel.mention))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_user(self, ctx, member: discord.Member):
        # utils.create_table()
        utils.create_user(member.name, member.id)
        await ctx.send("{}, has been added to the database!".format(member.mention))
            



def setup(bot):
    bot.add_cog(ModCommands(bot))