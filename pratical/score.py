while True:
    score1=input("请输入分数:")
    try:
        score=int(score1)
    except ValueError:
        print("请输入数字")
    if 90<=score<=100:
        print("A")
        break
    elif 80<=score<=89:
        print("B")
        break
    elif 70<=score<=79:
        print("C")
        break
    elif 60<=score<=69:
        print("D")
        break
    elif 0<=score<=59:
        print("F")
        break
    else:
        print("输入格式不对,请重新输入")
