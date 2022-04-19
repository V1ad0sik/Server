import Tool.Service.Log as Log
import json, os.path


def ReadConfig(Point):
    FileName = "Data/Config.json"

    if (os.path.exists(FileName)):
        File = open(FileName, "r")
        Data = json.loads(File.read())
        File.close()

        return Data[Point]

    else:
        Log.Save("[moduleJSON.py | ОШИБКА] > Файл конфигурации не найден.")
        return False