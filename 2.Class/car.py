class Car:
    wheels = 4 
    start = False

    def __init__(self, make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        if  not Car.start:
            print(f"The car {self.make} is starting moving")
            Car.start = True
        else:
            print(f"The car {self.make} already is On, don't need start him again")

    def stop(self):
        if Car.start:
            print(f"The car {self.make} is off now")
        else:
            print(f"The car {self.make} is already off")