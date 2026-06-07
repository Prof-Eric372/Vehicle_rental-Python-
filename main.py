from config.database import create_table, insert_vehicle, get_vehicles, get_vehicles_as_objects
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck
from models.customer import Customer
from models.rental import Rental
from datetime import datetime


#list
vehicles = get_vehicles_as_objects                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ()
for v in vehicles:
    v.display_info()
    print("---------------------------")


#AVAILABLE VEHICLES
print("===AVAILABLE VEHICLES ===")
for v in vehicles:
    if v.is_available:
        print(f"{v.brand} {v.model} - {v.plate}")
        print("------------------------")
        v.display_info()

 #SEARCH VEHICLE
plate = input("Buscar veículo por placa: ").upper()
found = False

for v in vehicles:
    if v.plate == plate:
        v.display_info()
        found = True

if not found:
    print("Veículo não encontrado!")

#RENT FUNCTION:
plate = input("Digite a placa: ").upper()

for v in vehicles:
    if v.plate == plate:
        if v.is_available:
            v.rent()
            print("Veículo alugado com sucesso!")
        else:
            print("Veículo indisponível!")

# RETURN VEHICLES
plate = input("Digite a placa para devolver: ").upper()

for v in vehicles:
    if v.plate == plate:
        if not v.is_available:
            v.return_vehicle()
            print("Veículo devolvido com sucesso!")
        else:
            print("Veículo não estava alugado!")

#CUSTOMER
customer1 = Customer("Carlin", "057.876.099-32", True, "45378967-8", "91934558000")

#RENTAL
car1 = Car("QWJ873", "Chevrolet", "Ônix", "Black", 2023, "Gasoline", "Automatic", "Economy way")
rental1 = Rental(customer1, vehicles[0],datetime(2026, 5, 1), datetime(2026, 5,15), 0,0)
rental1.calculate_total()
rental1.display_info()

#TABLE
create_table()
insert_vehicle("Chevrolet", "Ônix", "Black", "QWJ873", 2023)
insert_vehicle("Honda", "Biz", "White", "QTU304", 2024)
insert_vehicle("Mercedes", "Sprinter", "Black and Grey", "TSV951", 2021)

#GET VEHICLES FROM DATABASE
vehicles_db = get_vehicles()