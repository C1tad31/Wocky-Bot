from asyncio import tasks
from discord.ext import commands
import discord
import sqlite3


async def embedDetails(ctx, title, desc, color, guild_icon, timestamp, footer, time):
    embed = discord.Embed(
        title=title,
        description=desc,
        colour=color,
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=guild_icon)
    embed.timestamp = timestamp
    embed.set_footer(text=footer)
    if time == 0:
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=embed, delete_after=time)


async def task_embed(ctx, title, desc, color, guild_icon, timestamp, footer):
    embed = discord.Embed(
        title=title,
        description=desc,
        colour=color,
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=guild_icon)
    embed.timestamp = timestamp
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)


async def logsEmbeds(message, channel, title, desc, color, guild_icon, timestamp, footer):
    log_channel = discord.utils.get(message.guild.channels, name="{}".format(channel))
    embed = discord.Embed(
        title=title,
        description=desc,
        colour=color,
    )
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=guild_icon)
    embed.timestamp = timestamp
    embed.set_footer(text=footer)
    await log_channel.send(embed=embed)


async def member_join_leave(member, channel, title, desc, color, guild_icon, timestamp, footer):
    log_channel = discord.utils.get(member.guild.channels, name="{}".format(channel))
    embed = discord.Embed(
        title=title,
        description=desc,
        colour=color,
    )
    embed.set_author(name=member.author.name, icon_url=member.author.avatar_url)
    embed.set_thumbnail(url=guild_icon)
    embed.timestamp = timestamp
    embed.set_footer(text=footer)
    await log_channel.send(embed=embed)


# async def create_table(ctx):
#     conn = sqlite3.connect("db/users.db")
#     if conn:
#         print("Connected to Database Successfully!")
#
#     conn.execute('''
#         CREATE TABLE USERS
#         (USERNAME CHAR(50) NOT NULL,
#         PASSWORD CHAR(50) NOT NULL,
#         EMAIL CHAR(50) NOT NULL,
#         USERID CHAR(50) NOT NULL);''')
#
#     conn.close()
#
#     print("DB created!")
#     await ctx.send("DB Create Successfully!")


async def create_eco_table():
    conn = sqlite3.connect("db/eco_users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE ECO_USERS(
    USERNAME TEXT,
    BALANCE INTEGER,
    USERID INTEGER NOT NULL
    );
    """)
    conn.commit()
    conn.close()


async def create_task_user(ctx, username, user_id):
    task = "INSERT INTO USERS (USERNAME, USERID) VALUES (?,?)"
    conn = sqlite3.connect("db/task_users.db")
    conn.execute(task, (username, user_id))

    conn.commit()
    await ctx.send("User added to DB!")
    conn.close()


async def delete_user(ctx, username, user_id):
    task = "DELETE * WHERE USERNAME = ? AND USERID = ?"
    conn = sqlite3.connect("db/task_users.db")
    conn.execute(task, (username, user_id))
    conn.commit()
    await ctx.send("User deleted from DB!")
    conn.close()


async def update_user(ctx, username, user_id):
    # TODO: Edit User Sqlite Syntax
    task = ""
    conn = sqlite3.connect("db/task_users.db")
    conn.execute(task, (username, user_id))
    conn.commit()
    await ctx.send("User edited in DB!")
    conn.close()
