from vehicle import Vehicle

class Truck(Vehicle):
    def __init__ (self, plate, brand, model, color, year, cargo_capacity, has_refrigeration, truck_type):
        super().__init__(plate,brand, model, color, year)
        self.truck_type = truck_type
        self.has_refrigeration = has_refrigeration
        self.cargo_capacity = cargo_capacity

    def display_info (self):
        super().display_info()
        print(f"Truck type: {self.truck_type}")
        print(f"has_refrigeration: {self.has_refrigeration}")
        print(f"truck_capacity: {self.cargo_capacity}")