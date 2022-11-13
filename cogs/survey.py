from datetime import datetime
import os
import interactions
import json
import aiohttp
import time
import nextcord
from  nextcord.ext  import commands
bot  =  commands.Bot()
intents  =  nextcord.Intents.default()
intents.members  =  True
intents.message_content  =  True
bot  =  commands.Bot(command_prefix=".",  intents=intents)
bot.remove_command('help')

class Order(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

#-----Run-----
def setup(bot):
	bot.add_cog(Order(bot))