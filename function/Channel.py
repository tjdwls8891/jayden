import os

filepath = "D:/디코봇/jayden/info_file/SvFile/%s.txt"


def Channel(ID, gID):
    txt = open(filepath % gID, "w")
    txt.write(str(ID))
    txt.close()
