import Tool.Data.ModuleSQLite as ModuleSQLite
import Tool.Service.GetDateTime as GetDateTime
import random


def Comment():
    while (True):
        RandomComment = random.randint(1111111111, 9999999999)

        if (not ModuleSQLite.Request(f"SELECT Value FROM NotValidComments WHERE Value = '{RandomComment}'")):
            if (not ModuleSQLite.Request(f"SELECT Comment FROM Users WHERE Comment = '{RandomComment}'")):
                ModuleSQLite.Request(f"INSERT INTO NotValidComments (Value, BeginTime) VALUES ('{RandomComment}', '{GetDateTime.ThisTime()}')")
                
                return str(RandomComment)


def UserID():
    while (True):
        RandomUserID = random.randint(1111111111111111111111111, 9999999999999999999999999)

        if (not ModuleSQLite.Request(f"SELECT UserID FROM Users WHERE UserID = '{RandomUserID}'")):
            return str(RandomUserID)