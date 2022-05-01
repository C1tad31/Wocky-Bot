from discord.ext import commands
import discord

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot connected as: {}#{}".format(self.bot.user.name, self.bot.user.discriminator))
        
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        if message.author.bot: 
            return

        if message.channel.id != 970437396342665266:
            await message.channel.send(":warning: UNDER DEVELOPMENT :warning:... i can only be accessed in <#970437396342665266> at this time, thank you for understanding")
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        pass

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        pass

def setup(bot):
    bot.add_cog(Events(bot))