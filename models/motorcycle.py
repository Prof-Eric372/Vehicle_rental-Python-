from models.vehicle import Vehicle

class Motorcycle (Vehicle):
    def __init__(self, plate, brand, model, color, year, engine_cc, type, has_storage):
        super().__init__(plate, brand, model, color, year)
        self.engine_cc = engine_cc
        self.type = type
        self.has_storage = has_storage

    def display_info(self):
        super().display_info()
        print(f"CC : {self.engine_cc}")
        print(f"Type : {self.type}")
        print(f"Has Storage : {self.has_storage}")
