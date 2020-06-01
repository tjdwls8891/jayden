def BMI(a):
    height = int(a[1])
    weight = int(a[2])
    bmifig = float(str((weight / (height * height)) * 10000)[:4])
    if bmifig < 18.5:
        msg = "`저체중`입니다!"
    elif bmifig < 25:
        msg = "`정상체중`입니다!"
    elif bmifig < 30:
        msg = "`과체중`입니다!"
    else:
        msg = "`비만`입니다!!"
    bmifig = "BMI : `" + str(bmifig) + "`"
    result = bmifig + "\n" + msg
    return result
