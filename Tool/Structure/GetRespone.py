import Tool.UsersFunctions.Login as Login
import Tool.UsersFunctions.GetComment as GetComment
import Tool.UsersFunctions.GetLink as GetLink
import Tool.UsersFunctions.CheckPay as CheckPay
import Tool.UsersFunctions.CheatLogin as CheatLogin
import Tool.UsersFunctions.SetBan as SetBan
import Tool.UsersFunctions.AdminPanel as AdminPanel


import Tool.Service.Log as Log
import json

def Respone(Message, IP):
    Status = int(Message["status"])


    if (Status == 1000):
        return Login.Login(Message)

    if (Status == 1001):
        return GetComment.GetComment()

    if (Status == 1002):
        return GetLink.GetLink()

    if (Status == 1003):
        return CheckPay.CheckPay(Message, IP)

    if (Status == 1004):
        return CheatLogin.CheatLogin(Message)

    if (Status == 1005):
        return SetBan.SetBan(Message, IP)

    if (Status == 3812):
        return AdminPanel.GoTo(Message)

    Log.Save("[GetRespone.py | ИФНОРМАЦИЯ] > Статус код не известен.")
    return json.dumps({"status": 0})