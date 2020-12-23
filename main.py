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
        channel = message.channel
        author = message.author

        def random_choice():


        def check(m):
            """
            Checks if the wait_for is correct
            """
            return m.content in possibilities and m.author == author and m.channel == channel

        response = await client.wait_for('message', check=check)

        await channel.send('Your response: {}'.format(response.content))

        '''curr_time = time.time()
        await message.channel.send(curr_time)
        # if $play -> 1 at a time
        time.sleep(3)
        await message.channel.send('GO')

        if message.content.startswith('$time'):
            if (time.time() > curr_time +2) and (time.time() < curr_time +4):
                await message.channel.send('YEE')'''


        '''beginning_time = time.time()
        for i in range(5, -1, -1):
            time.sleep(1)
            if i == 0:
                await message.channel.send('@{0.author} Go'.format(message))
            else:
                await message.channel.send(i)'''
        #await message.channel.send('')
        #await message.channel.send(response)

client.run(os.getenv('TOKEN'))