import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.command()
async def hello(ctx):
    author = ctx.message.author

    await ctx.send(f'Hello, {author.mention}!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def getmap(ctx):
    await ctx.send(file=discord.File('mireamap.png'))


bot.run(settings['token'])
