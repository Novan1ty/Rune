import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import express
express.get_port()

OCs_Storage = "./Storages/OCs.json"
Annoys_Storage = "./Storages/Annoys.json"
Warnings_Storage = "./Storages/Warnings.json"

from RuneChats import Rune
import vacefron
import random
import json
import time
import requests
from Exports import Communication

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='R!', intents=intents, help_command=None)
vac = vacefron.Client()

def get_author_id(Storage, Author_ID):
    with open(Storage, "r") as Data:
        _Data_ = json.load(Data)
        return next((_Data for _Data in _Data_ if _Data[f"Member_ID"] == int(Author_ID)), None)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    await Rune.Rune(message)
    await client.process_commands(message)

    Annoy = get_author_id(Annoys_Storage, message.author.id)
    if Annoy and (Annoy["Guild_ID"] == message.guild.id):
        await message.channel.send(Annoy["Message"])

# ---------------------------------------------------------

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('R!ping - Chilling'))

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
    Require = discord.Embed(description='```You have to follow the requirements.```', color=0x87f587)
    No_Permission = discord.Embed(description='```You don\'t have the permission(s) to use this command.```', color=0x87f587)

    await invalid_user(Require)
    await invalid_channel(Require)
    await no_permission(No_Permission)

# ---------------------------------------------------------

@client.command()
async def ping(Rune):
    Ping = discord.Embed(title="Pong! 🏓", description=f"Latency: `{round(client.latency * 1000)}ms`", color=0x87f587)
    return await Rune.send(embed=Ping)


@client.command()
async def say(Rune, *, args = None):
    Provide_Message = discord.Embed(title='You have to provide a message for Rune to say.', description='```R!add_oc <Name> [Avatar]```', color=0x87f587)
    Provide_Message.set_author(name=Rune.author.name, icon_url=Rune.author.avatar_url)

    if args is None:
        return await Rune.send(embed=Provide_Message)

    return await Rune.send(args)


@client.command()
async def owofy(message, *, args = None):
    Provide_Message = discord.Embed(title='You have to provide a message for Rune to owofy.', description='```R!owofy <Text>```', color=0x87f587)
    Provide_Message.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if args is None:
        return await message.send(embed=Provide_Message)

    l = args.replace("l", "w")
    L = l.replace("L", "W")
    r = L.replace("r", "w")
    R = r.replace("R", "W")
    ur = R.replace("ur", "ow")
    UR = ur.replace("UR", "OW")
    ove = UR.replace("ove", "uv")
    Message_To_OwOfy = ove.replace("OVE", "UV")

    return await message.send(Message_To_OwOfy)


@client.command(name="clap-text")
async def clap_text(message, *, args = None):
    Provide_Message = discord.Embed(title='You have to provide a message for Rune to clap text.', description='```R!clap_text <Text>```', color=0x87f587)
    Provide_Message.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if args is None:
        await message.send(embed=Provide_Message)

    Message_To_Clap_Text = args.replace(" ", " 👏 ")
    return await message.send(Message_To_Clap_Text)


@client.command()
async def eject(message, impostor: discord.User = None):
    Mention = discord.Embed(title='You have to mention a user.', description='```R!eject <User>```', color=0x87f587)
    Mention.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if impostor is None:
        return await message.send(embed=Mention)

    Image_Template = await vac.ejected(impostor.name)
    Eject = discord.File(fp=await Image_Template.read(), filename="ejected.png")

    return await message.send(file=Eject)


@client.command()
async def iq(message):
    iq = random.randint(0, 400)

    IQ = discord.Embed(title='🧠 IQ Test:', description=f"{message.author.mention}'s IQ is **{iq}**", color=0x87f587)
    IQ.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    IQ.set_image(url='https://images-ext-2.discordapp.net/external/3IZX7j1iQvU8IX-znaR3eyK5OgBhdXG0UT5U-5KpwoU/https/media.giphy.com/media/l44QzsOLXxcrigdgI/giphy.gif')

    return await message.send(embed=IQ)


@client.command(name="sparkles-text")
async def sparkles_text(message, *, args = None):
    Provide_Message = discord.Embed(title='You have to provide a message for Rune to sparkles text.', description='```R!sparkles_text <Text>```', color=0x87f587)
    Provide_Message.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if args is None:
        return await message.send(embed=Provide_Message)

    Sparkles_Text = args.replace(" ", " ✨ ")
    Sparkles_Text = '✨ ' + Sparkles_Text + ' ✨'

    return await message.send(Sparkles_Text)


@client.command(name="sparkle-text")
async def sparkle_text(message, *, args = None):
    Provide_Message = discord.Embed(title='You have to provide a message for Rune to sparkle text.', description='```R!sparkle_text <Text>```', color=0x87f587)
    Provide_Message.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if args is None:
        return await message.send(embed=Provide_Message)

    Sparkle_Text = '✨ ' + args + ' ✨'
    return await message.send(Sparkle_Text)


@client.command(name="say-in")
async def say_in(message, channel: discord.TextChannel = None, *, args = None):
    Mention = discord.Embed('You need to mention a channel for Rune to say in.', description='```R!say_in <Channel> <Text>```', color=0x87f587)
    Mention.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    Provide_Message = discord.Embed(title='You have to provide a message for Rune to say.', description='```R!say_in <Channel> <Text>```', color=0x87f587)
    Provide_Message.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if channel is None:
        return await message.send(embed=Mention)
    if args is None:
        return await message.send(embed=Provide_Message)

    await channel.send(args)

    Success = discord.Embed(description='```Message has been said.```', color=0x87f587)
    Success.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    
    return await message.send(embed=Success)


@client.command()
async def compliment(message, member: discord.Member = None):
    if member:
        return await message.send(f'{member.mention} {Communication.Compliment()}')

    return await message.send(f'{message.author.mention} {Communication.Compliment()}')


@client.command(name="say-to")
@has_permissions(manage_messages=True)
async def say_to(message, member: discord.Member = None, *, args = None):
    Mention = discord.Embed(title='You need have to mention a user.', description='```R!say_to <User> <Text>```', color=0x87f587)
    Mention.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    Provide_Message = discord.Embed(title='You have to provide a message for Rune to say.', description='```R!say_to <User> <Text>```', color=0x87f587)
    Provide_Message.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if member is None:
        return await message.send(embed=Mention)
    if args is None:
        return await message.send(embed=Provide_Message)

    await member.send(args)

    Success = discord.Embed(description='```Message has been sent.```', color=0x87f587)
    Success.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    return await message.send(embed=Success)

# Recontinue of Recreation of JSON as Database in Python ~ 5/7/21; May 7, 2021

def get_oc(OC_ID):
    with open(OCs_Storage, "r") as OCs:
        _OC_ = json.load(OCs)
        return next((_OC for _OC in _OC_ if _OC["OC_ID"] == int(OC_ID)), None)
def remove_dict(Storage, Key, Value):
    with open(Storage, "r") as Datas:
        _Data_ = json.load(Datas)
    _Data_[:] = (Data for Data in _Data_ if Data.get(f"{Key}") != Value)
    with open(Storage, "w") as Datas:
        return json.dump(_Data_, Datas, indent=4)
def get_author(Author_ID):
    with open(OCs_Storage, "r") as OCs:
        _OC_ = json.load(OCs)
        return [_OC for _OC in _OC_ if _OC["Author_ID"] == int(Author_ID)]
def list_to_string(list, Separator): # ~ 6/3/21; June 3, 2021
    _Separator_ = str(Separator)
    return _Separator_.join(list)
def number_list_to_str(list, Separator): # ~ 6/3/21; June 3, 2021
    _Separator_ = str(Separator)
    return _Separator_.join([str(num) for num in list])
def get_guild(Storage, Guild_ID):
    with open(Storage, "r") as Data:
        _Data_ = json.load(Data)
        return [_Data for _Data in _Data_ if _Data["Guild_ID"] == int(Guild_ID)]
def edit_warns(Storage, Author_ID, Author_Name, Key): # ~ 6/8/21; June 8, 2021
    Data = get_author_id(Storage, Author_ID)
    # print(Data)

    Edited_Data = []
    with open(Storage, "r") as _Data:
        _Data_ = json.load(_Data)
    for Datas in _Data_:
        if Datas["Member_ID"] == Author_ID:
            Datas.update(
                {
                    "Username": Author_Name,
                    "Warns": Data[f"{Key}"] + 1,
                    "Guild_ID": 786716363539611679,
                    "Member_ID": 782851049316024360,
                }
            )
        Edited_Data.append(Datas)
    # print(Edited_Data)

    with open(Storage, "w") as _Data:
        json.dump(Edited_Data, _Data, indent=4)
def remove_warn(Storage, Author_ID, Author_Name, Key): # ~ 6/8/21; June 8, 2021
    Data = get_author_id(Storage, Author_ID)
    # print(Data)

    Edited_Data = []
    with open(Storage, "r") as _Data:
        _Data_ = json.load(_Data)
    for Datas in _Data_:
        if Datas["Member_ID"] == Author_ID:
            Datas.update(
                {
                    "Username": Author_Name,
                    "Warns": Data[f"{Key}"] - 1,
                    "Guild_ID": 786716363539611679,
                    "Member_ID": 782851049316024360,
                }
            )
        Edited_Data.append(Datas)
    # print(Edited_Data)

    with open(Storage, "w") as _Data:
        json.dump(Edited_Data, _Data, indent=4)
def edit_oc(Storage, Author_ID, OC_ID, Name=None, Avatar=None):
    Data = get_oc(OC_ID)

    if Data["Author_ID"] != Author_ID:
        return None
        
    Edited_Data = []
    with open(Storage, "r") as _Data:
        _Data_ = json.load(_Data)
    for Datas in _Data_:
        if Datas["OC_ID"] == OC_ID:
            Datas.update(
                {
                   "Author_ID": Author_ID,
                   "OC_Name": Data["OC_Name"] if Name is None else Name,
                   "OC_ID": Datas["OC_ID"],
                   "OC_Avatar": Data["OC_Avatar"] if Avatar is None else Avatar
                }
            )
        Edited_Data.append(Datas)

    with open(Storage, "w") as _Data:
        json.dump(Edited_Data, _Data, indent=4)

@client.command(name="add-oc")
async def add_oc(message, *, Name = None):  
    Provide_Name = discord.Embed(title='You have to provide the name for your OC.', description='```R!add_oc <Name> [Attachment]```', color=0x87f587)
    Provide_Name.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    Provide_Avatar = discord.Embed(title='You have to provide the avatar for your OC.', description='```R!add_oc <Name> [Attachment]```', color=0x87f587)
    Provide_Avatar.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    Avatar = None if len(message.message.attachments) == 0 else message.message.attachments[0].url
    # print(Avatar)

    if Name is None:
        return await message.send(embed=Provide_Name)
    if Avatar is None:
        return await message.send(embed=Provide_Avatar)

    OC = {}
    with open(OCs_Storage, "r") as _OCs:
        OCs = json.load(_OCs)
        ID = len(OCs) + 1
    OC["Author_ID"] = message.author.id
    OC["OC_Name"] = Name
    OC["OC_ID"] = ID
    OC["OC_Avatar"] = Avatar

    OCs.append(OC)
    with open(OCs_Storage, "w") as _OCs:
        json.dump(OCs, _OCs, indent=4)

    Success = discord.Embed(description=f"```{Name} has been added with the ID of {ID}.```", color=0x87f587)
    Success.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    return await message.send(message.author.mention, embed=Success)


@client.command(name="search-oc")
async def search_oc(message, *, ID = None):
    No_OCs = discord.Embed(description='```You don\'t have any OCs yet.```', color=0x87f587)
    No_OCs.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    Author_Check = get_author(message.author.id)
    if Author_Check is None:
        return await message.send(embed=No_OCs)

    Provide_ID = discord.Embed(title='You have to provide the ID of the OC you want to search for.', description='```R!search_oc <ID>```', color=0x87f587)
    Provide_ID.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if ID is None:
        return await message.send(embed=Provide_ID)

    OC = get_oc(ID)

    No_OC = discord.Embed(description='```There is no OC that you own with that ID.```', color=0x87f587)
    No_OC.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if OC is None:
        return await message.send(embed=No_OC)

    OC_Name = OC["OC_Name"]
    OC_ID = OC["OC_ID"]
    OC_Avatar = OC["OC_Avatar"]
    OC_Author = OC["Author_ID"]

    if OC_Author != message.author.id:
        return await message.send(embed=No_OC)

    OC_ = discord.Embed(description=f"```An OC was found with the name {OC_Name}```", color=0x87f587)
    OC_.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    OC_.set_thumbnail(url=OC_Avatar)
    OC_.add_field(name='Name:', value=f"```{OC_Name}```", inline=True)
    OC_.add_field(name='ID:', value=f"```{OC_ID}```", inline=True)
    OC_.set_footer(text=f"Author's ID - {OC_Author}")
    return await message.send(embed=OC_)


@client.command(name="remove-oc")
async def remove_oc(message, *, ID = None):
    No_OCs = discord.Embed(description='```You don\'t have any OCs yet.```', color=0x87f587)
    No_OCs.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    Author_Check = get_author(message.author.id)
    if Author_Check is None:
        return await message.send(embed=No_OCs)

    Provide_ID = discord.Embed(title='You have to provide the ID of the OC you want to remove.', description='```R!remove_oc <ID>```', color=0x87f587)
    Provide_ID.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if ID is None:
        return await message.send(embed=Provide_ID)

    _OC = get_oc(ID)

    No_OC = discord.Embed(description='```There is no OC that you own with that ID.```', color=0x87f587)
    No_OC.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    if _OC is None:
        return await message.send(embed=No_OC)

    OC_Name = _OC["OC_Name"]
    OC_Author = _OC["Author_ID"]

    if OC_Author != message.author.id:
        return await message.send(embed=No_OC)

    Success = discord.Embed(description=f"```{OC_Name} has been removed.```", color=0x87f587)
    Success.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.send(embed=Success)

    return remove_dict(OCs_Storage, "OC_ID", int(ID))


@client.command(name="oc-say")
async def oc_say(message, ID = None, *, args = None):
    No_OCs = discord.Embed(description='```You don\'t have any OCs yet.```', color=0x87f587)
    No_OCs.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    Author_Check = get_author(message.author.id)
    if Author_Check is None:
        return await message.send(embed=No_OCs)

    Provide_ID = discord.Embed(title='You have to provide the ID of the OC you want to talk as.', description='```R!oc_say <ID> <Message>```', color=0x87f587)
    Provide_ID.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    Provide_Message = discord.Embed(title='You have to provide a message for your OC to say.', description='```R!oc_say <ID> <Message>```', color=0x87f587)
    Provide_Message.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if ID is None:
        return await message.send(embed=Provide_ID)

    OC = get_oc(ID)

    No_OC = discord.Embed(description='```There is no OC that you own with that ID.```', color=0x87f587)
    No_OC.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    
    if OC is None:
        return await message.send(embed=No_OC)

    OC_Name = OC["OC_Name"]
    OC_Author = OC["Author_ID"]
    OC_Avatar = OC["OC_Avatar"]

    if OC_Author != message.author.id:
        return await message.send(embed=No_OC)
    if args is None:
        return await message.send(embed=Provide_Message)
    
    await message.message.delete()

    _Avatar_ = requests.get(f"{OC_Avatar}")

    _OC_ = await message.channel.create_webhook(name=OC_Name, avatar=_Avatar_.content)
    await _OC_.send(args)

    time.sleep(3)
    return await _OC_.delete()


@client.command(name="list-ocs")
async def list_ocs(message): # ~ 5/25/21; May 25, 2021
    No_OCs = discord.Embed(description='```You don\'t have any OCs yet.```', color=0x87f587)
    No_OCs.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    OC = get_author(message.author.id)
    # print(OC)
    if OC == []:
        return await message.send(embed=No_OCs)

    # print(OCs["OC_Name"]) ~ 5/25/21; May 25, 2021
    _OCs_Names = []
    for OCs in OC:
        OCs_Names_ = OCs["OC_Name"]
        _OCs_Names.append(OCs_Names_)
    
    _OCs_IDs = []
    for OCs in OC:
        OCs_IDs_ = OCs["OC_ID"]
        _OCs_IDs.append(OCs_IDs_)

    OCs_Names = list_to_string(_OCs_Names, "\n")
    # print(OCs_Names) ~ 6/3/21; June 3, 2021
    OCs_IDs = number_list_to_str(_OCs_IDs, "\n")
    
    _OCs_ = discord.Embed(title=f"[ {message.author.name}'s OCs ]", color=0x87f587)
    _OCs_.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    _OCs_.add_field(name='Name:', value='```\n' + OCs_Names + '```', inline=True)
    _OCs_.add_field(name='ID:', value='```\n' + OCs_IDs + '```', inline=True)
    _OCs_.set_footer(text=f"Author's ID - {message.author.id}")
    return await message.send(embed=_OCs_)


@client.command(name="clear-ocs")
async def clear_ocs(message):
    No_OCs = discord.Embed(description='```You don\'t have any OCs yet.```', color=0x87f587)
    No_OCs.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    OC = get_author(message.author.id)
    if OC is None:
        return await message.send(embed=No_OCs)

    remove_dict(OCs_Storage, "Author_ID", message.author.id)

    Success = discord.Embed(description='```Your OCs has been removed.```', color=0x87f587)
    Success.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    return await message.send(embed=Success)


@client.command()
async def flirt(message, member: discord.Member = None):
    if member:
        return await message.send(f'{member.mention} {Communication.Flirt()}')

    return await message.send(Communication.Flirt())


@client.command()
async def insult(message, member: discord.Member = None):
    if member:
        return await message.send(f'{member.mention} {Communication.Insult()}')

    return await message.send(f'{message.author.mention} {Communication.Insult()}')


@client.command()
async def roast(message, member: discord.Member = None):
    if member:
        return await message.send(f'{member.mention} {Communication.Roast()}')

    return await message.send(f'{message.author.mention} {Communication.Roast()}')


@client.command()
@has_permissions(manage_guild=True)
async def annoy(message, member: discord.Member = None, *, args = None):
    Mention = discord.Embed(title='You need have to mention a user.', description='```R!annoy <User> <Text>```', color=0x87f587)
    Mention.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    Provide_Message = discord.Embed(title='You have to provide a message for Rune to use.', description='```R!annoy <User> <Text>```', color=0x87f587)
    Provide_Message.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if member is None:
        return await message.send(embed=Mention)
    if args is None:
        return await message.send(embed=Provide_Message)

    ID = member.id

    Mentioned = {}
    with open(Annoys_Storage, "r") as _Mentions:
        Mentions = json.load(_Mentions)
    Mentioned["Username"] = member.name
    Mentioned["Message"] = args
    Mentioned["Guild_ID"] = message.guild.id
    Mentioned["Member_ID"] = ID

    Already = discord.Embed(description=f"{member.name} has already been set to be annoyed.", color=0x87f587)
    Already.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    
    Check = get_author_id(Annoys_Storage, ID)
    if Check and (Check["Guild_ID"] == message.guild.id):
        return await message.send('Already')

    Mentions.append(Mentioned)
    with open(Annoys_Storage, "w") as _Mentions:
        json.dump(Mentions, _Mentions, indent=4)

    Success = discord.Embed(description='```All set.```', color=0x87f587)
    Success.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    return await message.send(embed=Success)


@client.command(name="list-annoys")
@has_permissions(manage_guild=True)
async def list_annoys(message):
    No_Annoys = discord.Embed(description='```There are no members that has been assigned to be annoyed.```', color=0x87f587)
    No_Annoys.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    Guild_Annoys = get_guild(Annoys_Storage, message.guild.id)
    if Guild_Annoys == []:
        return await message.send(embed=No_Annoys)

    _Usernames = []
    for Usernames in Guild_Annoys:
        Usernames_ = Usernames["Username"]
        _Usernames.append(Usernames_)
    
    _IDs = []
    for IDs in Guild_Annoys:
        IDs_ = IDs["Member_ID"]
        _IDs.append(IDs_)

    _Messages = []
    for Messages in Guild_Annoys:
        Messages_ = Messages["Message"]
        _Messages.append(Messages_)

    _Usernames_ = list_to_string(_Usernames, "\n")
    _IDs_ = number_list_to_str(_IDs, "\n")
    _Messages_ = number_list_to_str(_Messages, "\n")
    
    Annoys = discord.Embed(title=f"[ {message.guild.name}'s members that are to be annoyed ]", color=0x87f587)
    Annoys.set_author(name=message.guild.name, icon_url=message.guild.icon_url)
    Annoys.add_field(name='Username:', value='```\n' + _Usernames_ + '```', inline=True)
    Annoys.add_field(name='ID:', value='```\n' + _IDs_ + '```', inline=True)
    Annoys.add_field(name='Message to respond:', value='```\n' + _Messages_ + '```', inline=True)
    return await message.send(embed=Annoys)


@client.command()
@has_permissions(manage_guild=True)
async def unannoy(message, *, ID = None):
    Provide_ID = discord.Embed(title='You have to provide an ID.', description='```R!unannoy <ID>```', color=0x87f587)
    Provide_ID.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    
    if ID is None:
        return await message.send(embed=Provide_ID)

    _Member = get_author_id(Annoys_Storage, ID)

    No_Member = discord.Embed(description='```There was no member found with that ID.```', color=0x87f587)
    No_Member.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    
    if _Member is None:
        return await message.send(embed=No_Member)

    Member_Name = _Member["Username"]
    Member_Guild = _Member["Guild_ID"]

    if Member_Guild != message.guild.id:
        return await message.send(embed=No_Member)

    Success = discord.Embed(description=f"```{Member_Name} has been unannoyed; Not to be annoyed anymore.```", color=0x87f587)
    Success.set_author(name=message.guild.name, icon_url=message.guild.icon_url)
    await message.send(embed=Success)

    def unannoy(ID):
        with open(Annoys_Storage, "r") as Annoys:
            _Annoy_ = json.load(Annoys)
        _Annoy_[:] = (Annoy for Annoy in _Annoy_ if Annoy.get('Member_ID') != int(ID))
        with open(Annoys_Storage, "w") as Annoys:
            return json.dump(_Annoy_, Annoys, indent=4)
    return unannoy(ID)


@client.command()
@has_permissions(administrator=True)
async def warn(message, member: discord.Member = None):
    Mention = discord.Embed(title='You need have to mention a user.', description='```R!warn <User>```', color=0x87f587)
    Mention.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    
    if member is None:
        return await message.send(embed=Mention)

    Author = get_author_id(Warnings_Storage, member.id)
    if Author is None:
        Mentioned = {}
        with open(Warnings_Storage, "r") as _Warnings:
            Warnings = json.load(_Warnings)
        Mentioned["Username"] = member.name
        Mentioned["Warns"] = 1
        Mentioned["Guild_ID"] = message.guild.id
        Mentioned["Member_ID"] = member.id

        Warnings.append(Mentioned)
        with open(Warnings_Storage, "w") as _Warnings:
            json.dump(Warnings, _Warnings, indent=4)

        Success = discord.Embed(description=f"```{member.name} has been warned, {member.name} has 1 warning.```", color=0x87f587)
        Success.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        return await message.send(embed=Success)
    
    edit_warns(Warnings_Storage, member.id, member.name, "Warns") # ~ 6/8/21; June 8, 2021
    
    Success = discord.Embed(description=f"```{member.name} has been warned, {member.name} now has {Author['Warns'] + 1} warnings.```", color=0x87f587)
    Success.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    return await message.send(embed=Success)


@client.command()
@has_permissions(administrator=True)
async def warns(message):
    No_Warns = discord.Embed(description='```No one has been warned yet.```', color=0x87f587)
    No_Warns.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    Guild_Warns = get_guild(Warnings_Storage, message.guild.id)
    if Guild_Warns == []:
        return await message.send(embed=No_Warns)

    _Usernames = []
    for Usernames in Guild_Warns:
        Usernames_ = Usernames["Username"]
        _Usernames.append(Usernames_)
    
    _IDs = []
    for IDs in Guild_Warns:
        IDs_ = IDs["Member_ID"]
        _IDs.append(IDs_)

    _Warns = []
    for Warns in Guild_Warns:
        Warns_ = Warns["Warns"]
        _Warns.append(Warns_)

    _Usernames_ = list_to_string(_Usernames, "\n")
    _IDs_ = number_list_to_str(_IDs, "\n")
    _Warns_ = number_list_to_str(_Warns, "\n")
    
    Annoys = discord.Embed(title=f"[ {message.guild.name}'s members that are to be annoyed ]", color=0x87f587)
    Annoys.set_author(name=message.guild.name, icon_url=message.guild.icon_url)
    Annoys.add_field(name='Username:', value='```\n' + _Usernames_ + '```', inline=True)
    Annoys.add_field(name='Warnings:', value='```\n' + _Warns_ + '```', inline=True)
    Annoys.add_field(name='ID:', value='```\n' + _IDs_ + '```', inline=True)
    return await message.send(embed=Annoys)


@client.command()
@has_permissions(administrator=True)
async def unwarn(message, *, ID = None): # ~ 6/8/21; June 8, 2021
    Provide_ID = discord.Embed(title='You have to provide an ID of a warned member.', description='```R!unwarn <ID>```', color=0x87f587)
    Provide_ID.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    
    if ID is None:
        return await message.send(embed=Provide_ID)
    if ID == discord.Member:
        return await message.send(embed=Provide_ID)
    if type(int(ID)) is not int:
        return await message.send(embed=Provide_ID)

    ID = int(ID)
    # print(type(ID))

    _Member = get_author_id(Warnings_Storage, ID)

    No_Member = discord.Embed(description='```There was no member found with that ID.```', color=0x87f587)
    No_Member.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    
    if _Member is None:
        return await message.send(embed=No_Member)

    Member_Name = _Member["Username"]
    Member_Guild = _Member["Guild_ID"]
    Member_Warnings = _Member["Warns"]

    if Member_Guild != message.guild.id:
        return await message.send(embed=No_Member)

    if Member_Warnings - 1 == 0:
        Success = discord.Embed(description=f"```{Member_Name} has been unwarned, {Member_Name} no longer has a warning.```", color=0x87f587)
        Success.set_author(name=message.guild.name, icon_url=message.guild.icon_url)
        await message.send(embed=Success)

        return remove_dict(Warnings_Storage, "Member_ID", ID)

    async def Successful(Description):
        Success = discord.Embed(description=f"```{Description}```", color=0x87f587)
        Success.set_author(name=message.guild.name, icon_url=message.guild.icon_url)
        await message.send(embed=Success)

        Member_Username = client.get_user(ID)
        # print(f"{Member_Name} | {Member_Username.name}")

        return remove_warn(Warnings_Storage, ID, Member_Username.name, "Warns")
    if Member_Warnings - 1 == 1:
        return await Successful(f"{Member_Name} has been unwarned, {Member_Name} now has 1 warning.")

    await Successful(f"{Member_Name} has been unwarned, {Member_Name} now has {Member_Warnings - 1} warnings.")


@client.command(name="edit-oc-name")
async def edit_oc_name(message, ID = None, *, args = None):
    No_OCs = discord.Embed(description='```You don\'t have any OCs yet.```', color=0x87f587)
    No_OCs.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    Author_Check = get_author(message.author.id)
    if Author_Check is None:
        return await message.send(embed=No_OCs)

    Provide_ID = discord.Embed(title='You have to provide an ID.', description='```R!edit_oc_name <ID> <Name>```', color=0x87f587)
    Provide_ID.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    Provide_Name = discord.Embed(title='You have to provide a name for your OC.', description='```R!edit_oc_name <ID> <Name>```', color=0x87f587)    
    Provide_Name.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if ID is None:
        return await message.send(embed=Provide_ID)
    
    No_OC = discord.Embed(description='```There is no OC that you own with that ID.```', color=0x87f587)
    No_OC.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    ID = int(ID)
    OC = get_oc(ID)
    if OC is None:
        return await message.send(embed=No_OC)

    OC_Name = OC["OC_Name"]
    OC_Avatar = OC["OC_Avatar"]
    OC_Author = OC["Author_ID"]

    # print(OC_Name)
    # print(OC_ID)
    # print(OC_Avatar)
    # print(OC_Author)

    if OC_Author != message.author.id:
        return await message.send(embed=No_OC)

    if args is None:
        return await message.send(embed=Provide_Name)

    Success = discord.Embed(description=f"```{OC_Name}'s name has been changed to {args}.```", color=0x87f587)
    Success.set_author(name=args, icon_url=OC_Avatar)
    await message.send(embed=Success)

    edit_oc(OCs_Storage, message.author.id, ID, Name=args)


@client.command(name="edit-oc-avatar")
async def edit_oc_avatar(message, ID = None, *, args = None):
    No_OCs = discord.Embed(description='```You don\'t have any OCs yet.```', color=0x87f587)
    No_OCs.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    Author_Check = get_author(message.author.id)
    if Author_Check is None:
        return await message.send(embed=No_OCs)

    Provide_ID = discord.Embed(title='You have to provide an ID.', description='```R!edit_oc_avatar <ID> [Attachment]```', color=0x87f587)
    Provide_ID.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    Provide_Name = discord.Embed(title='You have to provide an avatar for your OC.', description='```R!edit_oc_avatar <ID> [Attachment]```', color=0x87f587)    
    Provide_Name.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    if ID is None:
        return await message.send(embed=Provide_ID)

    No_OC = discord.Embed(description='```There is no OC that you own with that ID.```', color=0x87f587)
    No_OC.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    ID = int(ID)
    OC = get_oc(ID)
    if OC is None:
        return await message.send(embed=No_OC)

    OC_Name = OC["OC_Name"]
    OC_Author = OC["Author_ID"]

    if OC_Author != message.author.id:
        return await message.send(embed=No_OC)

    Avatar = None if len(message.message.attachments) == 0 else message.message.attachments[0].url
    if Avatar is None:
        return await message.send(embed=Provide_Name)

    Success = discord.Embed(description=f"```{OC_Name}'s avatar has been changed.```", color=0x87f587)
    Success.set_author(name=OC_Name, icon_url=Avatar)
    await message.send(embed=Success)

    edit_oc(OCs_Storage, message.author.id, ID, Avatar=Avatar)


@client.command()
async def joke(message):
    return await message.send(Communication.Joke())


@client.command()
async def help(message, args = None):
    if args is None:
        Help = discord.Embed(description='```The Prefix for Rune is R!```', color=0x87f587)
        Help.add_field(name='help', value='```Rune will send this.```', inline=True)
        Help.add_field(name='help moderation', value='```Rune will send the list of moderation commands.```', inline=True)
        Help.add_field(name='help oc', value='```Rune will send the list of OC/Character commands.```', inline=True)
        Help.add_field(name='ping', value='```Rune will send the amount of miliseconds it takes to send a message; response time.```', inline=True)
        Help.add_field(name='invite', value='```Rune will send his invite link, and all the other links of my projects.```', inline=True)
        Help.add_field(name='say', value='```Rune will repeat the message you want him to say.```', inline=True)
        Help.add_field(name='say-in', value='```Rune will say the message you want to send in a channel.```', inline=True)
        Help.add_field(name='say-to', value='```Rune will say the message you want to send to a specified member.```', inline=True)
        Help.add_field(name='iq', value='```Rune will send your iq.```', inline=True)
        Help.add_field(name='owofy', value='```Wune wiww twanswate and send youw message wike this.```', inline=True)
        Help.add_field(name='clap-text', value='```Rune 👏 will 👏 turn 👏 and 👏 send 👏 your 👏 message 👏 like 👏 this.```', inline=True)
        Help.add_field(name='sparkles-text', value='```✨ Rune ✨ will ✨ turn ✨ and ✨ send ✨ your ✨ message ✨ like ✨ this. ✨.```', inline=True)
        Help.add_field(name='sparkle-text', value='```✨ Rune will turn and send your message like this. ✨```', inline=True)
        Help.add_field(name='eject', value='```Eject a specified member.```', inline=True)
        Help.add_field(name='compliment', value='```Rune will send a random compliment to you or to a specified member.```', inline=True)
        Help.add_field(name='insult', value='```Rune will send a random insult to you or to a specified member.```', inline=True)
        Help.add_field(name='flirt', value='```Rune will send a random flirt or to a specified member.```', inline=True)
        Help.add_field(name='roast', value='```Rune will send a random roast/comeback to you or to a specified member.```', inline=True)
        Help.add_field(name='joke', value='```Rune will send a random joke to you or to a specified member.```', inline=True)

        return await message.send(embed=Help)
    elif args.lower() == 'oc':
        Help_OC = discord.Embed(description='```Here is the list of OC/Character Commands```', color=0x87f587)
        Help_OC.add_field(name='add-oc', value='Add an OC/Character.', inline=True)
        Help_OC.add_field(name='remove-oc', value='Remove an OC/Character.', inline=True)
        Help_OC.add_field(name='oc-say', value='Talk as one of your OCs; Roleplay as your OCs.', inline=True)
        Help_OC.add_field(name='list-ocs', value='Rune will send your OC(s)/Character(s).', inline=True)
        Help_OC.add_field(name='clear-ocs', value='Remove all of your OCs.', inline=True)
        Help_OC.add_field(name='edit-oc-name', value='Edit an OC\'s/Character\'s name.', inline=True)
        Help_OC.add_field(name='edit-oc-avatar', value='Edit an OC\'s/Character\'s avatar.', inline=True)

        return await message.send(embed=Help_OC)
    elif args.lower() == 'moderation':
        Help_Moderation = discord.Embed(description='```Here is the list of Moderation Commands```', color=0x87f587)
        Help_Moderation.add_field(name='warn', value='Warn a specified member.', inline=True)
        Help_Moderation.add_field(name='warns', value='Rune will send all of the warns of warned members/a warned member.', inline=True)
        Help_Moderation.add_field(name='unwarn', value='Remove a warn from a specifed member.', inline=True)
        Help_Moderation.add_field(name='annnoy', value='Rune will annoy a member; Sends the specified message everytime the specified member sends a message.', inline=True)
        Help_Moderation.add_field(name='annoys', value='Rune will send the member/all of the members that are to be annoyed.', inline=True)
        Help_Moderation.add_field(name='unannoy', value='Remove a specifed member from the annoy list.', inline=True)

        return await message.send(embed=Help_Moderation)


@client.command()
async def invite(message):
    Invite = discord.Embed(title='Links', description="[Rune's Invite Link](https://discord.com/oauth2/authorize?client_id=781224758355820555&permissions=8&scope=bot)\n[Discord Server Invite Link](https://discord.io/TheTalk)", color=0x87f587)
    Invite.add_field(name='Incompletes', value="[Mitch's Invite Link](https://discord.com/oauth2/authorize?client_id=786702998998482955&permissions=8&scope=bot)\n[Nova's Invite Link](https://discord.com/api/oauth2/authorize?client_id=813290586085261322&permissions=8&scope=bot)\n[Rea's Invite Link](https://discord.com/oauth2/authorize?client_id=843626815498879067&permissions=8&scope=bot)")
    
    return await message.send(embed=Invite)


client.run(os.environ['Token'])