#init and str function
import math

class Passenger:
    
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.age} {self.gender}"

class Flight:
    passengers_list = list()
    
    def __init__(self, passenger, flightname, ticketcost):
        self.passenger = passenger
        self.flightname = flightname
        self.ticketcost = ticketcost
        
        self.passengers_list.append(self)

    def __str__(self):
        return f"{self.passenger} \t {self.flightname} \t {self.ticketcost}"

    def find_elder():
        eldest_passenger = None
        eldest_age = -1  

        # Iterate over the flight list to find the eldest passenger
        for flight in Flight.passengers_list:
            if flight.passenger.age > eldest_age:  
                eldest_age = flight.passenger.age 
                eldest_passenger = flight.passenger  # Update eldest passenger

        return eldest_passenger  # Return the eldest passenger

    # def find_male(self):
    #     for i in Flight.passengers_list:
    #         if i.gender==""


p1 = Passenger("james", "devid", 29, "male")
p2 = Passenger("peter", "mathew", 48, "male")
p3 = Passenger("bob", "mathew", 60, "male")


first_flight = Flight(p1, "INDIGO", 5000.00)
second_flight = Flight(p2, "AIR INDIA", 7000.00)
third_flight = Flight(p3, "AIR INDIA", 7000.00)


# for item in Flight.passengers_list:
#     print(item)


#Assignment: Compare condition for passengers in a passenger list, who is elder.


print()
# maxi = max(p1.age, p2.age)
elder = Flight.find_elder()
print(elder)
print()
