# Task 2: Car Dealership and Car Objects

# Create a Car class with attributes like brand, model, year, and price.

# Create a Dealership class that stores a list of cars.

# Implement __str__() for Car to print the car details.

# Write methods in Dealership to add cars, search for cars based on price or brand, and remove sold cars.

class Car:

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    def __str__(self):
        return f"{self.brand} by {self.model}, published in {self.price}"     

class Dealership:
    def __init__(self):
        self.cars = []
    
    def add_cars(self, car):
        self.cars.append(car)
    
    def remove_car(self, car):
       self.cars.remove(car)

    def search_car(self):
        carname = input("Enter brand of car: ").upper()
        for i in self.cars:
            if i.brand.upper()==carname:
                print("yes")
                print(f"{i.brand} by {i.model}, published in {i.price}")
            else:
                print("No")

        # if car in self.cars:
        #     print("yes")
        # else:
        #     print("No")
        
    def show_cars(self):
        for car in self.cars:
            print(car)


car1 = Car("Toyota", "Camry", 2020, 25000)
car2 = Car("Honda", "Civic", 2019, 22000)

d = Dealership()
d.add_cars(car1)
d.show_cars()
print()
d.add_cars(car2)
d.show_cars()
print()

d.remove_car(car1)

d.show_cars()
print()
d.search_car()


