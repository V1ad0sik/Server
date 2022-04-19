import Tool.Service.Log as Log
import sqlite3, os.path

def Request(Request):
    FileName = "Data/Base.db"

    if (os.path.exists(FileName)):
        with sqlite3.connect(FileName) as FileConnect:
            MethodCursor = FileConnect.cursor()
            MethodCursor.execute(Request)

            return MethodCursor.fetchall()

    else:
        Log.Save("[moduleSQLite.py | ОШИБКА] > Файл БД не найден.")
        return False


def RequestOne(Request):
    FileName = "Data/Base.db"

    if (os.path.exists(FileName)):
        with sqlite3.connect(FileName) as FileConnect:
            MethodCursor = FileConnect.cursor()
            MethodCursor.execute(Request)

            return MethodCursor.fetchall()[0][0]

    else:
        Log.Save("[moduleSQLite.py | ОШИБКА] > Файл БД не найден.")
        return False