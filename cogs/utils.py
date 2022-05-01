from discord.ext import commands
import discord

def embedDetails(ctx, title: str, desc: str, color, guild_icon, timestamp, footer):
    embed = discord.Embed(
        title=title,
        description=desc,
        colour=color,
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_color(color)
    embed.set_thumbnail(guild_icon)
    embed.timestamp = timestamp
    embed.set_footer(text=footer)
    ctx.send(embed=embed)