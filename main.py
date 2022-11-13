import json
import os
import time
from datetime import datetime

import aiohttp
import nextcord
from nextcord.ext import commands

bot  =  commands.Bot()
intents  =  nextcord.Intents.default()
intents.members  =  True
intents.message_content  =  True
bot  =  commands.Bot(command_prefix=".",  intents=intents)
bot.remove_command('help')
bot.load_extension('whatnot')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ.get("TOKEN", 'MTAzODA4MjAxNTQ5MDIxNTk2Nw.GzyfvP.CEMQwx95UgezBGiP_XHOu_xQV053Gze74PuFNg'))