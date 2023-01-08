#

class car():
    def __init__(self,transmission,colour,seats,engin):
        self.transmission = transmission
        self.colour = colour
        self.seats = seats
        self.engin = engin
    def car_info(self):
        print("********Car Information**********")
        print("The car is having ",self.transmission," transmission system.")
        print("it comes in ",self.colour,"colour.")
        print("Providing",self.seats,"seater arrangement.")
        print("Also having a ",self.engin,"type of engin.")
    def custome (self,colour):
        self.colour=colour
print()
bmw=car("Semi-Automatic","black",4,"Petrol")
bmw.car_info()
print()
audi=car("Manual","white",4,"Disel")
audi.car_info()
print()
tesla=car("Automatic","blue",4,"Electric")
tesla.car_info()
print()
tesla.custome("red")
tesla.car_info()

print()
