from flask import Flask
from routes.sector_routes import sector_bp
from database.model import create_user_table
from waitress import serve

# Cria uma instância do Flask
app = Flask(__name__)
app.register_blueprint(sector_bp)
# Dados Falsos data = ['teste', 'ola']


# Vizualizar
@app.route('/', methods=['GET'])
def home():
    return jsonify('inicio'), 200

# Indentifica se o arquivo atual esta sendo executado diretamente
if __name__ == "__main__":
    create_user_table() # Verifica e cria a base de dados.
    serve(app, host="0.0.0.0", port=5000) # Inicia o servidor indicando o IP e PORTA
    #app.run(debug=True, host="0.0.0.0", port=5000) # Inicia o servidor em modo de teste