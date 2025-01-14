import discord
import os
from keepalive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
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

    if message.content == ('sussy baka'):
        await message.channel.send('https://media.discordapp.net/attachments/798464697036046356/871983183678291988/unknown.png?width=713&height=419')

    if 'ayaya' in message.content:
        await message.channel.send('ayaya')

keep_alive()
client.run(os.getenv('TOKEN'))