import datetime


def ThisTime():
    ThisData = datetime.datetime.now()
    ThisData = ThisData.strftime("%Y.%m.%d %H:%M")

    return ThisData


def DiffTime(UserTime):
    ThisDateObject = datetime.datetime.strptime(ThisTime(), "%Y.%m.%d %H:%M")
    UserDateObject = datetime.datetime.strptime(UserTime, "%Y.%m.%d %H:%M")

    return UserDateObject - ThisDateObject


def DiffTimeToHours(UserTime):
    return int(round(DiffTime(UserTime).total_seconds() / 3600, 1))


def DiffTimeToSecond(UserTime):
    return DiffTime(UserTime).total_seconds()


def SubTime():
    ThisDate = datetime.datetime.now() + datetime.timedelta(days = 30)

    return ThisDate.strftime("%Y.%m.%d %H:%M")