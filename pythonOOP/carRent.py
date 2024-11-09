from car import Car

class RentCar:
    def __init__(self):
        self.data=[] 

    def add_car(self, newcar):
        self.data.append(newcar)



    def show_cars(self):
        for i in self.data:
            print(f"{i.brand} , {i.model}, {i.rented}")



def main():
    car_obj = RentCar()
    car1 = Car("tata", "Nexon" , True)
    car_obj.add_car(car1)

    car_obj.show_cars()


    

if __name__ == '__main__':
    main()

