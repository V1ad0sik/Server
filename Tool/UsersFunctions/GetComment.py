import Tool.Service.Log as Log
import Tool.Service.GetRandomData as GetRandomData
import json


def GetComment():
    Log.Save("[GetComment.py | ИНФОРМАЦИЯ] > Был выдан комментарий к платежу.")
    return json.dumps({"comment": GetRandomData.Comment()})
