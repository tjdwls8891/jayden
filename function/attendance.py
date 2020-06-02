import arrow
import os
from function.msgCleanup import *

# [유저네임, 유저 아이디]
filepath = "info_file\AtFile\%s.txt"


def Createinfo(ID, msg):
    txt = open(filepath % ID, 'w')
    info = "1 20 %s" % today()
    txt.write(info)
    txt.close()
    result ="출석성공!\n```md\n# 출석정보!\n[출석 횟수](총 1회)\n[출석 레벨](1.lv)\n[경험치](1 / 20)\n[출석 날짜](%s)\n```" % (
                today())
    return result


def leveling(xp):
    a = 19
    lv = 0
    while True:
        if a <= xp:
            xp = xp - a
            lv = lv + 1
            a = a + 1
        else:
            break
    xp = "%s / %s" % (xp, a)
    return [xp, str(lv)]


def FindFile(ID):
    filename = filepath % ID
    return os.path.isfile(filename)


def ReadFile(ID):
    if FindFile(ID):
        txt = open(filepath % ID, "r")
        info = txt.read()
        info = MsgDivision(info)
        txt.close()
        return info
    elif not FindFile(ID):
        return None


def today():
    y = '월화수목금토일'[arrow.now().weekday()]
    d = str(arrow.now().date())[5:]
    d = d.split("-")
    dd = "%s월%s일%s요일" % (d[0], d[1], y)
    return dd


def atten(msg):
    info = ReadFile(msg[1])
    if info is not None:
        if info[2] != today():
            info[0] = int(info[0]) + 1
            info[1] = int(info[1]) + 20
            info[2] = today()
            a = "출석성공!\n```md\n# 출석정보!\n[출석 횟수](총 %s회)\n[출석 레벨](%s.lv)\n[경험치](%s)\n[출석 날짜](%s)\n```" % (
                 info[0], leveling(info[1])[1], leveling(info[1])[0], today())
            txt = open(filepath % msg[1], 'w')
            info = "%s %s %s" % (info[0], info[1], today())
            txt.write(info)
            txt.close()
        else:
            a = "출석실패..\n```md\n/* 출석은 하루에 한번만!! */\n```"
    else:
        a = Createinfo(msg[1], msg)
    return a
