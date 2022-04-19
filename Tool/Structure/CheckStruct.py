import Tool.Service.Log as Log


def ReadStruct(Message):
    try:
        Status = int(Message["status"])

    except Exception as MessageExcept:
        Log.Save("[CheckStruct.py | ОШИБКА] > " + str(MessageExcept))
        return False

    
    if (Status == 1000):
        try:
            str(Message["user_id"]), str(Message["hwid"]), int(Message["version"])
            return True

        except Exception as MessageExcept:
            Log.Save("[CheckStruct.py | ОШИБКА] > " + str(MessageExcept))
            return False

    
    if (Status == 1001 or Status == 1002 or Status == 3812):
        return True


    if (Status == 1003):
        try:
            str(Message["comment"])
            return True

        except Exception as MessageExcept:
            Log.Save("[CheckStruct.py | ОШИБКА] > " + str(MessageExcept))
            return False


    if (Status == 1004):
        try:
            str(Message["user_id"]), str(Message["hwid"]), int(Message["version"])
            return True

        except Exception as MessageExcept:
            Log.Save("[CheckStruct.py | ОШИБКА] > " + str(MessageExcept))
            return False


    if (Status == 1005):
        try:
            str(Message["user_id"])
            return True

        except Exception as MessageExcept:
            Log.Save("[CheckStruct.py | ОШИБКА] > " + str(MessageExcept))
            return False
            

    return False