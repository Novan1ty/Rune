import discord
from discord.ext import commands

import random

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = 'R!', intents = intents)
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('R!ping'))
    print('Rune is now online in his discord account.')

@client.event
async def on_member_join(Member):
    channel = client.get_channel('786716364248842301')
    await channel.send('Welcome')

@client.event
async def on_member_remove(Member):
    channel = client.get_channel('786716364248842301')
    await channel.send('Bye')

@client.event
async def pog(message):
    if message.content.lower() == 'pog':
        await message.add_reaction('🇵')
        await message.add_reaction('🇴')
        await message.add_reaction('🇬')

@client.event
async def poggers(message):
    if message.content.lower() == 'poggers':
        await message.add_reaction('🇵')
        await message.add_reaction('🇴')
        await message.add_reaction('🇬')
        await message.add_reaction('☪️')
        await message.add_reaction('🇪')
        await message.add_reaction('🇷')
        await message.add_reaction('🇸')

# ---------------------------------------------------------

@client.command()
async def ping(Rune):
    Ping = discord.Embed(title="Pong! 🏓", description=f"Latency: `{round(client.latency * 1000)}ms`", color=0x87f587)
    await Rune.send(embed=Ping)

@client.command()
async def say(Rune, args = None):
    if args is not None:

        await Rune.send(args)
    else:
        await Rune.send('You have to provide something for Rune to say.\n`R!say <Text>`')

@client.command()
async def owofy(message, args = None):
    if args is not None:
        th = args.replace("th", "w")
        L = th.replace("l", "w")
        R = L.replace("r", "w")
        Message_To_OwOfy = R.replace("ur", "ow")

        await message.send(Message_To_OwOfy)
    else:
        await message.send('You have to provide something for Rune to say.\n`R!owofy <Text>`')

@client.command()
async def claptext(message, args = None):
    if args is not None:
        Message_To_Clap_Text = args.replace(" ", " 👏 ")

        await message.send(Message_To_Clap_Text)
    else:
        await message.send('You have to provide something for Rune to say.\n`R!claptext <Text>`')

client.run('NzgxMjI0NzU4MzU1ODIwNTU1.X76iQA.JNDq3Ok_HGPiSnL--6iqsxm61LU')
