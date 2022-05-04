import json

from discord.ext import commands

with open("config/config.json") as file:
    config = json.load(file)

TOKEN = config["token"]
PREFIX = config["prefix"]

wockyfx = commands.Bot(command_prefix=PREFIX)
wockyfx.remove_command("help")

cogs = [
    "cogs.commands",
    "cogs.modcommands",
    "cogs.events",
    "cogs.db.users",
]

for cog in cogs:
    wockyfx.load_extension(cog)
    print("loaded {}".format(cog))

wockyfx.run(TOKEN, reconnect=True)