from car import *

class Dealership(object):
    def __init__(self):
        self.electriccars = []  #list electric
        self.petrolcars = []   #list petrol
        self.dieselcars = []    #list diesel
        self.hybridcars = []    #list hybrid
        self.rentedcars = []   # Cars that are rented
                                
    def create_petrol_cars(self, amount, colour, make):
    
        for x in range(amount):         # Create petrol cars
            grey_car = Car()
            grey_car.setMake(make)
            grey_car.paint(colour)
            grey_car.setEngineSize('4 Cylinder')
            grey_car.move(10000)
            self.petrolcars.append(grey_car)
                        
    def create_diesel_cars(self, amount):     # etc for all cars to be created
        diesel_car = DieselCar()
        diesel_car.setMake('Volkswagon Golf')
        diesel_car.paint('Black')
        diesel_car.setEngineSize('4 Cylinder')
        diesel_car.move(15000)
        self.dieselcars.append(diesel_car)
        
    def create_electric_cars(self, amount):   # Create electric cars
        electric_car = ElectricCar()
        electric_car.setMake('Nissan Leaf')
        electric_car.paint('Red')
        electric_car.setNumberFuelCells(4)
        electric_car.move(9000)
        self.electriccars.append(electric_car)
        
    def create_hybrid_car(self, amount):   # Create hybrid cars
        white_car = HybridCar()
        white_car.setMake('Toyota Prius')
        white_car.paint('White')
        white_car.setEngineSize('4 Cylinder')
        white_car.move(10000)
        white_car.setNumberFuelCells(4)
        self.hybridcars.append(white_car)   

    def create_current_stock(self):       # Create current stock of all 4 types of cars
            
        for i in range(4):
            self.electriccars.append(ElectricCar())                
        for i in range(16):
            self.create_petrol_cars(1, 'Blue', 'Volkswagon Golf')
        for i in range(8):
            self.create_petrol_cars(1, 'Black', 'Ford Focus')                                                                   
        for i in range(8):
            self.dieselcars.append(DieselCar())            
        for i in range(4):
            self.hybridcars.append(HybridCar())
                                                
    def stock_count(self):       # Stock count at end of transaction for a given car type
        print 'There are %d petrol cars in stock' %(len(self.petrolcars))
        print 'There are %d diesel cars in stock' %(len(self.dieselcars))
        print 'There are %d electric cars in stock' %(len(self.electriccars))
        print 'There are %d hybrid cars in stock' %(len(self.hybridcars))
        
    def rent(self, car_list, amount):     # Process to rent a car function        
        if len(car_list) < amount:
            print 'Not enough cars in stock'     # Make sure enough cars in stock
            return
        total = 0
        while total < int(amount):
            carout = car_list.pop()          # Pop last item from given car list and return it
            self.rentedcars.append(carout)       # Then append to a new list of rented cars that are now unavailable
            total = total + 1
            print 'Make: ' + carout.getMake()       
            print 'Colour: ' + carout.getColour()
            print 'Engine Size(Cylinders): ' + carout.getEngineSize()            
        print 'You have rented ' + str(amount) + ' car(s)'       
        return self.rentedcars

    def rented(self, car_list, amount):  # Process for returning cars        
        total = 0
        while total < int(amount):
            carin = self.rentedcars.pop()
            
            car_list.append(carin)
            total = total + 1
        print 'You have returned ' + str(amount) + 'car(s)'
        
                    
    def rental_system(self): 
        
        rented = raw_input('Are you returning or renting a car? Type either return/rent ')
        if rented.lower() == 'return':       # Return system
            type = raw_input('Are you returning a petrol, electric, diesel or hybrid car? ')
            amount = raw_input('How many would you like to return? ')
            if type == 'petrol':
                self.rented(self.petrolcars, amount)
            elif type.lower() == 'diesel':
                self.rented(self.dieselcars, amount)
            elif type.lower() == 'hybrid':
                self.rented(self.hybridcars, amount)
            elif type.lower() == 'electric':
                self.rented(self.electriccars, amount)
            else:
                print 'Error, please check your spelling'
                
            
        elif rented.lower() == 'rent':        
# Rental process                     
            answer = raw_input('What type of car would you like? Type: petrol/diesel/hybrid/electric ')
            amount = int(raw_input('How many of that type of car?'))
            if answer.lower() == 'petrol':
                self.rent(self.petrolcars, amount)
            elif answer.lower() == 'diesel':
                self.rent(self.dieselcars, amount)
            elif answer.lower() == 'hybrid':
                self.rent(self.hybridcars, amount)
            elif answer.lower() == 'electric':
                self.rent(self.electriccars, amount)
            else:
                print 'Error, please check your spelling'
                return
        else:
            print 'Error, please check your spelling'
            return
        self.stock_count()
        
            
dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.rental_system()
    proceed = raw_input('Continue? y/n ')
print 'Thank you for renting with DBS cars'