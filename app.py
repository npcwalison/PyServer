from flask import Flask, request, jsonify
from database.model import create_user_table
from waitress import serve

# Cria uma instância do Flask
app = Flask(__name__)

# Dados Falsos
data = ['teste', 'ola']


# Vizualizar
@app.route('/', methods=['GET'])
def home():
    return jsonify(data), 200

# Adicionar Valores
@app.route('/register', methods=['GET'])
def register():
    return jsonify('teste de cadastro'), 200

# Indentifica se o arquivo atual esta sendo executado diretamente
if __name__ == "__main__":
    create_user_table() # Verifica e cria a base de dados.
    serve(app, host="0.0.0.0", port=5000) # Inicia o servidor indicando o IP e PORTA