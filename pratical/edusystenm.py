stu=[]
def add():
    student=input("请输入学生姓名:")
    while True:
        try:
            score=int(input("请输入学生成绩:"))
            break
        except ValueError:
            print("成绩必须是整数")
    stu.append({"name":student,"score":score})
    print("成绩添加完毕")
def see():
    for s in stu:
        print(s["name"], s["score"])
    if not stu:
        print("无学生")
def sort():
    if not stu:
            print("无学生")
            return
    stu.sort(key=lambda x: x["score"],reverse=True)
    print(stu)
def dele():
    name=input("输入姓名:")
    for s in stu:
        if name==s["name"]:
            stu.remove(s)
            print("已删除")
            return
    print("未找到学生")
while True:
    print("\n===== 学生成绩管理 =====")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 按成绩排序")
    print("4. 删除学生")
    print("5. 退出")
    choice = input("请选择(1-5):")

    if choice == "1":
        add()
    elif choice == "2":
        see()
    elif choice == "3":
        sort()
    elif choice == "4":
        dele()
    elif choice == "5":
        print("再见!")
        break
    else:
        print("请输入 1 到 5 之间的数字!")

    


