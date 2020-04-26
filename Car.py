class Car:
    # properties
    color = ""
    brand = ""
    number_of_wheels = 4
    number_of_seats = 4
    maxspeed = 0

    # constructor
    def __init__(self, color, brand, number_of_wheels, number_of_seats, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_wheels = number_of_wheels
        self.number_of_seats = number_of_seats
        self.maxspeed = maxspeed

    # create method set color
    def setcolor(self, x):
        self.color = x

    def setbrand(self, x):
        self.brand = x

    def setspeed(self, x):
        self.maxspeed = x

    def printdata(self):
        print("color of this car is ", self.color)
        print("brand of this car is ", self.brand)
        print("max speed of this car is ", self.maxspeed)

    # deconstructor

    def __del__(self):
        print()
