try:
    print("--------------------------------")
    print(1/0)
    print("abv"[100])
    print("==================================")
except ZeroDivisionError as e:
    print("除零错误:", e)
except IndexError as e:
    print("索引错误:", e)
except NameError as e:
    print("变量未定义:", e)
