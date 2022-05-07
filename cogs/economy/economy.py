# import sqlite3
#
# from discord.ext import commands
# import discord
# from .. import utils
#
#
# class Economy(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     @commands.command()
#     async def create_db(self, ctx):
#         await utils.create_eco_table()
#         await ctx.send("Economy Table Created!")
#
#     @commands.command()
#     async def bal(self, ctx):
#         start_bal = 100
#         conn = sqlite3.connect("db/eco_users.db")
#         cursor = conn.cursor()
#
#         USER_ID = ctx.message.author.id
#         USER_NAME = str(ctx.message.author)
#
#         cursor.execute("SELECT USERID FROM ECO_USERS WHERE USERID=(USERID)")
#         result_user_id = cursor.fetchone()
#         if result_user_id is None:
#             cursor.execute("INSERT INTO ECO_USERS(USERNAME, BALANCE, USERID) VALUES (?,?,?)",
#                            (USER_NAME, start_bal, USER_ID))
#             conn.commit()
#             await ctx.send(
#                 "``{}`` has been added to the DB with a starting balance of ``{}`` wocky bucks".format(USER_NAME, start_bal))
#             conn.close()
#         else:
#             cursor.execute("SELECT BALANCE FROM ECO_USERS WHERE USERID=({})".format(USER_ID))
#             result_user_bal = cursor.fetchone()
#             await ctx.send("``{}'s`` Balance is: ``{}`` wocky bucks".format(USER_NAME, str(result_user_bal).strip("(),")))
#
#     @commands.command()
#     @commands.has_any_role("CEO", "Co-Owner", "•")
#     async def give(self, ctx, member: discord.Member = None, amount=None):
#         start_bal = 100
#         conn = sqlite3.connect("db/eco_users.db")
#         cursor = conn.cursor()
#
#         USER_ID = member.id
#         USER_NAME = str(member.name)
#
#         cursor.execute("SELECT USERID FROM ECO_USERS WHERE USERID=(USERID)")
#         result_user_id = cursor.fetchone()
#         if result_user_id is None:
#             cursor.execute("INSERT INTO ECO_USERS(USERNAME, BALANCE, USERID) VALUES (?,?,?)",
#                            (USER_NAME, start_bal, USER_ID))
#             conn.commit()
#             await ctx.send(
#                 "``{}`` has been added to the DB with a starting balance of ``{}`` wocky bucks".format(USER_NAME, start_bal))
#             conn.close()
#         else:
#             new_bal = amount
#             cursor.execute("UPDATE ECO_USERS SET BALANCE = BALANCE + ? WHERE USERID=?", (new_bal, USER_ID))
#             conn.commit()
#             conn.close()
#             await ctx.send("``{}`` wocky bucks have been added ``{}'s`` balance".format(str(new_bal).strip("(),"), USER_NAME))
#
#
#
#
# def setup(bot):
#     bot.add_cog(Economy(bot))
