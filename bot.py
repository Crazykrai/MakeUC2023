import os

import discord
from dotenv import load_dotenv

from cocimands import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@CociBot.event
async def on_ready():
    print(f'{CociBot.user.name} has connected to Discord!')

CociBot.run(TOKEN)