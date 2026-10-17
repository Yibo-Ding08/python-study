import random
num=random.randint(1,100)
num2=0
while True:
    num1=int(input("请输入猜的数字:"))
    num2+=1
    if num1==num:
        print("猜对了")
        print(f"一共猜了{num2}次")
        break
    elif num1>num:
        print("猜大了")
    else:
        print("猜小了")
  

