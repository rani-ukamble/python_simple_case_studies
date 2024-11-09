#WAP to inherit a class and extend their properties

class Car:

    def __init__(self, carname="BMW", carmodel="x10", color="white", cost=100000):
        self.carname = carname
        self.carmodel = carmodel
        self.color = color
        self.cost = cost

    def __str__(self):
        return f"{self.carname} \t {self.carmodel} \t {self.color} \t {self.cost}"


class Sales(Car):
    l = []
    def __init__(self, carDetails=None):
        self.l.append(self)
        if carDetails!=None:
            super().__init__(carDetails['carname'], carDetails['model'], carDetails['color'], carDetails['cost'])
            
        else:
            super().__init__()
            

    def purchaseCar(self, date, downpayment, customer):
        self.date = date
        self.downpayment = downpayment
        self.customer = customer

    def showSales(self):
        print("Car Details = ", super().__str__())
        print("Sales Details = ", self.date, self.downpayment, self.customer)

    def print_list_of_details(self):
        for i in Sales.l:
            print(i)
      

s1 = Sales()
s1.purchaseCar("10-Jan-2024", 80000, "smith")
# s1.showSales()

s2 = Sales({'carname':"Ferrari1", 'model':"F10", 'color':"red", 'cost':7000000})
s3 = Sales({'carname':"Ferrari2", 'model':"F11", 'color':"red", 'cost':7000000})
s4 = Sales({'carname':"Ferrari3", 'model':"F12", 'color':"red", 'cost':7000000})

# s2.purchaseCar("18-Feb-2024", 600000, "peter")
# s2.showSales()

# s1.print_list_of_details()
s2.print_list_of_details()




