# CANCELLED - 5/1/21; May 1, 2021

import discord
from discord.ext import commands

import json
import random

intents = discord.Intents.default()
intents.members = True

filename = "OCs.json"

client = commands.Bot(command_prefix = 'R!', intents = intents)
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('R!ping - rune-discord.web.app'))
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

@client.command() # Achieved at 7:14 pm on 4/30/21
async def add_oc(message, name = None):
    if name is None:
        return await message.send('You have to provide the name of your OC.\n`R!add_oc <Name>`')
    
    Name = name
    async def add_oc_data():
        data = {}
        with open ("OCs.json", "r") as f:
            _data = json.load(f)
            ID = len(_data) + 1

        data["Author"] = f"{message.author.id}"
        data["OC_Name"] = Name
        data["OC_ID"] = f"{ID}"
        _data.append(data)
        with open ("OCs.json", "w") as f:
            json.dump(_data, f, indent=4)
        await message.send(f"**{Name}** has been added, **{Name}'s** ID is **{ID}**")
    return await add_oc_data()

@client.command()
async def remove_oc(message, ID = None):
    if ID is None:
        return await message.send('You have to provide an name of your OC.\n`R!remove_oc <ID>`')

    def delete_data():
        new_data = []
        with open (filename, "r") as f:
            _data = json.load(f)
        with open (filename, "w") as f:
            json.dump(new_data, f, indent=4)
    delete_data()

client.run('TOKEN')
