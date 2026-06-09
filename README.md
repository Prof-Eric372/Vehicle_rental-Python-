# VehicleRental 

## About
A vehicle rental system built with Python using OOP concepts, REST API and SQLite database.
Python version of the Java VehicleRental project.

## Features
- List all vehicles
- List available vehicles
- Rent a vehicle by plate
- Return a vehicle by plate
- Customer registration
- Rental management with automatic price calculation
- REST API with Flask
- User authentication with JWT
- Web interface

## Technologies
- Python 3.13
- Flask
- SQLite
- JWT (flask-jwt-extended)
- bcrypt

## OOP Concepts Applied
- Inheritance
- Encapsulation
- Polymorphism
- Method Overriding

## Project Structure
VehicleRental
├── models → Vehicle, Car, Motorcycle, Truck, Customer, Rental
├── config → database.py, price_table.py
├── templates → index.html
├── app.py → REST API
└── main.py

## API Routes
| Method | Route | Description |
|---|---|---|
| GET | /vehicles | List all vehicles |
| GET | /vehicles/<plate> | Search by plate |
| POST | /rent | Rent a vehicle |
| POST | /return | Return a vehicle |
| POST | /register | Register user |
| POST | /login | Login |

## How to Run
```bash
python app.py
```

## Classes
- `Vehicle` → base class
- `Car`, `Motorcycle`, `Truck` → inherit from Vehicle
- `Customer` → customer registration
- `Rental` → rental management

