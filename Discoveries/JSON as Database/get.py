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

def get_data(OC_ID):
    with open (OCs_Storage, "r") as OCs:
        _OC_ = json.load(OCs)
        return next((_OC for _OC in _OC_ if _OC["OC_ID"] == int(OC_ID)), None)

OC = get_data(1)
if OC is None:
    print ('No OC Found.')
else:
    # print (OC) | {'Author': '564145650736955402', 'OC_Name': 'Luna', 'OC_ID': 2}

    # Getting The Values
    OC_Name = OC["OC_Name"]
    OC_ID = OC["OC_ID"]
    OC_Author = OC["Author"]
    
    print (OC_Name)
    print (OC_ID)
    print (OC_Author)