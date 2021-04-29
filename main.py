import discord
import asyncio
from discord.ext import commands

from config import *

import json
import random

intents = discord.Intents.default()
intents.members = True

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
async def Pog(message):
    if (message.have.lower() == 'pog'):
        await message.add_reaction('🅿')
        await message.add_reaction('🅿')
        await message.add_reaction('🅿')

# ---------------------------------------------------------

@client.command()
async def ping(Rune):
    Ping = discord.Embed(title="Pong! 🏓", description=f"Latency: `{round(client.latency * 1000)}ms`", color=0x87f587)
    await Rune.send(embed=Ping)

@client.command()
async def say(Rune, *, args = None):
    if args is not None:
        Message_To_Say = args.replace("(", "")
        Message_To_Say = args.replace(")", "")

        await Rune.send(Message_To_Say)
    else:
        await Rune.send('You have to provide something for Rune to say.\n`R!say <Text>`')

@client.command()
async def owofy(message, *, args = None):
    if args is not None:
        th = args.replace("th", "w")
        L = th.replace("l", "w")
        R = L.replace("r", "w")
        Message_To_OwOfy = R.replace("ur", "ow")

        await message.send(Message_To_OwOfy)
    else:
        await message.send('You have to provide something for Rune to say.\n`R!owofy <Text>`')

@client.command()
async def claptext(message, *, args = None):
    if args is not None:
        Message_To_Clap_Text = args.replace(" ", " 👏 ")

        await message.send(Message_To_Clap_Text)
    else:
        await message.send('You have to provide something for Rune to say.\n`R!claptext <Text>`')

def write_json(data, filename="OCs.json"):
    with open (filename, "w") as f:
        json.dump(data, f, indent=4)
@client.command()

async def add_oc(message, *, name = None):
    if name is None:
        return await message.send('You have to provide the name of your OC.\n`R!add_oc <Name>`')
        
    if name is not None:
        Name = name
        ID = random.randint(1, 1000)

        with open ('OCs.json') as OC_Storage:
            OCs_Data = json.load(OC_Storage)
            Author = OCs_Data[f"{message.author.id}"]

            if Author is not None:
                OC = {
                    "OC_Name": Name,
                    "OC_ID": ID
                }
                
                Author.append(OC)

                write_json(OCs_Data)

                return await message.send(f"**{Name}** has been added, **{Name}'s** ID is **{ID}**")
            else:
                New_Author = OCs_Data['}']

                OC = {
                    {
                        f"{message.author.id}": [
                            {
                                "OC_Name": Name,
                                "OC_ID": random.randint(1, 1000)
                            }
                        ]
                    }
                }
                New_Author.append(OC)

                write_json(OCs_Data)

                return await message.send(f"**{Name}** has been added, **{Name}'s** ID is **{ID}**")
        write_json(OCs_Data)

client.run(TOKEN)