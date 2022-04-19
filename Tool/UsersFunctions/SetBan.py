import Tool.Data.ModuleSQLite as ModuleSQLite

import Tool.Service.Log as Log
import Tool.Service.GetDateTime as GetDateTime
import json


def SetBan(Message, IP):
    UserID = str(Message["user_id"])
    Info = str(Message["info"])

    if (ModuleSQLite.Request(f"SELECT UserID FROM Users WHERE UserID = '{UserID}'")):
        ModuleSQLite.Request(f"UPDATE Users SET BanStatus = '1' WHERE UserID = '{UserID}'")
        InfoLog = f"User ID: {UserID}\nПричина блокировки: {Info}\nIP: {IP}\nВремя блокировки: {GetDateTime.ThisTime()}\n\n"

        Log.Save(f"[SetBan.py | ИНФОРМАЦИЯ] > User ID Был заблокирован. ({Info})")
        Log.SaveBanLog(UserID, InfoLog)

    else:
        HWID = str(Message["hwid"])
        ModuleSQLite.Request(f"UPDATE Users SET BanStatus = '1' WHERE HWID = '{HWID}'")

        Log.Save(f"[SetBan.py | ИНФОРМАЦИЯ] > Сработала HWID блокировка. ({Info})")

    
    return json.dumps({"status": 2012})