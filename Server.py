import Tool.Service.GetDateTime as GetDateTime
import Tool.Service.Defender as Defender
import Tool.Service.Log as Log

import Tool.Structure.XOR as XOR
import Tool.Structure.JsonConvert as JsonConvert
import Tool.Structure.GetRespone as GetRespone
import Tool.Structure.CheckStruct as CheckStruct

import json, socket

print("> Server SECTOR [CS:GO] <")
print("- Время запуска: " + GetDateTime.ThisTime())
print("---------------------------------")


def Server():
    Server = socket.socket()

    Server.bind(("", 3390))
    Server.listen(Defender.timeOut)


    while (True):
        Cleint, ClientInfo = Server.accept()
        Cleint.settimeout(3)

        Log.Save("")

        IP = str(ClientInfo[0])
        Port = str(ClientInfo[1])

        if (Defender.SpamDef(IP) and Defender.CheackTimeOut(IP)):
            Log.Save(f"[ПОДКЛЮЧЕНИЕ] -> {IP} | {Port} | {GetDateTime.SubTime()}")

            try:
                Message = XOR.Decrypt(Cleint.recv(20971520).decode())

            except socket.timeout:
                Log.Save("[server.py | ОШИБКА] > Время подключения вышло.")
                Defender.TimeOutDef(IP)
                Cleint.close()

            except Exception as MessageExcept:
                Log.Save("[server.py | ОШИБКА] > " + str(MessageExcept))
                Cleint.close()

            
            Log.Save("[server.py | ЗАПРОС] > " + str(Message))


            if (JsonConvert.ToJson(Message)):
                try:
                    Message = json.loads(Message)

                except Exception as MessageExcept:
                    Log.Save("[server.py | ОШИБКА] > " + str(MessageExcept))
                    Cleint.close()

            
            if (CheckStruct.ReadStruct(Message)):
                try:
                    Cleint.send(XOR.Crypt(GetRespone.Respone(Message, IP)).encode())

                except Exception as MessageExcept:
                    Log.Save("[server.py | ОШИБКА] > " + str(MessageExcept))
                    Cleint.close()


        Log.Save("")
        Cleint.close()


while (True):
    try:
        Server()

    except Exception as MessageExcept:
        Log.Save("[server.py | ОШИБКА] > " + str(MessageExcept))