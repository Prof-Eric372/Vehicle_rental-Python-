from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck

vehicles = []
#add vehicles
vehicles.append(Car("QWJ873", "Chevrolet", "Ônix", "Black", 2023, "Gasoline", "Automatic", "Economy way"))
vehicles.append(Motorcycle("QTU304", "Honda", "Biz", "White", 2024, 110, "Motoneta", False))
vehicles.append(Truck("TSV951", "Mercedes", "Sprinter", "Black and Grey", 2021, 1500.0, True, "Baú"))

#list
for v in vehicles:
    v.display_info()
    print("---------------------------")


#AVAILABLE VEHICLES
for v in vehicles:
    print("===AVAILABLE VEHICLES ===")
    if v.is_available:
        print(f"{v.brand} {v.model} - {v.plate}")
        print("------------------------")
        v.display_info()

