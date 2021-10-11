class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    def update_odometer(self,mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading  = mileage
        else:
            print("You can't roll the odometer back")

    def increment_odometer(self,miles):

        self.odometer_reading += miles
class Battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    def get_range(self):
        if self.battery_size == 75:
            range = 240
        elif self.battery_size == 100:
            range = 400
        print(f'This car can go about {range} miles on a full charge ')
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
        print(f'Battery has been upgraded to {self.battery_size}-kWH ')

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    #new child class of the parent class (car)
    def __init__(self,make,model,year):
        #attribute of parent class
        super().__init__(make,model,year)#it is use to call a method from parent class
        self.battery = Battery()



    def fill_gas_tank(self):
        print("this car doesn't need gas tank")

my_tesla = ElectricCar('tesla','model S',2019)
print(my_tesla.get_descriptive_name())
my_car = Car('Audi','A6',2018)
my_car.get_descriptive_name()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
