import Tool.Service.Log as Log
import time, threading, collections

IP_List = []
TimeErrorList = []

maxRequest = 8
timeOut = 3


def SpamDef(IP):
    IP = str(IP)
    IP_List.append(IP)

    IP_Count = IP_List.count(IP)

    if (IP_Count > maxRequest):
        Log.Save(f"[Defender.py | ИНФОРМАЦИЯ] > IP: {IP} был заблокирован, из-за большого количества запросов.")
        return False

    else:
        return True
        

def CheackTimeOut(IP):
    IP = str(IP)
    IP_Count = TimeErrorList.count(IP)

    if (IP_Count > 3):
        return False

    else:
        return True


def TimeOutDef(IP):
    IP = str(IP)
    TimeErrorList.append(IP)

    IP_Count = TimeErrorList.count(IP)

    if (IP_Count > 3):
        Log.Save(f"[Defender.py | ИНФОРМАЦИЯ] > IP: {IP} был заблокирован, из-за длительных соединений.")
        return False

    else:
        return True


def IP_LiseClear():
    while (True):
        IP_List.clear()
        time.sleep(60)


def TimeErrorListClear():
    while (True):
        TimeErrorList.clear()
        time.sleep(240)


def CheckIP_ListCount():
    global maxRequest

    while (True):
        IP_ListCount = len(collections.Counter(IP_List).keys())

        if (IP_ListCount > 20):
            if (maxRequest != 2):
                Log.Save(f"[Defender.py | ИНФОРМАЦИЯ] > Количество запросов превысило 20, максимальное количество запросов - 2")
                maxRequest = 2


        if (IP_ListCount < 20 and IP_ListCount > 10):
            if (maxRequest != 6):
                Log.Save(f"[Defender.py | ИНФОРМАЦИЯ] > Количество запросов превысило 10, максимальное количество запросов - 4")
                maxRequest = 4

        
        if (IP_ListCount < 10):
            if (maxRequest != 8):
                Log.Save(f"[Defender.py | ИНФОРМАЦИЯ] > Количество запросов меньше 10, максимальное количество запросов - 8")
                maxRequest = 8


        time.sleep(5)


def CheckTimeErrorListCount():
    global timeOut

    IP_Count = len(collections.Counter(TimeErrorList).keys())

    if (IP_Count > 10):
        if (timeOut != 1):
            Log.Save(f"[Defender.py | ИНФОРМАЦИЯ] > Количество заблокированных timeOut превысило 10, максимальное время подключения - 1")
            timeOut = 1

    if (IP_Count < 10 and IP_Count > 5):
        if (timeOut != 2):
            Log.Save(f"[Defender.py | ИНФОРМАЦИЯ] > Количество заблокированных timeOut превысило 5, максимальное время подключения - 2")
            timeOut = 2


    if (IP_Count < 5):
        if (timeOut != 3):
            Log.Save(f"[Defender.py | ИНФОРМАЦИЯ] > Количество заблокированных timeOut менее 5, максимальное время подключения - 3")
            timeOut = 3


    time.sleep(5)


threading.Thread(target = IP_LiseClear).start()
threading.Thread(target = CheckIP_ListCount).start()

threading.Thread(target = TimeErrorListClear).start()
threading.Thread(target = CheckTimeErrorListCount).start()