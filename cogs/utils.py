from asyncio import tasks
from discord.ext import commands
import discord
import sqlite3

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

def create_table():
    conn = sqlite3.connect("db/users.db")
    if (conn):
        print("Connected to Database Successfully!")

    conn.execute('''
        CREATE TABLE USERS
        (USERNAME CHAR(50) NOT NULL,
        USERID CHAR(50) NOT NULL);''')

    conn.close()

    print("DB created!")

def create_user(username, user_id):
    task = "INSERT INTO USERS (USERNAME, USERID) VALUES (?,?)"
    conn = sqlite3.connect("db/users.db")
    conn.execute(task, (username, user_id))

    conn.commit()
    print("User added to DB!")
    conn.close()

def delete_user():
    pass

def update_user():
    pass