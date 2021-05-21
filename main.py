import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import express
express.get_port()

OCs_Storage = "OCs.json"

from RuneChats import Rune
import vacefron
import random
import json
import time
import requests

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='R!', intents=intents)
vac = vacefron.Client()


@client.event
async def on_message(message):
    if message.author.bot:
        return

    await Rune.Rune(message)
    await client.process_commands(message)

# ---------------------------------------------------------


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('R!ping'))
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

    async def no_permission(response):
        if isinstance(error, MissingPermissions):
            return await message.send(embed=response)
    Require = discord.Embed(
        title='You have to follow the requirements.', color=0x87f587)
    No_Permission = discord.Embed(
        title='You don\'t have the permission to use this command.', color=0x87f587)

    await invalid_user(Require)
    await invalid_channel(Require)
    await no_permission(No_Permission)

# ---------------------------------------------------------


@client.command()
async def ping(Rune):
    Ping = discord.Embed(
        title="Pong! 🏓", description=f"Latency: `{round(client.latency * 1000)}ms`", color=0x87f587)
    await Rune.send(embed=Ping)


@client.command()
async def say(Rune, *, args = None):
    if args is None:
        Provide = discord.Embed(
            description='```R!say <Text>```', color=0x87f587)
        return await Rune.send('You have to provide something for Rune to say.', embed=Provide)

    return await Rune.send(args)


@client.command()
async def owofy(message, *, args = None):
    if args is None:
        Provide = discord.Embed(
            description='```R!owofy <Text>```', color=0x87f587)
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
        Provide = discord.Embed(
            description='```R!clap_text <Text>```', color=0x87f587)
        await message.send('You need to provide something for Rune to clap text.', embed=Provide)

    Message_To_Clap_Text = args.replace(" ", " 👏 ")
    await message.send(Message_To_Clap_Text)


@client.command()
async def eject(message, impostor: discord.User = None):
    if impostor is None:
        Provide = discord.Embed(
            description='```R!eject <User>```', color=0x87f587)
        return await message.send('You need to mention someone.', embed=Provide)

    image = await vac.ejected(impostor.name)
    image_out = discord.File(fp=await image.read(), filename="ejected.png")

    return await message.send(file=image_out)


@client.command()
async def iq(message):
    iq = random.randint(0, 400)

    IQ = discord.Embed(
        title='🧠 IQ Test:', description=f"{message.author.mention}'s IQ is **{iq}**", color=0x87f587)
    IQ.set_author(name=f'{message.author.name}',
                  icon_url=f'{message.author.avatar_url}')
    IQ.set_image(url='https://images-ext-2.discordapp.net/external/3IZX7j1iQvU8IX-znaR3eyK5OgBhdXG0UT5U-5KpwoU/https/media.giphy.com/media/l44QzsOLXxcrigdgI/giphy.gif')

    return await message.send(embed=IQ)


@client.command()
async def sparkles_text(message, *, args = None):
    if args is None:
        Provide = discord.Embed(
            description='```R!sparkles_text <Text>```', color=0x87f587)
        return await message.send('You have to provide something for Rune to sparkles text.', embed=Provide)

    Sparkles_Text = args.replace(" ", " ✨ ")
    Sparkles_Text = '✨ ' + Sparkles_Text + ' ✨'

    return await message.send(Sparkles_Text)


@client.command()
async def sparkle_text(message, *, args = None):
    if args is None:
        Provide = discord.Embed(
            description='```R!sparkle_text <Text>```', color=0x87f587)
        return await message.send('You have to provide something for Rune to sparkle text.', embed=Provide)

    Sparkle_Text = '✨ ' + args + ' ✨'
    return await message.send(Sparkle_Text)


@client.command()
async def say_in(message, channel: discord.TextChannel = None, *, args = None):
    if channel is None:
        Provide = discord.Embed(
            description='```R!say_in <Channel> <Text>```', color=0x87f587)
        return await message.send('You need to mention a channel for Rune to say in.', embed=Provide)

    if args is None:
        Provide = discord.Embed(
            description='```R!say_in <Channel> <Text>```', color=0x87f587)
        return await message.send('You have to provide something for Rune to say.', embed=Provide)

    await channel.send(args)
    return await message.send('Message sent.')


@client.command()
async def compliment(message, member: discord.Member):
    from Exports import Compliment

    if member:
        return await message.send(f'{member.mention} {Compliment.Compliment()}')

    return await message.send(f'{message.author.mention} {Compliment.Compliment()}')


@client.command()
@has_permissions(manage_messages=True)
async def say_to(message, member: discord.Member = None, *, args = None):
    if member is None:
        Provide = discord.Embed(
            description='```R!say_to <User> <Text>```', color=0x87f587)
        return await message.send('You need to mention a user.', embed=Provide)

    if args is None:
        Provide = discord.Embed(
            description='```R!say_to <User> <Text>```', color=0x87f587)
        return await message.send('You have to provide something for Rune to say.', embed=Provide)

    await member.send(args)
    return await message.send('Message sent.')

# Recontinue of Recreation of JSON as Database in Python ~ 5/7/21; May 7, 2021

def get_data(OC_ID):
    with open(OCs_Storage, "r") as OCs:
        _OC_ = json.load(OCs)
        return next((_OC for _OC in _OC_ if _OC["OC_ID"] == int(OC_ID)), None)
def delete_data(OC_ID):
    with open(OCs_Storage, "r") as OCs:
        _OC_ = json.load(OCs)
    _OC_[:] = (OC for OC in _OC_ if OC.get('OC_ID') != int(OC_ID))
    with open(OCs_Storage, "w") as OCs:
        return json.dump(_OC_, OCs, indent=4)

@client.command()
async def addOC(message, *, Name = None):
    Provide = discord.Embed(
        description='```R!add_oc <Name> [Avatar]```', color=0x87f587)

    if Name is None:
        return await message.send('You have to provide the name of your OC.', embed=Provide)
    # if len(message) == 0:
    #     return await message.send('You have to provide the avatar for your OC.', embed=Provide)

    OC = {}
    with open(OCs_Storage, "r") as _OCs:
        OCs = json.load(_OCs)
        ID = len(OCs) + 1
    OC["Author"] = f"{message.author.id}"
    OC["OC_Name"] = Name
    OC["OC_ID"] = ID
    OC["OC_Avatar"] = ""

    OCs.append(OC)
    with open(OCs_Storage, "w") as _OCs:
        json.dump(OCs, _OCs, indent=4)

    return await message.send(f"**{Name}** has been added, **{Name}'s** ID is **{ID}**.")


@client.command()
async def searchOC(message, *, ID = None):
    Provide = discord.Embed(
        description='```R!search_oc <ID>```', color=0x87f587)
    if ID is None:
        return await message.send('You have to provide the ID of the OC you want to search for.', embed=Provide)

    OC = get_data(ID)
    if OC is None:
        return await message.send('There is no OC with that was found with that ID.')
    else:
        OC_Name = OC["OC_Name"]
        OC_ID = OC["OC_ID"]
        OC_Author = OC["Author"]

        OC_ = discord.Embed(
            description=f"```An OC was found with the name {OC_Name}```", color=0x87f587)
        OC_.set_author(name=message.author.name,
                       icon_url=f"{message.author.avatar_url}")
        OC_.add_field(name='Name:', value=f"{OC_Name}", inline=True)
        OC_.add_field(name='ID:', value=f"{OC_ID}", inline=True)
        OC_.set_footer(text=f"{OC_Author}")
        return await message.send(embed=OC_)


@client.command()
async def removeOC(message, *, ID = None):
    Provide = discord.Embed(
        description='```R!remove_oc <ID>```', color=0x87f587)
    if ID is None:
        return await message.send('You have to provide the ID of the OC you want to remove.', embed=Provide)

    _OC = get_data(ID)
    if _OC is None:
        return await message.send('There is no OC with that was found with that ID.')
    else:
        OC_Name = _OC["OC_Name"]
        await message.send(f'{OC_Name} has been removed.')

        return delete_data(ID)


@client.command()
async def oc_say(message, ID = None, *, args = None):
    Provide = discord.Embed(
        description='```R!oc_say <ID> <Message>```', color=0x87f587)
    if ID is None:
        return await message.send('You have to provide the ID of the OC you want to talk as.', embed=Provide)

    OC = get_data(ID)
    if OC is None:
        return await message.send('There is no OC with that was found with that ID.')
    else:
        if args is None:
            return await message.send('You have to provide a message for your OC to say.', embed=Provide)

        OC_Name = OC["OC_Name"]
        OC_ID = OC["OC_ID"]
        OC_Author = OC["Author"]
        OC_Avatar = OC["OC_Avatar"]

        if OC_Author != f"{message.author.id}":
            return await message.send('There is no OC with that was found with that ID.')
        else:
            await message.message.delete()

            _Avatar_ = requests.get(f"{OC_Avatar}")

            _OC_ = await message.channel.create_webhook(name=OC_Name, avatar=_Avatar_.content)
            await _OC_.send(args)

            time.sleep(3)
            await _OC_.delete()


client.run('NzgxMjI0NzU4MzU1ODIwNTU1.X76iQA.r8t22ybi31GM0j3qhhR52485vO4')