# *args

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

    #return sum(args)

# print(add(1, 4, 7, 3, 2))


# def calculate(**kwargs):



class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")


my_car = Car(make="Toyota", model="4 x 4")

print(my_car.make)