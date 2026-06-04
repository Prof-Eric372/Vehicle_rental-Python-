from config.price_table import PRICE_TABLE


class Rental:
    def __init__(self, customer, vehicle, rental_date, return_date, price_per_day, total_price):
        self.customer = customer
        self.vehicle = vehicle
        self.rental_date = rental_date
        self.return_date = return_date
        self.price_per_day = price_per_day
        self.total_price = total_price

    def display_info(self):
        print(f'Customer Name: {self.customer.name}')
        print(f"Vehicle Name: {self.vehicle.model}")
        print(f"Rental Date: {self.rental_date}")
        print(f"Return Date: {self.return_date}")
        print(f"Price per Day: {self.price_per_day}")
        print(f"Total Price: {self.total_price}")


    def calculate_total(self):
        def calculate_total(self):
            try:
                days = (self.return_date - self.rental_date).days
                price = PRICE_TABLE[self.vehicle.category]
                self.total_price = days * price
                return self.total_price
            except ValueError:
                print("Data inválida!")
            except KeyError:
                print("Categoria não encontrada na tabela de preços!")

    def display_info(self):
        print(f"Customer: {self.customer.name}")
        print(f"Vehicle: {self.vehicle.brand} {self.vehicle.model}")
        print(f"Rental Date: {self.rental_date.strftime('%d/%m/%Y')}")
        print(f"Return Date: {self.return_date.strftime('%d/%m/%Y')}")
        print(f"Price per Day: R${self.price_per_day}")
        print(f"Total Price: R${self.total_price}")