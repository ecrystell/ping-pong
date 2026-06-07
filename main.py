import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('ping' or 'Ping'):
        if message.content.startswith('ping pong'):
            await message.channel.send('pong ping' + message.content[9:])
        else:
            await message.channel.send('pong' + message.content[4:])
    
    if message.content.startswith('pong' or 'Pong'):
        await message.channel.send('ping' + message.content[4:])

    if message.content.startswith('bing' or 'Bing'):
        await message.channel.send('bong' + message.content[4:])

    if message.content.startswith('bonk' or 'Bonk'):
        await message.channel.send('bonk' + message.content[4:])

    if message.content.startswith('%invite'):
        await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=869447771973890058&permissions=0&scope=bot')

    if 'ayaya' in message.content:
        await message.channel.send('ayaya')

bot.run(os.getenv('TOKEN'))