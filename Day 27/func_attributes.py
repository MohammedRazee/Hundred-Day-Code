# Working with default function values

def function (a=1, b=2):
    print(a+b)
# function(6)


# Learning args
def addition(*args):
    return sum(args)

# print(addition(1,2,3,4,5,6,7))


# Learning kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# Demo class with kwargs

class Car():
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
