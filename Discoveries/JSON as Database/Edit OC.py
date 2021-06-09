import json

OCs_Storage = "./Storages/OCs.json"

def get_oc(OC_ID):
    with open(OCs_Storage, "r") as OCs:
        _OC_ = json.load(OCs)
        return next((_OC for _OC in _OC_ if _OC["OC_ID"] == int(OC_ID)), None)
def edit_oc(Storage, Author_ID, OC_ID, Name=None, Avatar=None):
    Data = get_oc(OC_ID)

    if Data["Author_ID"] != Author_ID:
        return print(None)
        
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

edit_oc(OCs_Storage, 564145650736955402, 2, Name="Luna")