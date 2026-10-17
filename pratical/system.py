books=[]
class book:
    def __init__(self,num,name,author,now):
        self.num=num
        self.name=name
        self.author=author
        self.now=now
    def add():
        name5=input("请输入添加名字:")
        num6=int(input("请输入编号"))
        author3=input("请输入作者:")
        books.append(book(name5,num6,author3))
        book.now="在馆"
        print("已存入",name5)
    def show_all():
        print(books)
    def bloow():
        num1=int(input("请输入借出书籍的编号:"))
        for s in books:
            if s.num==num1:
                s.now="借出"
    def huan():
        num2=int(input("请输入归还书籍编号:"))
        for s in books:
                    if s.num==num2:
                        s.now="在馆"
while True:
    print("""===== 图书借阅管理 =====
    1. 添加  2. 查看  3. 借书  4. 还书  5. 查找  6. 删除  7. 退出
    """)
    num3=int(input("请选择:"))     

    match(num3):
        case 1:
            
        case 2:
            print(books)





        