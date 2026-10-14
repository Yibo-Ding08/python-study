class student:
    def __init__(self, name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    def __str__(self):
        return f"{self.name}|语文:{self.chinese},数学:{self.math},英语:{self.english}"
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese=chinese
        if math is not None:
            self.math=math  
        if english is not None:
            self.english=english

#教务管理
class edum:
     system_verson="1.0"
     system_name="教务管理系统"
     def __init__(self):
          self.students_list=[]#列表,记录在校学生信息
    #添加成绩
     def add_student(self,student):
        name=input("请输入学生姓名:")
        if name in [s.name for s in self.students_list]:
            print("该学生已存在")
            return
        chinese=int(input("请输入语文成绩:"))
        math=int(input("请输入数学成绩:"))
        english=int(input("请输入英语成绩:"))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            new_student=student(name,chinese,math,english)
            self.students_list.append(new_student)
            print(f"学生{name}成绩已添加")
        else:
            print("成绩输入有误,请重新输入")
     def update_student(self):
         name=input("请输入要修改成绩的学生姓名:")
         for s in self.students_list:
               if s.name==name:
                     print(f"当前成绩为:语文:{s.chinese},数学:{s.math},英语:{s.english}")
                     chinese=int(input("请输入新的语文成绩:"))
                     math=int(input("请输入新的数学成绩:"))
                     english=int(input("请输入新的英语成绩:"))
                     if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                        s.update_score(chinese,math,english)
                        print(f"学生{name}成绩已更新")
                        return
                     else:
                        print("成绩输入有误,请重新输入")
                        return
         print(f"未找到学生{name},请检查输入是否正确")
     def delete_student(self):
         name=input("请输入要删除成绩的学生姓名:")
         for s in self.students_list:
               if s.name==name:
                     self.students_list.remove(s)
                     print(f"学生{name}成绩已删除")
                     return
         print(f"未找到学生{name},请检查输入是否正确")
     def query_student(self):
         name=input("请输入要查询成绩的学生姓名:")
         for s in self.students_list:
               if s.name==name:
                     print(f"学生{name}成绩为:语文:{s.chinese},数学:{s.math},英语:{s.english}")
                     return
         print(f"未找到学生{name},请检查输入是否正确")
     #查询全部学生
     def query_all_students(self):
         if not self.students_list:
               print("暂无学生信息")
               return
         print(f"共{len(self.students_list)}名学生:")
         for s in self.students_list:
               print(s)
     def run(self):
          print(f"欢迎使用{self.system_name} v{self.system_verson}")
          while True:
               print()
               print("# # # # # # # # # # # # # # # # # #")
               print("1.添加学生成绩")
               print("2.修改学生成绩")
               print("3.删除学生成绩")
               print("4.查询指定学生成绩")
               print("5.查询全部学生")
               print("6.退出系统")
               choice=input("请输入操作编号:")
               try:
                    match choice:
                        case "1":
                            self.add_student(student)
                        case "2":
                            self.update_student()
                        case "3":
                            self.delete_student()
                        case "4":
                            self.query_student()
                        case "5":
                                                
                         self.query_all_students()
                        case "6":
                            print("退出系统")
                            break
                        case _:
                            print("输入有误,请重新输入")
               except ValueError:
                    print("输入有误,请重新输入")
               except Exception as e:
                    print(f"发生错误:{e},请重新输入")            
if __name__=="__main__":
    edu_system=edum()
    edu_system.run()
    
