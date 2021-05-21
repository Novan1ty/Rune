import requests # pip install requests

async def URL_to_Bytes():
    OC_Avatar = "https://media.discordapp.net/attachments/839163340714409996/844421314147254362/Mitch.jpg"

    await message.message.delete() # Deletes the original message.

    _Avatar_ = requests.get(OC_Avatar) # Make sure the parameter or URL is a string.

    _OC_ = await message.channel.create_webhook(name="Mitch", avatar=_Avatar_.content)
    await _OC_.send("Heya")