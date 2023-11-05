import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True
CociBot = commands.Bot(command_prefix="//", intents=intents)

@CociBot.event
async def on_ready():
    print(f'{CociBot.user.name} has connected to Discord!')
    channel = discord.utils.get(CociBot.get_all_channels(), name="General") 
    await channel.connect()

@CociBot.command()
async def info(ctx):
    await ctx.send("You're a livesaver!")

@CociBot.command(pass_context = True)
async def join(ctx):
    channel = discord.utils.get(CociBot.get_all_channels(), name="General")
    await channel.connect()

@CociBot.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()

CociBot.run(TOKEN)