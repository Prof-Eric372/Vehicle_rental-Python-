from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck
from customer import Customer
from rental import Rental

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
print("===AVAILABLE VEHICLES ===")
for v in vehicles:
    if v.is_available:
        print(f"{v.brand} {v.model} - {v.plate}")
        print("------------------------")
        v.display_info()

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
rental1 = Rental(customer1, vehicles[0],"2026-05-01", "2026-05-15", 200, 2000 )
rental1.display_info()