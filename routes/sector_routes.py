from flask import Blueprint, request, jsonify
from controller.sectors import controller_sector
from controller.sectors import controller_users
from controller.sectors import controller_machines
from controller.sectors import controller_events

sector_bp = Blueprint('sector', __name__)


# Adicionar Valores
@sector_bp.route('/register/sector', methods=['POST'])
def registerSector():
    data = request.get_json() # Recebe os dados JSON enviados pelo postman
    if not data:
        return jsonify({'error': 'Nenhum dado enviado'}), 400
    
    return jsonify({'mensagem': 'Setor registrado com sucesso!', 'dados_recebidos:': data}), 201
    # return jsonify('registrar sector'), 200

@sector_bp.route('/register/users', methods=['POST'])
def registerUsers():
    data = request.get_json() # Recebe os dados JSON enviados pelo postman
    if not data:
        return jsonify({'error': 'Nenhum dado enviado'}), 400
    
    return jsonify({'mensagem': 'Setor registrado com sucesso!', 'dados_recebidos:': data}), 201

    # return jsonify('registrar usuarios'), 200

@sector_bp.route('/register/machines', methods=['POST'])
def registerMachines():
    data = request.get_json() # Recebe os dados JSON enviados pelo postman
    if not data:
        return jsonify({'error': 'Nenhum dado enviado'}), 400
    
    return jsonify({'mensagem': 'Setor registrado com sucesso!', 'dados_recebidos:': data}), 201

    # return jsonify('registrar maquinas'), 200

@sector_bp.route('/register/events', methods=['POST'])
def registerEvents():
    data = request.get_json() # Recebe os dados JSON enviados pelo postman
    if not data:
        return jsonify({'error': 'Nenhum dado enviado'}), 400
    
    return jsonify({'mensagem': 'Setor registrado com sucesso!', 'dados_recebidos:': data}), 201

    # return jsonify('registrar eventos'), 200