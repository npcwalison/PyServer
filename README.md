#### COMO BAIXAR E CONFIGURAR ESTE PROJETO

 Quando Baixar o projeto, use o comando: <br/>
``` python -m venv venv ```

Para ativar o ambiente virtual python: <br/>
``` .venv\Scripts\activate ```

Antes de upar o projeto use para gravar as dependências: <br/>
``` pip freeze > requirements.txt ```

Para desativar o ambiente virtual python: <br/>
``` deactivate ```

Para instalar as dependências: <br/>
``` pip install -r requirements.txt ```

Para rodar o nosso codigo, executar no terminal: <br />
``` uvicorn main:app --reload ```


#### MODELO DE ESTRUTURA DO PROJETO



📁 meu_projeto <br/>
│ <br/>
├── 📁 .venv/ㅤㅤㅤㅤ# Pasta relacionada ao ambiente virtual python <br/>
├── 📁 Include/  <br/>
├── 📁 Lib/  <br/>
├── 📁 Scripts/  <br/>
│   └── settings.jsonㅤㅤㅤㅤ# Configura o vscode para elimitar os arquivos de cache <br/>
│ <br/>
├── 📁 .vscode/ㅤㅤㅤㅤ# Pasta relacionada ao vscode <br/>
│   └── settings.jsonㅤㅤㅤㅤ# Configura o vscode para elimitar os arquivos de cache <br/>
│ <br/>
├── 📁 config/ㅤㅤㅤㅤ# Projeto Django (configuração global) <br/>
│   ├── __ init __.py <br/>
│   ├── settings.pyㅤㅤㅤㅤ# Configurações do projeto <br/>
│   ├── urls.pyㅤㅤㅤㅤ# URLs globais <br/>
│   ├── asgi.py <br/>
│   └── wsgi.py <br/>
│ <br/>
├── 📁 apps/ㅤㅤㅤㅤ# Aplicações da API (módulos do ERP) <br/>
│   ├── 📁 users/ㅤㅤㅤㅤ# App: usuários e autenticação <br/>
│   │   ├── migrations/ <br/>
│   │   ├── __ init __.py <br/>
│   │   ├── models.pyㅤㅤㅤㅤ# Modelos de usuário <br/>
│   │   ├── views.pyㅤㅤㅤㅤ# Lógica da API (controllers) <br/>
│   │   ├── serializers.pyㅤㅤㅤㅤ# Serialização de dados <br/>
│   │   ├── urls.pyㅤㅤㅤㅤ# Rotas específicas <br/>
│   │   ├── permissions.pyㅤㅤㅤㅤ# Regras de acesso personalizadas <br/>
│   │   └── services.pyㅤㅤㅤㅤ# Lógica de negócio extra <br/>
│   │ <br/>
│   ├── 📁 financeiro/ <br/>
│   ├── 📁 estoque/ <br/>
│   ├── 📁 clientes/ㅤㅤㅤㅤ# Cadastro e gestão de clientes <br/>
│   ├── 📁 contratos/ㅤㅤㅤㅤ# Gestão de contratos e planos <br/>
│   ├── 📁 notificacoes/ㅤㅤㅤㅤ# Envio de avisos, e-mails ou push <br/>
│   └── 📁 ... outros módulos <br/>
│ <br/>
├── 📁 core/ㅤㅤㅤㅤ# Lógica comum e utilitários <br/>
│   ├── __ init __.py <br/>
│   ├── models.pyㅤㅤㅤㅤ# Modelos base <br/>
│   ├── permissions.py <br/>
│   └── utils.pyㅤㅤㅤㅤ# Funções genéricas (ex: mascarar CPF) <br/>
│ <br/>
├── 📁 static/ㅤㅤㅤㅤ# Arquivos estáticos (caso precise) <br/>
├── 📁 media/ㅤㅤㅤㅤ# Uploads (caso use imagens/documentos) <br/>
│ <br/>
├── 📄 manage.pyㅤㅤㅤㅤ# Comando principal do Django <br/>
├── 📄 requirements.txtㅤㅤㅤㅤ# Lista de dependências <br/>
└── 📄 .env  <br/>
