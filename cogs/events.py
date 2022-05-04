from datetime import datetime

from discord import Color
from discord.ext import commands

from . import utils


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot connected as: {}#{}".format(self.bot.user.name, self.bot.user.discriminator))

    @commands.Cog.listener()
    async def on_message(self, message):

        with open("config/blacklist/words.txt") as bad_words:
            profain_words = bad_words.readline()
            if message.clean_content in profain_words:
                await message.delete()
                await message.channel.send("That word is not allowed here!", delete_after=1)

        if message.author == self.bot.user and message.author.bot: return

        if message.author.id == 954454712273490002:
            await message.delete()

        await utils.logsEmbeds(message,
                               "logs",
                               "Message Sent by: {}".format(message.author.name),
                               "Message Content: ``{}``".format(message.clean_content),
                               Color.gold(),
                               message.guild.icon_url,
                               datetime.utcnow(),
                               "WockyFX - Message Logs")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        await utils.logsEmbeds(message,
                               "logs",
                               "Message Deleted by: {}".format(message.author.name),
                               "Deleted Message Content: ``{}``".format(message.clean_content),
                               Color.gold(),
                               message.guild.icon_url,
                               datetime.utcnow(),
                               "WockyFX - Deleted Message Logs")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        await utils.logsEmbeds(before,
                               "logs",
                               "Message Edited by: {}".format(before.author.name),
                               "Message Content Before: ``{}``\n\nMessage Content After: {}".format(
                                   before.clean_content, after.clean_content),
                               Color.gold(),
                               before.guild.icon_url,
                               datetime.utcnow(),
                               "WockyFX - Message Edit Logs")

    @commands.Cog.listener()
    async def on_role_create(self, role):
        pass

    @commands.Cog.listener()
    async def on_role_delete(self, role):
        pass

    @commands.Cog.listener()
    async def on_role_update(self, role):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await utils.member_join_leave(member, "welcome", "New Member!",
                                      "{} has joined the server!\n\nMember Count: {}".format(member.mention,
                                                                                             member.guild.member_count),
                                      Color.gold(), member.guild.icon_url, datetime.utcnow(), "WockyFX - Member Join")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await utils.member_join_leave(member, "welcome", "Member Left",
                                      "{} sorry to see you go\n\nMember Count: {}".format(member.mention,
                                                                                          member.guild.member_count),
                                      Color.gold(), member.guild.icon_url, datetime.utcnow(), "WockyFX - Member Leave")


def setup(bot):
    bot.add_cog(Events(bot))
