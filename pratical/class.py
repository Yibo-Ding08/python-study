from os import name


class Account:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def cunqian(self):
        tem=int(input("请输入存入的金额:"))
        self.money+=tem
        print("现存金额为:",self.money)
    def quqian(self):
        tem1=int(input("请输入取走的金额:"))
        if tem1>self.money:
            print("余额不足")
        else:
            self.money-=tem1
            print("余额为:",self.money)
a=Account("丁怡博",10000)
b=Account("王津",1000)
print("***************")
print("银行账户系统开放,功能如下")
print("""1.存钱\n2.取钱\n3.退出""")

while True:
    num=int(input("请选择功能:"))
    name1=input("请输入姓名:")
    match(num):
        case 1:
            if name1=="丁怡博":
                a.cunqian()
            elif name1=="王津":
                b.cunqian()
            else:
                print("无此人")
        case 2:
            if name1=="丁怡博":
                a.quqian()
            elif name1=="王津":
                b.quqian()
            else:
                print("无此人")
        case 3:
            break
        case _:
            print("请重新输入功能:")
    




