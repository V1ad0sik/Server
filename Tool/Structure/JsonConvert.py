import Tool.Service.Log as Log
import json


def ToJson(Message):
    try:
        Message = json.dumps(Message)

        if (("{" in Message) and ("}" in Message)):
            return True

        else:
            Log.Save("[JsonConvert.py | ОШИБКА] > Не были найдены '{' или '}' в структуре запроса.")
            return False

    except Exception as MessageExcept:
        Log.Save("[JsonConvert.py | ОШИБКА] > " + str(MessageExcept))
        return False