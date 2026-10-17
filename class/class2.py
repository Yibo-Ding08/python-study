class car:
    def __init__(self,color,brand,price,owner):
        self.color=color
        self.brand=brand
        self.price=price
        self.__owner=owner
    def start(self):
        print(f"{self.__owner}:{self.brand} is starting")
        self.__control_fuel()
    def __control_fuel(self):
        print(f"{self.brand}正在控制油门")
    def get_owner(self):
        return self.__owner[0:1]
class ai:
    def __init__(self,verson):
        self.verson=verson
class elecar(car,ai):
    def __init__(self,color,brand,price,owner,verson):
        super().__init__(color,brand,price,owner)
        ai.__init__(self,verson)
        


c1=car("red","BMW",1000000,"怡博")
print(c1)
c1.start()
print(c1.get_owner()+"**")


c2=elecar("red","bwa",100,"ddd","1.0")
print(c2.color)

