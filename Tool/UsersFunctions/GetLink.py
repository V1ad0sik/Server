import Tool.Data.ModuleJSON as ModuleJSON
import Tool.Service.Log as Log
import json


def GetLink():
    Link = ModuleJSON.ReadConfig("Pay")["Link"]
    Name = ModuleJSON.ReadConfig("Pay")["Name"]
    Price = str(ModuleJSON.ReadConfig("Pay")["Price"])

    Link = Link.replace("NAME", Name).replace("PRICE", Price)

    Log.Save("[GetLink.py | ИНФОРМАЦИЯ] > Была выдана ссылка на оплату.")
    return json.dumps({"link": Link})