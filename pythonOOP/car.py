class Car:
    def __init__(self, brand, model, rented):
        self.brand= brand
        self.model = model
        self.rented = rented

    def rentCar(self):
        self.rented = False

    def returnCar(self):
        self.available = False