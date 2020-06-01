from function.msgCleanup import *


nextlet = "!"


def SecCode(origin, key):
    codelist = []
    for let in origin:
        seccodeuni = int(ord(let)) * int(key)
        for num in range(0, len(str(seccodeuni)), 3):
            codelist.append(chr(int("1" + str(seccodeuni)[num:num + 3])))
        codelist.append(nextlet)
    result = "```" + listlink(codelist) + "```"
    return result


def UnlCode(code, key):
    originnum = ""
    origintext = []
    for let in code:
        if let != nextlet:
            originnum = originnum + str(ord(let))[1:]
        elif let == nextlet:
            origintext.append(chr(int(originnum.strip()) // int(key)))
            originnum = ""
    result = "```" + listlink(origintext) + "```"
    return result


def Code(a):
    if a[1] == "생성":
        return SecCode(a[2], a[3])
    elif a[1] == "해독":
        return UnlCode(a[2], a[3])
