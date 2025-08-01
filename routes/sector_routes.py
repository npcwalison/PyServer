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
    
    try:
        controller_sector(data)
        return jsonify({
            'mensagem': 'Setor registrado com sucesso!',
            'dados_recebidos:': data
        }), 201
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
# Final sector router.

@sector_bp.route('/register/users', methods=['POST'])
def registerUsers():
    data = request.get_json() # Recebe os dados JSON enviados pelo postman
    if not data:
        return jsonify({'error': 'Nenhum dado enviado'}), 400
    
    try:
        controller_sector(data)
        return jsonify({
            'mensagem': 'Setor registrado com sucesso!',
            'dados_recebidos:': data
        }), 201
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
# Final users router.

@sector_bp.route('/register/machines', methods=['POST'])
def registerMachines():
    data = request.get_json() # Recebe os dados JSON enviados pelo postman
    if not data:
        return jsonify({'error': 'Nenhum dado enviado'}), 400
    
    try:
        controller_sector(data)
        return jsonify({
            'mensagem': 'Setor registrado com sucesso!',
            'dados_recebidos:': data
        }), 201
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
# Final machines router.

@sector_bp.route('/register/events', methods=['POST'])
def registerEvents():
    data = request.get_json() # Recebe os dados JSON enviados pelo postman
    if not data:
        return jsonify({'error': 'Nenhum dado enviado'}), 400
    
    try:
        controller_sector(data)
        return jsonify({
            'mensagem': 'Setor registrado com sucesso!',
            'dados_recebidos:': data
        }), 201
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
# Final events router.