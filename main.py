from function.Import import *
import discord

client = discord.Client()
svfilepath = "info_file/SvFile/%s.txt"


@client.event
async def on_ready():
    print("bot ready.\nBot code : Jayden")
    game = discord.Game("땅굴속에서 힐링")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_member_join(member):
    if os.path.isfile(svfilepath % member.guild.id):
        a = "%s님께서 입장하셨습니다!" % member.name
        txt = open(svfilepath % member.guild.id, "r")
        b = txt.read()
        txt.close()
        cha = member.guild.get_channel(int(b))
        await cha.send(a)


@client.event
async def on_member_remove(member):
    if os.path.isfile(svfilepath % member.guild.id):
        a = "%s님께서 퇴장하셨습니다..." % member.name
        txt = open(svfilepath % member.guild.id, "r")
        b = txt.read()
        txt.close()
        cha = member.guild.get_channel(int(b))
        await cha.send(a)


@client.event
async def on_message(message):
    if not message.author.bot:
        a = RoadingLeveling(message.author.id, message.content)
        if a is not None:
            b = message.author.mention + a
            await message.channel.send(b)

    if message.content.startswith("!입퇴장"):
        if message.guild.owner.id == message.author.id:
            Channel(message.channel.id, message.guild.id)
            await message.channel.send("설정 완료!")
        else:
            await message.channel.send("이 명령어는 서버의 오너만 사용 가능합니다!")

    if message.content.startswith("!서버"):
        time = str(message.guild.created_at)
        if int(time[11:13]) < 12:
            a = "오전"
        else:
            a = "오후"
            time[11:13] = int(time[11:13]) - 12
        ttime = "%s년 %s월 %s일 %s %s:%s" % (time[:4], time[5:7], time[8:10], a, time[11:13], time[14:16])
        txt = "```md\n- 서버 이름: %s\n- 관리자: %s\n- 아이디: %s\n- 생일: %s\n```" % \
              (message.guild.name, message.guild.owner.name, message.guild.id, ttime)
        await message.channel.send(txt)

    if message.content.startswith("!테스트"):
        await message.channel.send("테스트")

    if message.content.startswith("!학습"):
        await message.channel.send(Study(message.content))

    if message.content.startswith("이든아 "):
        await message.channel.send(Talk(message.content))

    if message.content.startswith("!비만도"):
        msglist = MsgDivision(message.content)
        await message.channel.send(BMI(msglist))

    if message.content.startswith("!암호"):
        msglist = MsgDivision(message.content)
        await message.channel.send(Code(msglist))

    if message.content.startswith("!임티"):
        msg = MsgDivision(message.content)
        await message.channel.send(Imti(msg[1]))

    if message.content.startswith("!초대"):
        await message.channel.send("https://discordapp.com/oauth2/authorize?client_id=681087205912870963&scope=bot")

    if message.content.startswith("!레벨"):
        a = LevelChecking(message.author.id)
        b = ExChecking(message.author.id)[0]
        c = ExChecking(message.author.id)[1]
        embed = discord.Embed(description="```md\n- lv.%s\n- ex : %s / %s\n```" % (a, b, c), color=0x00ff56)
        embed.set_author(name=message.author.name + "#" + message.author.discriminator,
                         icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("!강화"):
        msg = MsgDivision(message.content)
        user_id = message.author.id
        embed = discord.Embed(title='강화 결과', description=Enhance(msg, user_id), color=0x00ff56)
        await message.channel.send(embed=embed)

    if message.content.startswith("!출석"):
        embed = discord.Embed(description=atten([message.author.name, message.author.id]), color=0x00ff56)
        await message.channel.send(embed=embed)

    if message.content.startswith("!비밀암호"):
        user = message.guild.get_member(message.author.id)
        await user.send("```\n서버 채널에 공개할 암호가 아니라면 이곳에\n !암호 생성 (원하는 문장이나 단어) (2~5정도의 숫자)\n를 입력해 주세요. \n !암호 해독 "
                                   "(암호문) (생성할 때 사용한 숫자) \n 로 해독 가능합니다.\n```")


@client.event
async def on_reaction_add(reaction):
    msgID = reaction.message.id
    FilePath = "D:\디코봇\제이든\VoFile\%s.txt"
    path = FilePath % msgID
    if os.path.isfile(path):
        voinfo = open(path, "a")
        # info = "/%s %s" % (reaction.author.mention, reaction.emoji)
        # voinfo.write(info)
        voinfo.close()

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
