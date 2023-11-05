import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from search import gpt_summarize, query_google

from voiceInput import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True
CociBot = commands.Bot(command_prefix="//", intents=intents)

@CociBot.event
async def on_ready():
    print(f'{CociBot.user.name} has connected to Discord!')
    channel = discord.utils.get(CociBot.get_all_channels(), name="General")
    textChannel =  discord.utils.get(CociBot.get_all_channels(), name="general")
    await channel.connect()
    await startVoiceInput(textChannel)

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

@CociBot.command()
async def listen(ctx):
    await startVoiceInput(ctx)

@CociBot.command()
async def search(ctx, q):
    textChannel =  discord.utils.get(CociBot.get_all_channels(), name="general")
    googleUrls = query_google(q)
    print(googleUrls)
    gptSummaries = [await gpt_summarize(x) for x in googleUrls]
    print(gptSummaries)
    for url, summary in zip(googleUrls, gptSummaries):
        await ctx.send(url['link'] + ' - ' + summary.choices[0].message.content)



CociBot.run(TOKEN)