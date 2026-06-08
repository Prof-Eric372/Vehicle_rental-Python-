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

def update_vehicle_availability(plate, is_available):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
            UPDATE vehicles 
            SET is_available = ?
            WHERE plate = ?
        """, (is_available, plate))
    conn.commit()
    conn.close()

def create_users_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (username, password)
            VALUES (?, ?)
        """, (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Usuário {username} já existe!")
    finally:
        conn.close()

def get_user(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

