import discord
from discord.ext import commands

import random

async def Rune(message):
    async def message_content(content, response):
        if message.content.lower() == f"{content}":
            return await message.channel.send(f"{response}")
    async def message_includes(content, response):
        if f"{content}" in message.content.lower():
            return await message.channel.send(f"{response}")
    async def loop_message(content_list, response):
        if type(content_list) is not list:
            return print ('content_list has to be a list.')
        for i in content_list:
            if f"{i}" in message.content.lower():
                return await message.channel.send(f"{response}")
    
    return await message_content('hi', 'Hi.')
    return await message_content('hello', 'Hello there.')
    return await message_content('hoy', '!')
    return await message_content('sup', 'Soup :ok_hand:')
    return await message_content('ey', '<:gun:830351533744193536>')
    return await message_content('oi', '<:gun:830351533744193536>')
    return await message_includes('no u', 'Go get em hapii.')
    if 'owofy' not in message.content.lower():
        return await message_includes('owo', 'No, just no.')
    return await message_includes('qwq', 'Stop')
    return await message_includes('kill', 'And then dead <:gun:830351533744193536>')
    return await message_content('how are you', "I'm good ig, how about the other :eyes:")
    return await message_includes('science', 'Science is good and easy, change my mind.')
    return await message_includes('math', 'Ew, just no. Math = brain damage.')

    # ------------------------------------------------------------------------------
    
    Mean  = [ 'ugly', 'hideous', 'nerd', 'moron', 'stupid' ]
    return await loop_message(Mean, "Hey look a jerk <:gun:830351533744193536> <:LaughsATYOU:830350872760418335>")

    Good = [
        'good', 'attractive', 'beautiful', 'wonderful',
        'stunning', 'elegant', 'bold', 'Angelic', 'hracious',
        'spirited', 'charming', 'majestic', 'brilliant',
        'amazing', 'lovely'
    ]
    Wholesome = [
        'A wholesome moment right here :)',
        'Indeed',
        'Agreed',
        'Now kiss (unless you\'re talking about a non-living object)',
        'Now get married (unless you\'re talking about a non-living object)'
    ]
    return await loop_message(Good, random.choice(Wholesome))