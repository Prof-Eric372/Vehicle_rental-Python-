from vehicle import Vehicle
class Car (Vehicle):
    def __init__(self, plate, brand, model, color, year, fuel_type,transmission, category):
        super().__init__(plate, brand, model, color, year,)
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.category = category

    def display_info (self):
        super().display_info()
        print(f"Fuel type:  + {self.fuel_type}")
        print(f"Transmission: + {self.transmission}")
        print(f"Category: {self.category}")


