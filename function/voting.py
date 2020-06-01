from random import sample
from function.msgCleanup import *

# !투표 제이지는 왜 심심한가?/ 그냥 그냥 그냥 그냥
def voting(msg):
    msgn = msg.split("/")
    title = msgn[0][4:]
    mat = msgn[1].split(" ")
    return [title, mat]


def text(vvv):
    a = "```md\n# %s\n" % vvv[0]
    b = ""
    c = 1
    for i in vvv[1]:
        b = b + "%s. %s\n" % (str(c), i)
        c = c + 1
    a = a + b + "```"
    return [a, c - 1]


def main(message, vot_msg_ID, user_dis, user_men):
    FilePath = "D:\디코봇\제이든\info_file\VoFile\%s.txt"
    re = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    if message.content[4:6] != "종료":
        vot_info = voting(message)
        embed = discord.Embed(description=text(message)[0])
        embed.set_author(name=message.author.name + "#" + message.author.discriminator,
                         icon_url=message.author.avatar_url)
        embed.set_footer(text="아래 번호를 클릭해 투표하세요!")
        message.channel.send(embed=embed)
        id = message.channel.last_message_id
        m = message.channel.fetch_message(id)
        for i in range(0, int(text(message)[1])):
            m.add_reaction(re[i])
        userment = message.author.mention
        code = "`%s`" % listlink(sample('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890', 10))
        anGup = "%s님, 투표 종료 코드는 %s 입니다." % (userment, code)
        message.channel.send(anGup)
