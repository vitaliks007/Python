import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Hello, {author.mention}!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def getmap(ctx):
    await ctx.send(file=discord.File('mireamap.png'))


bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
