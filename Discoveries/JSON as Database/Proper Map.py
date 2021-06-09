# The Proper way of mapping values by keys in a List of Dictionaries ~ 6/3/21; June 3, 2021

_OC_ = [
    {
        "Author_ID": "564145650736955402",
        "OC_Name": "Mitch",
        "OC_ID": 1,
        "OC_Avatar": "https://media.discordapp.net/attachments/839163340714409996/844421314147254362/Mitch.jpg"
    },
    {
        "Author_ID": "564145650736955402",
        "OC_Name": "Rune",
        "OC_ID": 2,
        "OC_Avatar": "https://media.discordapp.net/attachments/837243636663975936/846657748060995624/Rune.jpg?width=610&height=610"
    },
    {
        "Author_ID": "564145650736955402",
        "OC_Name": "Luna",
        "OC_ID": 3,
        "OC_Avatar": "https://media.discordapp.net/attachments/837243636663975936/846768163495739472/Luna.jpg?width=609&height=609"
    }
]

def get_author(Author_ID):
    return [OC for OC in _OC_ if OC["Author_ID"] == str(Author_ID)]
def list_to_string(list, Separator):
    _Separator_ = str(Separator)
    return _Separator_.join(list)
def number_list_to_str(list, Separator): # ~ 6/3/21; June 3, 2021
    _Separator_ = str(Separator)
    return _Separator_.join([str(num) for num in list])

OC = get_author(564145650736955402)

_OCs_Names = []
for OCs in OC:
    OCs_Names_ = OCs["OC_Name"]
    _OCs_Names.append(OCs_Names_)

_OCs_IDs = []
for OCs in OC:
    OCs_IDs_ = OCs["OC_ID"]
    _OCs_IDs.append(OCs_IDs_)

"""
OCs Names: ['Mitch', 'Rune', 'Luna']
OCs IDs: [1, 2, 3]
"""
print(f"\nOCs Names: {_OCs_Names}\nOCs IDs: {_OCs_IDs}")

OCs_Names = list_to_string(_OCs_Names, ", ")
OCs_IDs = number_list_to_str(_OCs_IDs, ", ")
print("------------------------------------")

"""
OCs Names: Mitch, Rune, Luna
OCs IDs: 1, 2, 3
"""
print(f"OCs Names: {OCs_Names}\nOCs IDs: {OCs_IDs}\n")