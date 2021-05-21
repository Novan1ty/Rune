import json
OCs_Storage = './Discoveries/JSON as Database/OCs.json'

Preview = [
    {
        "Author": "564145650736955402",
        "OC_Name": "Rune",
        "OC_ID": 1
    },
    {
        "Author": "564145650736955402",
        "OC_Name": "Luna",
        "OC_ID": 2
    }
]

Result = [
    {
        "Author": "564145650736955402",
        "OC_Name": "Rune",
        "OC_ID": 1
    },
    {
        "Author": "564145650736955402",
        "OC_Name": "Luna",
        "OC_ID": 2
    },
    {
        "Author": "564145650736955402",
        "OC_Name": "Rea",
        "OC_ID": 3
    }
]

OC = {}
with open (OCs_Storage, "r") as _OCs:
    OCs = json.load(_OCs)
    ID = len(OCs) + 1
OC["Author"] = "564145650736955402"
OC["OC_Name"] = "Rea"
OC["OC_ID"] = ID

OCs.append(OC)
with open (OCs_Storage, "w") as _OCs:
    json.dump(OCs, _OCs, indent=4)

OC_ = json.load(open(OCs_Storage, "r"))
print (OC_)