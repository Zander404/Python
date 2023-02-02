from abc import ABC, abstractmethod #ABS = Abstract Basic Class

class Vehicle(ABC):

    @abstractmethod # Serve para definir os metodos necessarios para as classes filhas 
    def go(self):
        pass

    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        pass
    def start(self):
        print('Car is on now!')
        pass

    def off(self):
        pass


car = Car()
car.start()
