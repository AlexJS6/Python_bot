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
        non_split_author = message.author
        author = str(message.author).split('#')[0]


        def check(m):
            """
            Checks if the wait_for is correct
            """
            return m.content in possibilities and m.author == non_split_author and m.channel == channel

        response = await client.wait_for('message', check=check)
        bot_response = random.choice(possibilities)
        # put draw at the end
        if bot_response == 'scissors' and response.content == 'paper':
            await channel.send('bot:{0}, {1}:{2}, I WON'.format(bot_response, author, response.content))
        if bot_response == 'scissors' and response.content == 'stone':
            await channel.send('bot:{0}, {1}:{2}, YOU WON'.format(bot_response, author, response.content))
        if bot_response == 'stone' and response.content == 'paper':
            await channel.send('bot:{0}, {1}:{2}, YOU WON'.format(bot_response, author, response.content))
        if bot_response == 'stone' and response.content == 'scissors':
            await channel.send('bot:{0}, {1}:{2}, I WON'.format(bot_response, author, response.content))
        if bot_response == 'paper' and response.content == 'scissors':
            await channel.send('bot:{0}, {1}:{2}, YOU WON'.format(bot_response, author, response.content))
        if bot_response == 'paper' and response.content == 'stone':
            await channel.send('bot:{0}, {1}:{2}, I WON'.format(bot_response, author, response.content))
        if bot_response == response.content:
            await channel.send('bot:{0}, {1}:{2}, DRAWWW MY!'.format(bot_response, author, response.content))
        '''else:
            await channel.send('bot:{0}, {1}:{2}, DAAMN THERE IS A PROBLEM'.format(bot_response, author, response.content))'''
        
        #await channel.send('Bot response: {}'.format(bot_response)) # response.content

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