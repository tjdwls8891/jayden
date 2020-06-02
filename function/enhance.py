from function.msgCleanup import *
import os
from random import *
from math import *


filepath = "info_file/EnFile/%s.txt"


def CreateItem(item, ID):
    txt = open(filepath % ID, 'w')
    info = item + " 1"
    txt.write(info)
    txt.close()
    result = "🎉아이템 제작에 성공했습니다!   `" + item + "`   lv.0  ➡  lv.1🆙"
    return result


def Enhance(msg, userID):
    info = ReadFile(userID)
    ReadFile(userID)
    if info is not None:
        if msg[1] == info[0]:
            return ItemUpgrade(msg[1], info[1], userID)
        elif msg[1] != info[0]:
            return "강화는 1가지만 가능합니다! 키워드를 바꾸려면 제이든에게 문의하세요!"
    elif info is None:
        return CreateItem(msg[1], userID)


def ReadFile(ID):
    if os.path.isfile(filepath % ID):
        txt = open(filepath % ID, "r")
        info = txt.read()
        info = MsgDivision(info)
        txt.close()
        return info
    else:
        return None


def ItemUpgrade(item, lv, ID):
    prob = 50 + (50 - ceil(int(lv) / 5))
    randomnum = randint(1, 100)
    if randomnum <= prob:
        txt = open(filepath % ID, "r")
        info = MsgDivision(str(txt.read()))
        txt.close()
        afterlv = int(info[1]) + randint(1, 9)
        Lvdiff = afterlv - int(info[1])
        msg = "🎉아이템 강화에 성공했습니다! `%s` lv.%s  ➡  lv.%s🆙 \n" \
              "`%s` 레벨 상승! \n강화 성공확률 : `%s 퍼센트`" % (item, info[1], afterlv, Lvdiff, prob)
        txt = open(filepath % ID, "w")
        jeyg = item + " " + str(afterlv)
        txt.write(jeyg)
        txt.close()
        return msg
    elif randomnum > prob:
        txt = open(filepath % ID, "r")
        info = txt.read()
        txt.close()
        info = MsgDivision(str(info))
        declv = randint(0, int(lv) // 8)
        if declv != 0:
            afterlv = int(info[1]) - declv
            Lvdiff = int(info[1]) - afterlv
            msg = "⛈️아이템 강화에 실패했습니다! `%s` lv.%s  ➡  lv.%s⬇️\n" \
                  "`%s` 레벨 하락... \n강화 성공확률 : `%s 퍼센트`" % (item, info[1], afterlv, Lvdiff, prob)
            txt = open(filepath % ID, "w")
            jeyg = item + " " + str(afterlv)
            txt.write(jeyg)
            txt.close()
            return msg
        elif declv == 0:
            if randint(1, 5) == 1:
                msg = '🎉🎉미친 확률을 뚫고 레벨을 복구하는 도중에 \n🎉🎉우연히 아이템이 각성합니다!!!!!! `%s` lv.%s  ➡  lv.%s🎉🎉 ' \
                      '\n`100` 레벨 상승!!! \n강화 성공확률 : `%s 퍼센트`' % (item, info[1], int(info[1]) + 100, prob)
                txt = open(filepath % ID, "w")
                jeyg = item + " " + str(info[1] + 100)
                txt.write(jeyg)
                txt.close()
                return msg
            msg = "🌈미친 확률을 뚫고 레벨을 복구했습니다! `%s` lv.%s↕️️\n레벨 유지! \n강화 성공확률 : `%s 퍼센트`" % (item, info[1], prob)
            return msg
