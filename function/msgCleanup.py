def MsgDivision(msg):
    msg.strip()
    msglist = msg.split(" ")
    return msglist


def listlink(Mlist):
    a = ""
    for i in Mlist:
        a = a + i
    return a


def MsgCleanUp(msg):
    msgs = msg[3:]
    msgs.strip()
