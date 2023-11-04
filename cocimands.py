from discord.ext import commands

CociBot = commands.Bot(command_prefix="//")

@CociBot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.author(ctx.author)
    await ctx.send(ctx.message.id)