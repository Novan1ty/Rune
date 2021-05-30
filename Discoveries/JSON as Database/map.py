# Mapping Values by Keys in a List of Dictionaries ~ 5/25/21; May 25, 2021

_OC_ = [
    {
        "Author": "564145650736955402",
        "OC_Name": "Mitch",
        "OC_ID": 1,
        "OC_Avatar": "https://media.discordapp.net/attachments/839163340714409996/844421314147254362/Mitch.jpg"
    },
    {
        "Author": "564145650736955402",
        "OC_Name": "Rune",
        "OC_ID": 2,
        "OC_Avatar": "https://media.discordapp.net/attachments/837243636663975936/846657748060995624/Rune.jpg?width=610&height=610"
    },
    {
        "Author": "564145650736955402",
        "OC_Name": "Luna",
        "OC_ID": 3,
        "OC_Avatar": "https://media.discordapp.net/attachments/837243636663975936/846768163495739472/Luna.jpg?width=609&height=609"
    }
]
def get_author(Author_ID):
    return [OC for OC in _OC_ if OC["Author"] == str(Author_ID)]

OC = get_author(564145650736955402)
for OCs in OC:
	print(OCs["OC_Name"])