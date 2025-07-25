from flask import Flask, request, jsonify

# Cria uma instância do Flask
app = Flask(__name__)

# Dados Falsos
data = ['teste', 'ola']


# Vizualizar
@app.route('/view', methods=['GET'])
def view():
    return jsonify(data), 200

# Indentifica se o arquivo atual esta sendo executado diretamente
if __name__ == "__main__":
    # Inicia o servidor indicando o IP e PORTA
    app.run(host="0.0.0.0", port=5000)