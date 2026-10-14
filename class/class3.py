class car:
    def __init__(self,color,brand,price):
        self.wheel=4
        self.tax=0.1
        self.color=color
        self.brand=brand
        self.price=price
        print(f"{self.brand} is created")
    def running(self):
        print(f"{self.brand}  is running")
    def total_cost(self,discount,rate):
        return self.price*discount+self.price*rate
    def __str__(self):
        return f"{self.color},{self.brand},{self.price})"
    def __eq__(self,other):
        return self.color==other.color and self.brand==other.brand and self.price==other.price
    def __lt__(self,other):
        return self.price<other.price
c1=car("red","BMW",1000000)
c2=car("red","BMW",100000)
total_cost=c1.total_cost(0.8,0.1)
print(f"Total cost of {c1.brand} is: {total_cost}")
c1.running()
print(c1==c2)
print(c1>c2)
print(c1.wheel)