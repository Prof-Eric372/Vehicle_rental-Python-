from flask import Flask, jsonify, request
from config.database import get_vehicles, update_vehicle_availability
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import bcrypt
from config.database import get_vehicles, update_vehicle_availability, insert_user, get_user, create_users_table

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'vehiclerental_secret_key'
jwt = JWTManager(app)

create_users_table()

@app.route('/vehicles', methods=['GET'])
def list_vehicles():
    vehicles = get_vehicles()
    vehicles_list = []
    for v in vehicles:
        vehicles_list.append({
            "id": v[0],
            "brand": v[1],
            "model": v[2],
            "color": v[3],
            "plate": v[4],
            "year": v[5],
            "is_available": v[6]
        })
    return jsonify(vehicles_list)
@app.route('/vehicles/<plate>', methods=['GET'])
def get_vehicle_by_plate(plate):
    vehicles = get_vehicles()
    for v in vehicles:
        if v[4] == plate.upper():
            return jsonify({
                "id": v[0],
                "brand": v[1],
                "model": v[2],
                "color": v[3],
                "plate": v[4],
                "year": v[5],
                "is_available": v[6]
            })
    return jsonify({"message": "Veículo não encontrado!"}), 404


@app.route('/rent', methods=['POST'])
@jwt_required()
def rent_vehicle():
    data = request.json
    plate = data['plate'].upper()

    vehicles = get_vehicles()
    for v in vehicles:
        if v[4] == plate:
            if v[6] == 1:  # is_available
                update_vehicle_availability(plate, 0)
                return jsonify({"message": "Veículo alugado com sucesso!"})
            else:
                return jsonify({"message": "Veículo indisponível!"}), 400

    return jsonify({"message": "Veículo não encontrado!"}), 404


@app.route('/return', methods=['POST'])
def return_vehicle():
    data = request.json
    plate = data['plate'].upper()

    vehicles = get_vehicles()
    for v in vehicles:
        if v[4] == plate:
            if v[6] == 0:  # is_available == 0 → tá alugado
                update_vehicle_availability(plate, 1)
                return jsonify({"message": "Veículo devolvido com sucesso!"})
            else:
                return jsonify({"message": "Veículo não estava alugado!"}), 400

    return jsonify({"message": "Veículo não encontrado!"}), 404

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    insert_user(username, password)
    return jsonify({"message": "Usuário cadastrado com sucesso!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = get_user(data['username'])
    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user[2]):
        token = create_access_token(identity=data['username'])
        return jsonify({"token": token})
    return jsonify({"message": "Usuário ou senha inválidos!"}), 401

if __name__ == '__main__':
    app.run(debug=True)

