#Define a class of car
class Car(object):
#Implememntation below
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        
    def getColour(self):
        return self.__colour
        
    def getMake(self):
        return self.__make
        
    def getMilage(self):
        return self.__mileage
        
    def getEngineSize(self):
        return self.__enginesize
        
    def setColour(self, colour):
        self.__colour = colour
    
    def setMake(self, make):
        self.__make = make   
    
    def setMilage(self, mileage):
        self.__mileage = mileage
        
    def setEngineSize(self, size):
        self.__enginesize = size
        
    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage
        
        
class ElectricCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
        
    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class DieselCar(Car):
    def __init__(self):
        Car.__init__(self)
        
class HybridCar(ElectricCar):
    def __init__(self):
        ElectricCar.__init__(self)



