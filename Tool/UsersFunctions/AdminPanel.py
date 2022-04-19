import json
import Tool.Data.ModuleSQLite as ModuleSQLite
import Tool.Service.GetDateTime as GetDateTime
import Tool.Service.GetRandomData as GetRandomData
import Tool.Service.Log as Log

def GoTo(Message):
    Status = int(Message["point"])

    if (Status == 90001):
        return GetAllUsers()

    if (Status == 90002):
        return BanUserID(Message)

    if (Status == 90003):
        return UnBan(Message)

    if (Status == 90004):
        return GetAccount()

    if (Status == 90005):
        return HWIDReset(Message)


def GetAllUsers():
    UsersList = ModuleSQLite.Request("SELECT * FROM Users")

    Log.Save("[AdminPanel.py | ИНФОРМАЦИЯ] > Был выдан список пользователей.")
    return (str(UsersList))


def BanUserID(Message):
    Type = Message["type"]

    if (Type == 1):
        ClientUserID = Message["user_id"]

        if (ModuleSQLite.Request(f"SELECT UserID FROM Users WHERE UserID = '{ClientUserID}'")):
            ModuleSQLite.Request(f"UPDATE Users SET BanStatus = '1' WHERE UserID = '{ClientUserID}'")

            Log.Save(f"[AdminPanel.py | ИНФОРМАЦИЯ] > UserID '{ClientUserID}' был заблокирован.")
            return json.dumps({"status": 1})

        else:
            Log.Save(f"[AdminPanel.py | ИНФОРМАЦИЯ] > UserID '{ClientUserID}' не найден.")
            return json.dumps({"status": 0})


    if (Type == 2):
        ClientHWID = Message["hwid"]
        ModuleSQLite.Request(f"UPDATE Users SET BanStatus = '1' WHERE HWID = '{ClientHWID}'")

        Log.Save(f"[AdminPanel.py | ИНФОРМАЦИЯ] > Все аккаунты с HWID '{ClientHWID}' заблокированы.")
        return json.dumps({"status": 1})


def UnBan(Message):
    ClientUserID = Message["user_id"]

    if (ModuleSQLite.Request(f"SELECT UserID FROM Users WHERE UserID = '{ClientUserID}'")):
        ModuleSQLite.Request(f"UPDATE Users SET BanStatus = '0' WHERE UserID = '{ClientUserID}'")

        Log.Save(f"[AdminPanel.py | ИНФОРМАЦИЯ] > UserID '{ClientUserID}' был разблокирован.")
        return json.dumps({"status": 1})

    else:
        Log.Save(f"[AdminPanel.py | ИНФОРМАЦИЯ] > UserID '{ClientUserID}' не найден.")
        return json.dumps({"status": 0})


def GetAccount():
    NewUserID = GetRandomData.UserID()

    ThisTime = GetDateTime.ThisTime()
    UserSubTime = GetDateTime.SubTime()

    ModuleSQLite.Request(f"""INSERT INTO Users (UserID, HWID, BeginTime, EndTime, BanStatus, IP, Comment) VALUES
                                ('{NewUserID}', 'HWID NOT DETECTED', '{ThisTime}', '{UserSubTime}', '0', '127.0.0.1', 'Admin')""")


    Log.Save("[AdminPanel.py | ИНФОРМАЦИЯ] > Был создан аккаунт.")
    return json.dumps({"status": 1, "user_id": str(NewUserID)})


def HWIDReset(Message):
    ClientUserID = Message["user_id"]

    if (ModuleSQLite.Request(f"SELECT UserID FROM Users WHERE UserID = '{ClientUserID}'")):
        ModuleSQLite.Request(f"UPDATE Users SET HWID = 'HWID NOT DETECTED' WHERE UserID = '{ClientUserID}'")

        Log.Save("[AdminPanel.py | ИНФОРМАЦИЯ] > HWID сброшен.")
        return json.dumps({"status": 1})

    else:
        Log.Save("[AdminPanel.py | ИНФОРМАЦИЯ] > Не удалось сбросить HWID.")
        return json.dumps({"status": 0})