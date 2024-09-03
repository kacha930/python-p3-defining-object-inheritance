from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    

print(Car.__bases__)

