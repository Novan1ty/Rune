import discord
from discord.ext import commands

import express
express.get_port()

import random
import vacefron

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='R!', intents=intents)
vac = vacefron.Client()

from RuneChats import Rune

@client.event
async def on_message(message):
    if message.author.bot: return

    await Rune.Rune(message)
    await client.process_commands(message)

# ---------------------------------------------------------

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

@client.event
async def on_command_error(message, error):
    async def invalid_user(response):
        if isinstance(error, commands.UserNotFound):
            return await message.send(embed=response)
    async def invalid_channel(response):
        if isinstance(error, commands.ChannelNotFound):
            return await message.send(embed=response)

    Require = discord.Embed(title='You have to follow the requirements.', color=0x87f587)

    await invalid_user(Require)
    await invalid_channel(Require)

# ---------------------------------------------------------

@client.command()
async def ping(Rune):
    Ping = discord.Embed(title="Pong! 🏓", description=f"Latency: `{round(client.latency * 1000)}ms`", color=0x87f587)
    await Rune.send(embed=Ping)

@client.command()
async def say(Rune, *, args = None):
    if args is None:
        Provide = discord.Embed(description='```R!say <Text>```', color=0x87f587)
        return await Rune.send('You have to provide something for Rune to say.', embed=Provide)

    return await Rune.send(args)

@client.command()
async def owofy(message, *, args = None):
    if args is None:
        Provide = discord.Embed(description='```R!owofy <Text>```', color=0x87f587)
        return await message.send('You have to provide something for Rune to say.', embed=Provide)

    l = args.replace("l", "w")
    L = l.replace("L", "W")
    r = L.replace("r", "w")
    R = r.replace("R", "W")
    ur = R.replace("ur", "ow")
    UR = ur.replace("UR", "OW")
    ove = UR.replace("ove", "uv")
    Message_To_OwOfy = ove.replace("OVE", "UV")

    return await message.send(Message_To_OwOfy)

@client.command()
async def clap_text(message, *, args = None):
    if args is None:
        Provide = discord.Embed(description='```R!clap_text <Text>```', color=0x87f587)
        await message.send('You need to provide something for Rune to clap text.', embed=Provide)
    
    Message_To_Clap_Text = args.replace(" ", " 👏 ")
    await message.send(Message_To_Clap_Text)

@client.command()
async def eject(message, impostor: discord.User = None):
    if impostor is None:
        Provide = discord.Embed(description='```R!eject <User>```', color=0x87f587)
        return await message.send('You need to mention someone.', embed=Provide) 

    image = await vac.ejected(impostor.name)
    image_out = discord.File(fp = await image.read(), filename = "ejected.png")

    return await message.send(file = image_out)

@client.command()
async def iq(message):
    iq = random.randint(0, 400)

    IQ = discord.Embed(title='🧠 IQ Test:', description=f"{message.author.mention}'s IQ is **{iq}**", color=0x87f587)
    IQ.set_author(name=f'{message.author.name}', icon_url=f'{message.author.avatar_url}')
    IQ.set_image(url='https://images-ext-2.discordapp.net/external/3IZX7j1iQvU8IX-znaR3eyK5OgBhdXG0UT5U-5KpwoU/https/media.giphy.com/media/l44QzsOLXxcrigdgI/giphy.gif')

    return await message.send(embed=IQ)

@client.command()
async def sparkles_text(message, *, args = None):
    if args is None:
        Provide = discord.Embed(description='```R!sparkles_text <Text>```', color=0x87f587)
        return await message.send('You have to provide something for Rune to sparkles text.', embed=Provide) 

    Sparkles_Text = args.replace(" ", " ✨ ")
    Sparkles_Text = '✨ ' + Sparkles_Text + ' ✨' 

    return await message.send(Sparkles_Text)

@client.command()
async def sparkle_text(message, *, args = None):
    if args is None:
        Provide = discord.Embed(description='```R!sparkle_text <Text>```', color=0x87f587)
        return await message.send('You have to provide something for Rune to sparkle text.', embed=Provide)
    
    Sparkle_Text = '✨ ' + args + ' ✨' 
    return await message.send(Sparkle_Text)

@client.command()
async def say_in(message, channel: discord.TextChannel = None, *, args = None):
    if channel is None:
        Provide = discord.Embed(description='```R!say_in <Text> <Channel>```', color=0x87f587)
        return await message.send('You need to mention a channel for Rune to say in.', embed=Provide)

    if args is None:
        Provide = discord.Embed(description='```R!say_in <Text> <Channel>```', color=0x87f587)
        return await message.send('You have to provide something for Rune to say.', embed=Provide)

    return await channel.send(args)

client.run('NzgxMjI0NzU4MzU1ODIwNTU1.X76iQA.JNDq3Ok_HGPiSnL--6iqsxm61LU')
