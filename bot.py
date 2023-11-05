import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from search import gpt_summarize, query_google

from voiceInput import *

class ChannelContext:
    def __init__(self, tc, vc):
        self.tc = tc
        self.vc = vc

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
send_tts_messages = True

intents = discord.Intents.all()
intents.members = True
CociBot = commands.Bot(command_prefix="//", intents=intents)

pauser = False

@CociBot.event
async def on_ready():
    print(f'{CociBot.user.name} has connected to Discord!')
    channel = discord.utils.get(CociBot.get_all_channels(), name="General")
    textChannel =  discord.utils.get(CociBot.get_all_channels(), name="general")
    await channel.connect()
    ctx = ChannelContext(textChannel, channel)
    #await listen(ctx)

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
async def pause(flag):
    await pauseCheck(flag)

@CociBot.command()
async def search(ctx, *, q):
    googleUrls = query_google(q)
    await ctx.send(q)
    print(googleUrls)
    gptSummaries = [await gpt_summarize(x) for x in googleUrls]
    print(gptSummaries)
    for url, summary in zip(googleUrls, gptSummaries):
        await ctx.send(url['link'] + ' - ' + summary.choices[0].message.content)

@CociBot.command()
async def send(ctx, *, message):
    channel = discord.utils.get(CociBot.get_all_channels(), name="General")
    members = channel.members
    memusernames = []
    for member in members:
        memusernames.append(member)
    await ctx.send(str(memusernames[-1]) + " " + message)

@CociBot.command()
async def speak(ctx, message):
    await ctx.send(message, tts=True)

CociBot.run(TOKEN)