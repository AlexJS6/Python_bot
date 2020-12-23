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

    if msg.startswith('$PapSciSto'):
        await message.channel.send('Those are the instructions: \n- Send \'$play\' to play \n- After the countdown send: \'paper\', \'stone\' or \'scissors\' in the 5 seconds \n- And then you will lose because I\'m insane at this game! \nGood Luck!!')

    if msg.startswith('$play'):
        channel = message.channel
        non_split_author = message.author
        author = str(message.author).split('#')[0]

        for i in range(3, -1, -1):
            time.sleep(1)
            if i == 0:
                await channel.send('GOGOGO MY MAN!')
            else:
                await channel.send(i)

        def check(m):
            """
            Checks if the wait_for is correct
            """
            return m.content in possibilities and m.author == non_split_author and m.channel == channel

        response = await client.wait_for('message', timeout=5, check=check)
        bot_response = random.choice(possibilities)
        await channel.send(bot_response.upper())
        time.sleep(1)

        if bot_response == 'scissors' and response.content == 'paper':
            await channel.send('bot: {0} \n{1}: {2} \nI WON'.format(bot_response, author, response.content))
        if bot_response == 'scissors' and response.content == 'stone':
            await channel.send('bot: {0} \n{1}: {2} \nYOU WON'.format(bot_response, author, response.content))
        if bot_response == 'stone' and response.content == 'paper':
            await channel.send('bot: {0} \n{1}: {2} \nYOU WON'.format(bot_response, author, response.content))
        if bot_response == 'stone' and response.content == 'scissors':
            await channel.send('bot: {0} \n{1}: {2} \nI WON'.format(bot_response, author, response.content))
        if bot_response == 'paper' and response.content == 'scissors':
            await channel.send('bot: {0} \n{1}: {2} \nYOU WON'.format(bot_response, author, response.content))
        if bot_response == 'paper' and response.content == 'stone':
            await channel.send('bot: {0} \n{1}: {2} \nI WON'.format(bot_response, author, response.content))
        if bot_response == response.content:
            await channel.send('bot: {0} \n{1}: {2} \nDRAWWW MY MAN!'.format(bot_response, author, response.content))
        '''else:
            await channel.send('bot: {0} \n{1}: {2} \nDAAMN THERE IS A PROBLEM'.format(bot_response, author, response.content))'''


        



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