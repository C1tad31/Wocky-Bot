from discord.ext import commands
import discord
from discord import Color
from datetime import datetime
from .. import utils
import sqlite3
import hashlib


class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("CEO", "Co-Owner", "•")
    async def add_db_user(self, ctx, username, password, email, id):
        await ctx.message.delete()
        hashed_password = hashlib.sha1(password.encode())
        pass_value = hashed_password.hexdigest()
        task = "INSERT INTO DB_USERS (USERNAME, PASSWORD, EMAIL, USERID) VALUES (?,?,?,?)"
        conn = sqlite3.connect("db/users.db")
        conn.execute(task, (str(username), str(pass_value), str(email), str(id)))

        conn.commit()
        await utils.embedDetails(ctx,
                                 "Database Changed!",
                                 "{} has been added to the database by: {}".format(username, ctx.author.mention),
                                 Color.gold(),
                                 ctx.guild.icon_url,
                                 datetime.utcnow(),
                                 "WockyFX - Database Changed", 0)
        conn.close()

    @commands.command()
    @commands.has_any_role("CEO", "Co-Owner", "•")
    async def delete_db_user(self, ctx, username, password, email, id):
        await ctx.message.delete()
        hashed_password = hashlib.sha1(password.encode())
        pass_value = hashed_password.hexdigest()
        task = "DELETE FROM DB_USERS WHERE USERNAME = ? AND PASSWORD = ? AND EMAIL = ? AND USERID = ?"
        conn = sqlite3.connect("db/users.db")
        conn.execute(task, (str(username), str(pass_value), str(email), str(id)))

        conn.commit()
        await utils.embedDetails(ctx,
                                 "Database Changed!",
                                 "{} has been removed from the database by: {}".format(username, ctx.author.mention),
                                 Color.gold(),
                                 ctx.guild.icon_url,
                                 datetime.utcnow(),
                                 "WockyFX - Database Changed", 0)
        conn.close()

    @commands.command()
    @commands.has_any_role("CEO", "Co-Owner", "•")
    async def edit_db_user(self, ctx, username, password, email, member: discord.Member = None):
        pass


def setup(bot):
    bot.add_cog(Users(bot))
