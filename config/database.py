import sqlite3
from models.vehicle import Vehicle


def create_connection():
    conn = sqlite3.connect("vehicle_rental.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS vehicles (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   brand TEXT NOT NULL,
                   model TEXT NOT NULL,
                   color TEXT NOT NULL,
                   plate TEXT NOT NULL UNIQUE,
                   year INTEGER NOT NULL,
                   is_available INTEGER DEFAULT 1
                   )
                   """)
    conn.commit()
    conn.close()

def insert_vehicle(brand, model, color, plate, year):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO vehicles (brand, model, color, plate, year)
            VALUES (?, ?, ?, ?, ?)
        """, (brand, model, color, plate, year))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Veículo com placa {plate} já cadastrado!")
    finally:
        conn.close()

def get_vehicles():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicles_as_objects ():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehicles")
    rows = cursor.fetchall()
    conn.close()

    vehicles = []
    for row in rows:
        v = Vehicle(row[4], row[1], row[2], row[3], row[5])
        vehicles.append(v)
    return vehicles
