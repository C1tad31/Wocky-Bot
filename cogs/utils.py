from asyncio import tasks
from discord.ext import commands
import discord
import sqlite3

async def embedDetails(ctx, title, desc, color, guild_icon, timestamp, footer):
    embed = discord.Embed(
        title=title,
        description=desc,
        colour=color,
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=guild_icon)
    embed.timestamp = timestamp
    embed.set_footer(text=footer)
    await ctx.send(embed=embed, delete_after=20)

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

def delete_user(username, user_id):
    task = "DELETE * WHERE USERNAME = ? AND USERID = ?"
    conn = sqlite3.connect("db/users.db")
    conn.execute(task, (username, user_id))
    conn.commit()
    print("User deleted from DB!")
    conn.close()

def update_user(username, user_id):
    # TODO: Edit User Sqlite Syntax
    task = "" 
    conn = sqlite3.connect("db/users.db")
    conn.execute(task, (username, user_id))
    conn.commit()
    print("User edited in DB!")
    conn.close()