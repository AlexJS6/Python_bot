import discord
import os
import random

client = discord.Client() # Connection to discord

possibilities = ['stone', 'paper', 'scissors']

@client.event
async def on_ready():
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if msg.startswith('$play'):
        response = get_response() # We need to use Thread and put an integer into argument, if int = 0 send rand.choice
        await message.channel.send(response)

