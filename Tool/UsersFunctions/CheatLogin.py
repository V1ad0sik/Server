import Tool.Data.ModuleSQLite as ModuleSQLite
import Tool.Data.ModuleJSON as ModuleJSON

import Tool.Service.Log as Log
import Tool.Service.GetDateTime as GetDateTime
import Tool.Service.GetVacStatus as GetVacStatus

import json

def CheatLogin(Message):
    ClientCheatVersion = int(Message["version"])
    ServerCheatVersion = ModuleJSON.ReadConfig("Version")["Cheat"]

    if (ClientCheatVersion == ServerCheatVersion):
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
                            
                            ServerStruct = {"status": 2010, "hwid": ServerUserID}
                            AddresList = ModuleJSON.ReadConfig("Offsets")

                            ServerStruct["dwLocalPlayer"] = AddresList["dwLocalPlayer"]
                            ServerStruct["dwEntityList"] = AddresList["dwEntityList"]
                            ServerStruct["dwGlowObjectManager"] = AddresList["dwGlowObjectManager"]
                            ServerStruct["dwClientState"] = AddresList["dwClientState"]
                            ServerStruct["dwClientState_ViewAngles"] = AddresList["dwClientState_ViewAngles"]
                            ServerStruct["dwForceAttack"] = AddresList["dwForceAttack"]
                            ServerStruct["model_ambient_min"] = AddresList["model_ambient_min"]
                            ServerStruct["dwMouseEnable"] = AddresList["dwMouseEnable"]
                            ServerStruct["dwForceJump"] = AddresList["dwForceJump"]
                            ServerStruct["dwViewMatrix"] = AddresList["dwViewMatrix"]
                            ServerStruct["dwbSendPackets"] = AddresList["dwbSendPackets"]
                            ServerStruct["dwMouseIndexActive"] = AddresList["dwMouseIndexActive"]
                            ServerStruct["m_bDormant"] = AddresList["m_bDormant"]

                            ServerStruct["m_iGlowIndex"] = AddresList["m_iGlowIndex"]
                            ServerStruct["m_iTeamNum"] = AddresList["m_iTeamNum"]
                            ServerStruct["m_iHealth"] = AddresList["m_iHealth"]
                            ServerStruct["m_vecOrigin"] = AddresList["m_vecOrigin"]
                            ServerStruct["m_dwBoneMatrix"] = AddresList["m_dwBoneMatrix"]
                            ServerStruct["m_vecViewOffset"] = AddresList["m_vecViewOffset"]
                            ServerStruct["m_aimPunchAngle"] = AddresList["m_aimPunchAngle"]
                            ServerStruct["m_iShotsFired"] = AddresList["m_iShotsFired"]
                            ServerStruct["m_clrRender"] = AddresList["m_clrRender"]
                            ServerStruct["m_bUseCustomAutoExposureMax"] = AddresList["m_bUseCustomAutoExposureMax"]
                            ServerStruct["m_bUseCustomAutoExposureMin"] = AddresList["m_bUseCustomAutoExposureMin"]
                            ServerStruct["m_flCustomAutoExposureMax"] = AddresList["m_flCustomAutoExposureMax"]
                            ServerStruct["m_flCustomAutoExposureMin"] = AddresList["m_flCustomAutoExposureMin"]
                            ServerStruct["m_iDefaultFOV"] = AddresList["m_iDefaultFOV"]
                            ServerStruct["m_iCrosshairId"] = AddresList["m_iCrosshairId"]
                            ServerStruct["m_hMyWeapons"] = AddresList["m_hMyWeapons"]
                            ServerStruct["m_iItemDefinitionIndex"] = AddresList["m_iItemDefinitionIndex"]
                            ServerStruct["m_OriginalOwnerXuidLow"] = AddresList["m_OriginalOwnerXuidLow"]
                            ServerStruct["m_iItemIDHigh"] = AddresList["m_iItemIDHigh"]
                            ServerStruct["m_nFallbackPaintKit"] = AddresList["m_nFallbackPaintKit"]
                            ServerStruct["m_iAccountID"] = AddresList["m_iAccountID"]
                            ServerStruct["m_nFallbackStatTrak"] = AddresList["m_nFallbackStatTrak"]
                            ServerStruct["m_nFallbackSeed"] = AddresList["m_nFallbackSeed"]
                            ServerStruct["m_fFlags"] = AddresList["m_fFlags"]
                            ServerStruct["m_bSpotted"] = AddresList["m_bSpotted"]
                            ServerStruct["m_flFlashMaxAlpha"] = AddresList["m_flFlashMaxAlpha"]
                            ServerStruct["m_hActiveWeapon"] = AddresList["m_hActiveWeapon"]
                            ServerStruct["m_bIsScoped"] = AddresList["m_bIsScoped"]

                            Log.Save("[Login.py | ИНФОРМАЦИЯ] > Авторизация пройдена.")
                            return json.dumps(ServerStruct)

                        else:
                            Log.Save("[Login.py | ИНФОРМАЦИЯ] > Чит обнаружен VAC.")
                            return json.dumps({"status": 2011})

                    else:
                        Log.Save("[Login.py | ИНФОРМАЦИЯ] > Подписка истекла.")
                        return json.dumps({"status": 2011})

                else:
                    Log.Save("[Login.py | ИНФОРМАЦИЯ] > User ID заблокирован.")
                    return json.dumps({"status": 2011})

            else:
                Log.Save("[Login.py | ИНФОРМАЦИЯ] > HWID Ключи не схоядтся.")
                return json.dumps({"status": 2011})

        else:
            Log.Save("[Login.py | ИНФОРМАЦИЯ] > User ID не зарегистрирован.")
            return json.dumps({"status": 2011})

    else:
        Log.Save("[Login.py | ИНФОРМАЦИЯ] > Версия загрузчика устарела.")
        return json.dumps({"status": 2011})