import os
import math
from function.msgCleanup import *
# info = [레벨] [총 글자수]

filepath = "D:/디코봇/jayden/info_file/LvFile/%s.txt"


def ReadFile(ID):
    if os.path.isfile(filepath % ID):
        txt = open(filepath % ID, "r")
        info = txt.read()
        info = MsgDivision(info)
        txt.close()
        return info
    else:
        return None


def leveling(ex):
    lv = 1
    a = 10
    while True:
        if ex < a:
            break
        ex = ex - a
        lv = lv + 1
        if lv < 10:
            a = math.ceil(a * 1.5)
        elif lv < 15:
            a = math.ceil(a * 1.3)
        elif lv < 20:
            a = math.ceil(a * 1.2)
        else:
            a = math.ceil(a * 1.1)
    return lv


def RoadingLeveling(user_id, msg):
    if user_id != "681087205912870963":
        num_of_let = len(msg)
        info = ReadFile(user_id)
        if not os.path.isfile(filepath % user_id):
            txt = open(filepath % user_id, 'w')
            info = "1 %s" % str(int(num_of_let) + 10)
            txt.write(info)
            txt.close()
            return " `레벨 1`을 달성하셨습니다!"
        else:
            befo = info[0]
            ex = int(info[1]) + num_of_let
            lv = leveling(ex)
            info = "%s %s" % (lv, ex)
            txt = open(filepath % user_id, 'w')
            txt.write(info)
            txt.close()
            if int(befo) != int(lv):
                info = " `레벨 %s`을 달성하셨습니다!" % lv
                return info
            else:
                return None


def LevelChecking(ID):
    txt = open(filepath % ID, "r")
    info = txt.read()
    info = MsgDivision(info)
    txt.close()
    return info[0]


def ExChecking(ID):
    txt = open(filepath % ID, "r")
    info = txt.read()
    info = MsgDivision(info)
    txt.close()
    lv = 1
    a = 10
    while True:
        if int(info[1]) < a:
            break
        info[1] = int(info[1]) - a
        lv = lv + 1
        if lv < 10:
            a = math.ceil(a * 1.5)
        elif lv < 15:
            a = math.ceil(a * 1.3)
        elif lv < 20:
            a = math.ceil(a * 1.2)
        else:
            a = math.ceil(a * 1.1)
    return info[1], a
