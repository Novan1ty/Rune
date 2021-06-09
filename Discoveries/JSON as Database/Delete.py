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
        "OC_Name": "Luna",
        "OC_ID": 2
    }
]

def get_data(OC_ID):
    with open (OCs_Storage, "r") as OCs:
        _OC_ = json.load(OCs)
        return next((_OC for _OC in _OC_ if _OC["OC_ID"] == int(OC_ID)), None)

def delete_data(OC_ID):
    with open (OCs_Storage, "r") as OCs:
        _OC_ = json.load(OCs)
    _OC_[:] = (OC for OC in _OC_ if OC.get("OC_ID") != int(OC_ID))
    with open (OCs_Storage, "w") as OCs:
        return json.dump(_OC_, OCs, indent=4)

OC = get_data(1)
if OC is None:
    print ('No OC Found.')
else:
    delete_data(1)
    
    with open (OCs_Storage, "r") as OCs:
        _OCs_ = json.load(OCs)
    print (_OCs_)