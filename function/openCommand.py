import os
from function.msgCleanup import *
# !커맨드 [요소] [채널]
# !서버등록

filepath = "D:/디코봇/jayden/info_file/SvFile/%s.txt"


def ReadFile(ID):
    if os.path.isfile(filepath % ID):
        txt = open(filepath % ID, "r")
        info = txt.read()
        info = MsgDivision(info)
        txt.close()
        return info
    else:
        return None
