from discord.ext import commands
import discord
from discord import Color
from datetime import datetime
from discord.ext.commands import MissingPermissions, CommandOnCooldown
# imports utils from the parent dir for required function use
from . import utils


class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def clear(self, ctx, amount=None):
        try:
            if not amount:
                await utils.embedDetails(ctx,
                                         "Args Error",
                                         "Usage: .clear <amount>",
                                         Color.red(),
                                         ctx.guild.icon_url,
                                         datetime.utcnow(),
                                         "WockyFX - Args Error", 10)
            else:
                await ctx.channel.purge(limit=int(amount))
                await utils.embedDetails(ctx,
                                         "Messages Cleared!",
                                         "{} messages have been cleared from the chat by: {}".format(amount,
                                                                                                     ctx.author.mention),
                                         Color.gold(),
                                         ctx.guild.icon_url,
                                         datetime.utcnow(),
                                         "WockyFX - Clear Messages", 0)
        except Exception as e:
            print(e)

    # Error Handling for clearing messages
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await utils.embedDetails(ctx,
                                     "Permissions Error!",
                                     "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Permissions Error", 10)
        elif isinstance(error, CommandOnCooldown):
            await utils.embedDetails(ctx,
                                     "Cooldown Error!",
                                     "Cooldown remaining: ``{:.2f} s``".format(error.retry_after),
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Cooldown Error", 10)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        if not member:
            await ctx.send("Please specify a valid member to kick!")
        elif not reason:
            await ctx.send("Please specify a reason to kick this member!")
        else:
            await member.kick(reason=reason)

    # Error Handling for kicking users
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await utils.embedDetails(ctx,
                                     "Permissions Error!",
                                     "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Permissions Error", 10)
        elif isinstance(error, CommandOnCooldown):
            await utils.embedDetails(ctx,
                                     "Cooldown Error!",
                                     "Cooldown remaining: ``{.2f}``".format(error.retry_after),
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Cooldown Error", 10)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member = None, *, reason):
        if not member:
            pass
        elif not reason:
            pass
        else:
            await member.ban(1, reason=reason)
            # TODO: embed for alerting when a user is banned

    # Error Handling for banning users
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await utils.embedDetails(ctx,
                                     "Permissions Error!",
                                     "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Permissions Error", 10)
        elif isinstance(error, CommandOnCooldown):
            await utils.embedDetails(ctx,
                                     "Cooldown Error!",
                                     "Cooldown remaining: ``{.2f}``".format(error.retry_after),
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Cooldown Error", 10)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def mute(self, ctx, member: discord.Member = None):
        if not member:
            pass
        else:
            role = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.add_role(role)
            await utils.embedDetails(ctx, "Member Muted!",
                                     "{}, has been muted by: {}".format(member.mention, ctx.author.mention),
                                     Color.gold(), ctx.guild.icon_url, datetime.utcnow(), "WockyFX - Mute", 0)

    # Error Handling for muting  users
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await utils.embedDetails(ctx,
                                     "Permissions Error!",
                                     "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Permissions Error", 10)
        elif isinstance(error, CommandOnCooldown):
            await utils.embedDetails(ctx,
                                     "Cooldown Error!",
                                     "Cooldown remaining: ``{.2f}``".format(error.retry_after),
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Cooldown Error", 10)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def unmute(self, ctx, member: discord.Member = None):
        if not member:
            pass
        else:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.remove_role(role)

    # Error Handling for unmuting users
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await utils.embedDetails(ctx,
                                     "Permissions Error!",
                                     "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Permissions Error", 10)
        elif isinstance(error, CommandOnCooldown):
            await utils.embedDetails(ctx,
                                     "Cooldown Error!",
                                     "Cooldown remaining: ``{.2f}``".format(error.retry_after),
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Cooldown Error", 10)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def add_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
        if not role:
            pass
        elif not member:
            pass
        else:
            await member.add_roles(role)
            # embed to alert when a role is added to a user

    # Error Handling for adding roles from users
    @add_role.error
    async def add_role_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await utils.embedDetails(ctx,
                                     "Permissions Error!",
                                     "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Permissions Error", 10)
        elif isinstance(error, CommandOnCooldown):
            await utils.embedDetails(ctx,
                                     "Cooldown Error!",
                                     "Cooldown remaining: ``{.2f}``".format(error.retry_after),
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Cooldown Error", 10)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role = None):
        if not role:
            pass
        elif not member:
            pass
        else:
            await member.remove_role(role)
            # embed to alert when a role is added to a user

    # Error Handling for removing roles from users
    @remove_role.error
    async def remove_role_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await utils.embedDetails(ctx,
                                     "Permissions Error!",
                                     "Required Permissions: ``MESSAGE_MANAGE`` or ``ADMINISTRATOR``",
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Permissions Error", 10)
        elif isinstance(error, CommandOnCooldown):
            await utils.embedDetails(ctx,
                                     "Cooldown Error!",
                                     "Cooldown remaining: ``{.2f}``".format(error.retry_after),
                                     Color.gold(),
                                     ctx.guild.icon_url,
                                     datetime.utcnow(),
                                     "WockyFX Bot - Cooldown Error", 10)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member = None, *, reason):
        pass

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


def setup(bot):
    bot.add_cog(ModCommands(bot))
