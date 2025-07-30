No final do projeto, antes de dar PUSH, use o comando: <br/>
``` pip freeze > requirements.txt ```

Quando Baixar o projeto, use o comando:
``` python -m venv venv ```

Para instalar as dependências:
``` pip install -r requirements.txt ```


Começamos pelo arquivo app.py que chama routes/sector_routes.py
o routes/sector_routes.py chama pelo controller/sectors.py

o routes/sector_routes.py que recebe os dados das conexões e depois passa para o controller
depois do controller tratar ele vai injetar os dados no banco de dados pleo database/inject.py
