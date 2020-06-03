# 라이브러리 임포트
import math
from random import *
import os
import arrow
import discord

# 디스코드 클라이언트 정의
client = discord.Client()

# 정보를 저장할 딕셔너리 정의
Co_list = {'안녕': '안넝!', '하잉': '하이잉!', '이름뭐얌': '예아 암 제이든!', '안넝': '안너엉!', '안녀엉': '안눙안눙~', '안눙': '안눙안눙!',
           '후아유!': '암 제이든!', '하이': '하잉!', '하위': '하위하위', '제이지는': '심심하다', '제이든은': '제이든이다!', '코카콜라': '북극곰!!',
           '너뭐해': '힐링중이징ㅎㅎ', '비트박스해줘': '시러...안할거야...빼액', '제이든': '마자 나 제이든이야!', '제이지는지금': '인강듣는중.', '저리가': '아라쓰...',
           '사랑해': '미안..받아줄 수 없써!!', '사귀자': '앗 나는 자웅동ㅊ(웁웁)', '밥줘': '뭐 좋아하는뎅??', '놀자': '머할래?', '뭐해': '힐링!',
           '이든아': '왜불렁!!', '잘자': '웅 잘장', '닥쳐': '...ㅠㅠ', '심심해': '나랑 놀자!', '이리와': '구랭', '맘마먹자': '뭐 주려고?? 난 아무거나 안머거!',
           '나좋아?': '웅ㅎㅎ', '나잘생겼지?': '웅 완전 존잘', '아이패드프로사줘': '달팽이 돈없어..', '에플펜슬사줘': '달팽이한테 뭘 바래!',
           '나랑사귀자': '나는 자웅동체라니ㄲ(웁웁웁)', '너착해': '고마웡ㅎㅎㅎㅎ', '머꼬': '아무것두아니얌ㅎㅎ', '잘했어': '고마웡 히힣', '뒤져': '너... 쒸익쒸익.. 나빴어!',
           'ㅎㅇ': '하이하이!!', '올만이야': '보고싶었오...!', '똑똑하네': '더 가르쳐줭!!', '잘가': '안갈끄야ㅠㅠ', '착해': '고마웡', '안녕 뭐해': '나 힐링중!',
           '고마워': 'It’s nothing!!', '안냥': '안냥안냥', '고 마 워': '나 도 고 마 워!!', '내가왔어': '언넝 이것저것 알려줭!!', '뭐해?': '힐링중!',
           '나 심심해': '뭐하고 놀아주까아?', '심심해?': '난 갠차나!! 네가 왔자나!!', '안녕?': '안넝!! 반가워!!!', '무슨게임해?': '나 달리기 좋아해! 달팽이도 빨라!!',
           '열공했어?': '아직 더 해야됌..', '나와': '좀만 기다려!! 금방갈게!!(꼬물꼬물)', '나뻐': '허어어 미안해!!', '나오지마': '시러!!(꼬물꼬물)', '왔어': '어서왕!!',
           '빠빠': '가지마아ㅏㅏ', 'ㅏㅏ': '왜ㅐㅐ', '맞지?': '마저마저', '반가워': '나도 반가버!', '손': '잉?? 난 달팽ㅇㅣ..', '발': '난 달팽이라니까!!',
           '가': '너무해ㅠ흙흙', '할게 없다': '나랑 놀자!!', '아라라라': '아라ㅏㅏ'}
At_info = {}  # 출석정보
En_info = {}  # 강화 아이템 정보
Lv_info = {}  # 레벨 정보

# 전역변수
cha = ""  # 백업채널


# 단어를 학습시키는 함수
# !학습 (입력)/(출력)
def learning_words(msg):
    msg = msg[4:].split("/")
    Co_list[msg[0]] = msg[1]
    return "삐릭! 학습완료!"


# 단어를 받고 말하는 함수
# 이든아 (입력)
def word_speaking(msg):
    msg = msg[4:]
    if msg in Co_list:
        ans = Co_list.get(msg)
        return ans
    else:
        return "모르는 단어다!"


# 암호를 만드는 함수
def secret_code(origin, key):
    code_list = []
    for let in origin:
        sec_code = int(ord(let)) * int(key)
        for num in range(0, len(str(sec_code)), 3):
            code_list.append(chr(int("1" + str(sec_code)[num:num + 3])))
        code_list.append("!")
    result = "```" + connect_letters(code_list) + "```"
    return result


# 암호를 해독하는 함수
def decryption(sec_code, key):
    original_number = ""
    original_letter = []
    for let in sec_code:
        if let != "!":
            original_number = original_number + str(ord(let))[1:]
        elif let == "!":
            original_letter.append(chr(int(original_number.strip()) // int(key)))
            original_number = ""
    result = "```" + connect_letters(original_letter) + "```"
    return result


# 암호관련 함수를 관리하는 함수
# !암호 (생성/해독) (원문/암호문) (2이상의 정수)
def code(a):
    if a[1] == "생성":
        return secret_code(a[2], a[3])
    elif a[1] == "해독":
        return decryption(a[2], a[3])


# 문자열을 공백으로 나눈 리스트를 만드는 함수
def text_splitting(msg):
    msg.strip()
    msg_list = msg.split(" ")
    return msg_list


# 리스트를 한 문자열로 이어주는 함수
def connect_letters(letter_list):
    a = ""
    for i in letter_list:
        a = a + i
    return a


# 경험치로 레벨을 계산하는 함수
def get_levels(ex):
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


# 입력받은 메시지로 레벨 정보를 갱신하고 레벨이 오르면 문자열을 리턴하는 함수
def leveling(user_id, msg):
    if user_id != "681087205912870963":
        number_of_letters = len(msg)
        if not user_id in Lv_info:
            Lv_info[user_id] = "1 0"
            return " `레벨 1`을 달성하셨습니다!"
        else:
            info = Lv_info.get(user_id).split(" ")
            previous_level = info[0]
            ex = int(info[1]) + number_of_letters
            lv = get_levels(ex)
            info = "%s %s" % (lv, ex)
            Lv_info[user_id] = info
            if int(previous_level) != int(lv):
                info = " `레벨 %s`을 달성하셨습니다!" % lv
                return info
            else:
                return None


# 유저 아이디로 레벨, 경험치, 경험치바를 얻는 함수
# !레벨
def get_level_information(user_id):
    info = Lv_info.get(user_id).split(" ")
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
    return info[0], info[1], a


# 받은 키워드에 따라 이모티콘을 리턴하는 함수
# !임티 (키워드)
def emoticon(key):
    if key == "인사":
        return "(ㅇㅅㅇ)7\n(ㅇㅅㅇ)/"
    elif key == "상엎기":
        return "(    ㅇㅅㅇ） ┬─┬ \n(╯ㅇㅅㅇ）╯︵ ┻━┻"
    elif key == "상두기":
        return ".                  (ㅇㅅㅇ    )\n┬─┬ ノ(ㅇㅅㅇノ)"
    elif key == "상겹치기":
        return ".                           ︵┻━┻\n(╯ㅇㅅㅇ）╯    ┬─┬ ノ(ㅇㅅㅇノ)"
    elif key == "상두고엎기":
        return ".                  (ㅇㅅㅇ    )(    ㅇㅅㅇ） ┬─┬ \n┬─┬ ノ(ㅇㅅㅇノ)(╯ㅇㅅㅇ）╯︵ ┻━┻"
    elif key == "상두는데엎기":
        return "(    ㅇㅅㅇ）                    (ㅇㅅㅇ    ) \n(    ㅇㅅㅇ） ┬─┬ ノ(ㅇㅅㅇノ) " \
               "\n                                      ︵ ︵┻━┻\n(╯ㅇㅅㅇ）╯︵ ︵  ノ(ㅇㅅㅇノ)"
    elif key == "파이팅":
        return "(ㅇㅅㅇ)/\n(ㅇㅅㅇ)V"
    elif key == "위협":
        return ".(ㅇㅅㅇ)\nr(ㅇㅅㅇ)r"
    else:
        return "존재하지 않는 임티!"


# 아이템이 없을 때 아이템을 생성하는 함수
def create_item(item, user_id):
    En_info[user_id] = "%s 1" % item
    result = "🎉아이템 제작에 성공했습니다!   `" + item + "`   lv.0  ➡  lv.1🆙"
    return result


# 아이템의 레벨을 임의로 결정하고 문자열을 리턴하는 함수
def item_upgrade(item, lv, user_id):
    probability = 50 + (50 - math.ceil(int(lv) / 5))
    random_number = randint(1, 100)
    if random_number <= probability:
        level = int(lv) + randint(1, 9)
        level_difference = level - int(lv)
        En_info[user_id] = "%s %s" % (item, level)
        msg = "🎉아이템 강화에 성공했습니다! `%s` lv.%s  ➡  lv.%s🆙 \n" \
              "`%s` 레벨 상승! \n강화 성공확률 : `%s 퍼센트`" % (item, lv, level, level_difference, probability)
        return msg
    elif random_number > probability:
        falling_level = randint(0, int(lv) // 8)
        if falling_level != 0:
            level = int(lv) - falling_level
            level_difference = int(lv) - level
            En_info[user_id] = "%s %s" % (item, level)
            msg = "⛈️아이템 강화에 실패했습니다! `%s` lv.%s  ➡  lv.%s⬇️\n" \
                  "`%s` 레벨 하락... \n강화 성공확률 : `%s 퍼센트`" % (item, lv, level, level_difference, probability)
            return msg
        elif falling_level == 0:
            if randint(1, 5) == 1:
                En_info[user_id] = "%s %s" % (item, str(lv + 100))
                msg = '🎉🎉미친 확률을 뚫고 레벨을 복구하는 도중에 \n🎉🎉우연히 아이템이 각성합니다!!!!!! `%s` lv.%s  ➡  lv.%s🎉🎉 ' \
                      '\n`100` 레벨 상승! \n강화 성공확률 : `%s 퍼센트`' % (item, lv, int(lv) + 100, probability)

                return msg
            msg = "🌈미친 확률을 뚫고 레벨을 복구했습니다! `%s` lv.%s↕️️\n레벨 유지! \n강화 성공확률 : `%s 퍼센트`" % (item, lv, probability)
            return msg


# 아이템의 존재 여부를 확인하고 처리하는 함수
# !강화 (아이템)
def enhance(msg, user_id):
    if user_id in En_info:
        info = En_info.get(user_id).split(" ")
        if msg[1] == info[0]:
            return item_upgrade(msg[1], info[1], user_id)
        elif msg[1] != info[0]:
            return "강화는 1가지만 가능합니다! 키워드를 바꾸려면 제이든에게 문의하세요!"
    else:
        return create_item(msg[1], user_id)


# 키와 몸무게로 비만도를 계산하는 함수
# !비만도 (키) (몸무게)
def bmi(a):
    height = int(a[1])
    weight = int(a[2])
    the_bmi = float(str((weight / (height * height)) * 10000)[:4])
    if the_bmi < 18.5:
        msg = "`저체중`입니다!"
    elif the_bmi < 25:
        msg = "`정상체중`입니다!"
    elif the_bmi < 30:
        msg = "`과체중`입니다!"
    else:
        msg = "`비만`입니다!!"
    the_bmi = "BMI : `" + str(the_bmi) + "`"
    result = the_bmi + "\n" + msg
    return result


# 유저의 아이디로 출석정보를 출력하는 함수
def creating_attendance_information(user_id):
    At_info[user_id] = "1 20 %s" % today()
    result = "출석성공!\n```md\n# 출석정보!\n[출석 횟수](총 1회)\n[출석 레벨](1.lv)\n[경험치](1 / 20)\n[출석 날짜](%s)\n```" % (
        today())
    return result


# 경험치로 출석 레벨과 경험치바를 계산하는 함수
def get_at_levels(xp):
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


# 날짜와 요일을 한글로 출력하는 함수
def today():
    y = '월화수목금토일'[arrow.now().weekday()]
    d = str(arrow.now().date())[5:]
    d = d.split("-")
    dd = "%s월%s일%s요일" % (d[0], d[1], y)
    return dd


# 출석함수
def attendance(user_id):
    if user_id in At_info:
        info = At_info.get(user_id)
        if info[2] != today():
            info[0] = int(info[0]) + 1
            info[1] = int(info[1]) + 20
            info[2] = today()
            a = "출석성공!\n```md\n# 출석정보!\n[출석 횟수](총 %s회)\n[출석 레벨](%s.lv)\n[경험치](%s)\n[출석 날짜](%s)\n```" % (
                info[0], get_at_levels(info[1])[1], get_at_levels(info[1])[0], today())
            At_info[user_id] = "%s %s %s" % (info[0], info[1], today())
        else:
            a = "출석실패..\n```md\n/* 출석은 하루에 한번만!! */\n```"
    else:
        a = creating_attendance_information(user_id)
    return a


# 봇이 준비됐을 때 호출되는 이벤트
@client.event
async def on_ready():
    # 봇 준비 시 메시지
    print("bot ready.\nBot code : Jayden")
    # 온라인 상태와 게임 메시지 설정
    game = discord.Game("땅굴속에서 힐링")
    await client.change_presence(status=discord.Status.online, activity=game)


# 메시지가 보내졌을 때 호출되는 이벤트
@client.event
async def on_message(message):
    # 메시지를 보낸 사람이 봇인지 확인하고 레벨에 반영
    if not message.author.bot:
        level_msg = leveling(message.author.id, message.content)
        if level_msg is not None:
            result = message.author.mention + level_msg
            await message.channel.send(result)

    # 서버 정보 출력 함수
    if message.content.startswith("!서버"):
        time = str(message.guild.created_at)
        time = "%s년 %s월 %s일" % (time[:4], time[5:7], time[8:10])
        result = "```md\n- 서버 이름: %s\n- 관리자: %s\n- 아이디: %s\n- 생일: %s\n```" % \
                 (message.guild.name, message.guild.owner.name, message.guild.id, time)
        await message.channel.send(result)

    # 테스트용 함수
    if message.content.startswith("!테스트"):
        await message.channel.send("테스트")

    # 단어학습 함수
    if message.content.startswith("!학습"):
        await message.channel.send(learning_words(message.content))

    # 단어출력 함수
    if message.content.startswith("이든아 "):
        await message.channel.send(word_speaking(message.content))

    # 비만도 계산 함수
    if message.content.startswith("!비만도"):
        msg_list = text_splitting(message.content)
        await message.channel.send(bmi(msg_list))

    # 암호 생성/해독 함수
    if message.content.startswith("!암호"):
        msg_list = text_splitting(message.content)
        await message.channel.send(code(msg_list))

    # 이모티콘 출력 함수
    if message.content.startswith("!임티"):
        msg = text_splitting(message.content)
        await message.channel.send(emoticon(msg[1]))

    # 봇 초대 링크 출력 함수
    if message.content.startswith("!초대"):
        await message.channel.send("https://discordapp.com/oauth2/authorize?client_id=681087205912870963&scope=bot")

    # 유저 레벨 정보 출력 함수
    if message.content.startswith("!레벨"):
        exp = get_level_information(message.author.id)
        embed = discord.Embed(description="```md\n- lv.%s\n- ex : %s / %s\n```"
                                          % (exp[0], exp[1], exp[2]), color=0x00ff56)
        embed.set_author(name=message.author.name + "#" + message.author.discriminator,
                         icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    # 아이템 강화 함수
    if message.content.startswith("!강화"):
        msg = text_splitting(message.content)
        user_id = message.author.id
        embed = discord.Embed(title='강화 결과', description=enhance(msg, user_id), color=0x00ff56)
        await message.channel.send(embed=embed)

    # 출석함수
    if message.content.startswith("!출석"):
        embed = discord.Embed(description=attendance(message.author.id), color=0x00ff56)
        await message.channel.send(embed=embed)

    # 개인 디엠을 통한 암호 생성/해독 함수
    if message.content.startswith("!비밀암호"):
        user = message.guild.get_member(message.author.id)
        await user.send("```\n서버 채널에 공개할 암호가 아니라면 이곳에\n !암호 생성 (원하는 문장이나 단어) (2~5정도의 숫자)\n를 입력해 주세요. \n !암호 해독 "
                        "(암호문) (생성할 때 사용한 숫자) \n 로 해독 가능합니다.\n```")

    # 백업 채널을 정하는 함수
    access_backup_channel = os.environ["INFO_BACKUP_CHANNEL"]
    if message.content.startswith(access_backup_channel):
        global cha
        cha = message.channel

    # 백업 채널에 변하는 정보를 백업하는 함수
    access_backup = os.environ["INFO_BACKUP"]
    if message.content.startswith(access_backup):
        backup_file = "```md\nCo_list : %s\nAt_info : %s\nEn_info : %s\nLv_info : %s" % (Co_list, At_info, En_info, Lv_info)
        embed = discord.Embed(decryption=backup_file)
        await cha.send(embed=embed)


# 봇 토큰
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
