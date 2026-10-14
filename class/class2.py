class car:
    def __init__(self,color,brand,price):
        self.color=color
        self.brand=brand
        self.price=price
c1=car("red","BMW",1000000)
print(c1)
print(c1.__dict__)
