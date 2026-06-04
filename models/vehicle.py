class Vehicle:
    def __init__(self, plate, brand, model, color, year, ):
        self.plate = plate
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.is_available = True

    def display_info(self):
            print(f"plate: {self.plate}")
            print(f"brand: {self.brand}")
            print(f"model: {self.model}")
            print(f"color: {self.color}")
            print(f"year: {self.year}")
            print(f"is_available: {self.is_available}")

    def rent(self):
        self.is_available = False

    def return_vehicle(self):
        self.is_available = True