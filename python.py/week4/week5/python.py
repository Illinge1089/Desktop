# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Smartphone(Device):
    def __init__(self, brand, model, color, price):
        super().__init__(brand, model)  
        self.color = color
        self.price = price

    def display_info(self):  
        super().display_info()
        print(f"Color: {self.color}")
        print(f"Price: ${self.price}")


phone1 = Smartphone("Apple", "iPhone 14 Pro", "Black", 1000)
phone2 = Smartphone("Samsung", "Galaxy S22", "White", 850)

phone1.display_info()
print("---")
phone2.display_info()

