import Tool.Data.ModuleSQLite as ModuleSQLite
import Tool.Data.ModuleJSON as ModuleJSON

import Tool.Service.Log as Log
import Tool.Service.GetDateTime as GetDateTime
import Tool.Service.GetVacStatus as GetVacStatus

import json

def Login(Message):
    ClietnLoaderVersion = int(Message["version"])
    ServerLoaderVersion = ModuleJSON.ReadConfig("Version")["Loader"]

    if (ClietnLoaderVersion == ServerLoaderVersion):
        ClientUserID = Message["user_id"]
        
        if (ModuleSQLite.Request(f"SELECT UserID FROM Users WHERE UserID = '{ClientUserID}'")):
            ClientHWID = Message["hwid"]
            ServerUserID = ModuleSQLite.RequestOne(f"SELECT HWID FROM Users WHERE UserID = '{ClientUserID}'")

            if (ServerUserID == "HWID NOT DETECTED"):
                Log.Save("[Login.py | ИНФОРМАЦИЯ] > HWID Привязан.")
                ModuleSQLite.Request(f"UPDATE Users SET HWID = '{ClientHWID}' WHERE UserID = '{ClientUserID}'")


            if (ModuleSQLite.Request(f"SELECT UserID FROM Users WHERE UserID = '{ClientUserID}' AND HWID = '{ClientHWID}'")):
                ClientIsBanned = bool(ModuleSQLite.RequestOne(f"SELECT BanStatus FROM Users WHERE UserID = '{ClientUserID}'"))

                if (not ClientIsBanned):
                    ClientEndTime = ModuleSQLite.RequestOne(f"SELECT EndTime FROM Users WHERE UserID = '{ClientUserID}'")

                    if (GetDateTime.DiffTimeToSecond(ClientEndTime) > 0):
                        if (not GetVacStatus.IsBlock()):
                            ClientSumTimeHorus = GetDateTime.DiffTimeToHours(ModuleSQLite.RequestOne(f"SELECT EndTime FROM Users WHERE UserID = '{ClientUserID}'"))
                            ServerCheatLink = ModuleJSON.ReadConfig("Cheat")["Link"]

                            Log.Save("[Login.py | ИНФОРМАЦИЯ] > Авторизация пройдена.")
                            return json.dumps({"status": 2006, "time": str(ClientSumTimeHorus), "link": ServerCheatLink})

                        else:
                            Log.Save("[Login.py | ИНФОРМАЦИЯ] > Чит обнаружен VAC.")
                            return json.dumps({"status": 2005})

                    else:
                        Log.Save("[Login.py | ИНФОРМАЦИЯ] > Подписка истекла.")
                        return json.dumps({"status": 2004})

                else:
                    Log.Save("[Login.py | ИНФОРМАЦИЯ] > User ID заблокирован.")
                    return json.dumps({"status": 2003})

            else:
                Log.Save("[Login.py | ИНФОРМАЦИЯ] > HWID Ключи не схоядтся.")
                return json.dumps({"status": 2002})

        else:
            Log.Save("[Login.py | ИНФОРМАЦИЯ] > User ID не зарегистрирован.")
            return json.dumps({"status": 2001})

    else:
        Log.Save("[Login.py | ИНФОРМАЦИЯ] > Версия загрузчика устарела.")
        return json.dumps({"status": 2000})