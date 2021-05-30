"""
Avatar = None if len(message.message.attachments) == 0 else message.message.attachments[0].url
# print(Avatar)

if Avatar is None:
    message.send('You have to provide the avatar for your OC.', embed=Provide)
"""