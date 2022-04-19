import Tool.Data.ModuleJSON as ModuleJSON
import Tool.Data.ModuleSQLite as ModuleSQLite

import Tool.Service.GetRandomData as GetRandomData
import Tool.Service.GetDateTime as GetDateTime
import Tool.Service.Log as Log

import requests, json


def CheckPay(Message, IP):
    ClientComment = str(Message["comment"])

    Token = ModuleJSON.ReadConfig("Pay")["Token"]
    Price = ModuleJSON.ReadConfig("Pay")["Price"]
    Phone = ModuleJSON.ReadConfig("Pay")["Phone"]

    Session = requests.Session()
    Session.headers["authorization"] = "Bearer " + Token

    GetSession = Session.get(f"https://edge.qiwi.com/payment-history/v2/persons/{Phone}/payments?rows=10", params = {"rows": "10"})
    JSONSession = json.loads(GetSession.text)

    for i in range (len(JSONSession)):
        try:
            ThisComment = str(JSONSession["data"][i]["comment"])
            TthisAmount = int(JSONSession["data"][i]["sum"]["amount"])
        except:
            continue

        if ((ClientComment == ThisComment) and (TthisAmount >= Price)):
            if (not ModuleSQLite.Request(f"SELECT Comment FROM Users WHERE Comment = '{ClientComment}'")):
                NewUserID = GetRandomData.UserID()

                ThisTime = GetDateTime.ThisTime()
                UserSubTime = GetDateTime.SubTime()

                ModuleSQLite.Request(f"""INSERT INTO Users (UserID, HWID, BeginTime, EndTime, BanStatus, IP, Comment) VALUES
                                         ('{NewUserID}', 'HWID NOT DETECTED', '{ThisTime}', '{UserSubTime}', '0', '{IP}', '{ClientComment}')""")

                Log.Save("[CheckPay.py | ИНФОРМАЦИЯ] > Был выдан аккаунт.")
                return json.dumps({"status": 2007, "user_id": str(NewUserID)})

            else:
                Log.Save("[CheckPay.py | ИНФОРМАЦИЯ] > Аккаунт уже выдавался ранее.")
                return json.dumps({"status": 2008})
    
        else:
            continue

    Log.Save("[CheckPay.py | ИНФОРМАЦИЯ] > Оплата не прошла.")
    return json.dumps({"status": 2009})
