import json

from discord import Intents
from discord.ext import commands
from discord_slash import SlashCommand

with open("config/config.json") as file:
    config = json.load(file)

TOKEN = config["token"]
PREFIX = config["prefix"]

wockyfx = commands.Bot(command_prefix=PREFIX, intents=Intents.default())
slash = SlashCommand(wockyfx)
wockyfx.remove_command("help")


cogs = [
    "cogs.commands",
    "cogs.modcommands",
    "cogs.events",
    "cogs.db.users",
    # "cogs.economy.economy",
]

for cog in cogs:
    wockyfx.load_extension(cog)
    print("loaded {}".format(cog))

wockyfx.run(TOKEN, reconnect=True)
