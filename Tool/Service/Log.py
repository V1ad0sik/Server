import Tool.Service.GetDateTime as GetDataTime
import os.path


def Save(Message):
    print(Message)
    Path = "Data/Log.txt"

    if (not os.path.exists(Path)):
        File = open(Path, "w+")

    try:
        File = open(Path, "a", encoding = "utf-8")

        if (Message == ""):
            File.write("\n")

        else:
            File.write("\n" + f"[{GetDataTime.ThisTime()}] - {Message}")

        File.close()

    except Exception as MessageExcept:
        print("[Log.py | Ошибка] > " + str(MessageExcept))



def SaveBanLog(FileName, Message):
    Path = f"Data/BanList/{FileName}.txt"

    if (not os.path.exists(Path)):
        File = open(Path, "w+")

    try:
        File = open(Path, "a", encoding = "utf-8")
        File.write(Message)
        File.close()

    except Exception as MessageExcept:
        print("[Log.py | Ошибка] > " + str(MessageExcept))
