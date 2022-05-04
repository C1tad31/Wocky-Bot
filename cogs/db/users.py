from discord.ext import commands
import discord
from .. import utils
import sqlite3
import hashlib


class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("CEO", "Co-Owner", "•")
    async def add_db_user(self, ctx, username, password, email, id):
        hashed_password = hashlib.sha1(password.encode())
        pass_value = hashed_password.hexdigest()
        task = "INSERT INTO DB_USERS (USERNAME, PASSWORD, EMAIL, USERID) VALUES (?,?,?,?)"
        conn = sqlite3.connect("db/users.db")
        conn.execute(task, (str(username), str(pass_value), str(email), str(id)))

        conn.commit()
        await ctx.send("User added to DB!")
        conn.close()

    @commands.command()
    @commands.has_any_role("CEO", "Co-Owner", "•")
    async def delete_db_user(self, ctx, username, password, email, member: discord.Member = None):
        pass

    @commands.command()
    @commands.has_any_role("CEO", "Co-Owner", "•")
    async def edit_db_user(self, ctx, username, password, email, member: discord.Member = None):
        pass


def setup(bot):
    bot.add_cog(Users(bot))
