from function.msgCleanup import *

def yon(a):
    a = listlink(MsgDivision(a))
    return a


def Study(a):
    a = a[4:].split("/")
    txt = open("D:\디코봇\jayden\info_file\colist.txt", 'a')
    jeyg = a[0] + ">" + a[1] + "\n"
    txt.write(jeyg)
    txt.close()
    return "삐릭! 학습완료!"


def Talk(a):
    a = a[4:]
    txt = open("D:\디코봇\jayden\info_file\colist.txt", "r")
    while True:
        rd = txt.readline()
        rd = rd.split(">")
        if rd[0] == a:
            txt.close()
            return rd[1]
        elif rd == [""]:
            txt.close()
            return "모르는 단어다!"
