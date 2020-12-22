import discord
import os
import random
import time 

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
        for i in range(5, -1, -1):
            if i == 0:
                await message.channel.send('Go')
            else:
                await message.channel.send(i)
        #await message.channel.send('')
        #await message.channel.send(response)

