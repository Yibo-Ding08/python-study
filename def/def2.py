def fun1():
    print("This is function 1")
    fun2()
    print("Function 1 is done")
def fun2():
        print("This is function 2")
        fun3()
        print("Function 2 is done")
def fun3():
            print("This is function 3")
            print("Function 3 is done")
fun1()