import discord
from discord.ext import commands

async def Rune(message):
    async def message_content(content, response):
        if message.content.lower() == f"{content}":
            return await message.channel.send(f"{response}")
    async def message_includes(content, response):
        if f"{content}" in message.content.lower():
            return await message.channel.send(f"{response}")
    async def loop_message(content_list, response):
        if type (content_list) is not list:
            return print ('content_list has to be a list.')
        for i in content_list:
            if f"{i}" in message.content.lower():
                return await message.channel.send(f"{response}")
    
    await message_content('hi', 'Hi.')
    await message_content('hello', 'Hello there.')
    await message_content('hoy', '!')
    await message_content('sup', 'Soup :ok_hand:')
    await message_content('ey', '<:gun:830351533744193536>')
    await message_content('oi', '<:gun:830351533744193536>')
    await message_includes('no u', 'Go get em hapii.')
    if 'owofy' not in message.content.lower():
        await message_includes('owo', 'No, just no.')
    await message_includes('qwq', 'Stop')
    await message_includes('kill', 'And then dead <:gun:830351533744193536>')
    await message_content('how are you', "I'm good ig, how about the other :eyes:")
    await message_includes('science', 'Science is good and easy, change my mind.')
    await message_includes('math', 'Ew, just no. Math = brain damage.')

    # ------------------------------------------------------------------------------
    
    Mean  = [ 'ugly', 'hideous', 'nerd', 'moron', 'stupid' ]
    await loop_message(Mean, "Hey look a jerk <:gun:830351533744193536> <:LaughsATYOU:830350872760418335>")