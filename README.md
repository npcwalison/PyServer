#### COMO BAIXAR E CONFIGURAR ESTE PROJETO

 Quando Baixar o projeto, use o comando: <br/>
~~~
python -m venv venv
~~~

Para ativar o ambiente virtual python: <br/>
~~~
 .venv\Scripts\activate 
~~~

Antes de upar o projeto use para gravar as dependências: <br/>
~~~
pip freeze > requirements.txt
~~~

Para desativar o ambiente virtual python: <br/>
~~~
deactivate
~~~

Para instalar as dependências: <br/>
~~~
pip install -r requirements.txt
~~~

Para rodar o nosso codigo, executar no terminal: <br />
~~~
uvicorn main:app --reload
~~~


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


### MODELO DE BANDO DE DADOS

~~~sql
                -- CRIA SETOR COMO MESTRE DE TUDO
                CREATE TABLE IF NOT EXISTS gti_sectors (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    sc_name VARCHAR(100),
                    sc_description VARCHAR(500)
                );
                -- CRIA MAQUINAS PRESENTES NO SETOR
                CREATE TABLE IF NOT EXISTS gti_machines (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    mh_name VARCHAR(100),
                    mh_system_op VARCHAR(45),
                    mh_motherboard VARCHAR(100),
                    mh_processor VARCHAR(100),
                    mh_memory_ram VARCHAR(100),
                    mh_storage VARCHAR(100),
                    sector_id_sector UUID, --FK
                    CONSTRAINT fk_machines_sector FOREIGN KEY (sector_id_sector) REFERENCES gti_sectors(id)
                );
                -- CRIA USUARIOS E OS ATIBUE AOS SETORES E MAQUINAS
                CREATE TABLE IF NOT EXISTS gti_users (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    name VARCHAR(100),
                    sr_email VARCHAR(100),
                    sr_sector VARCHAR(50),
                    sector_id_sector UUID, --FK
                    CONSTRAINT fk_users_sector FOREIGN KEY (sector_id_sector) REFERENCES gti_sectors(id)
                );
                -- CRIA EVENTOS QUE PODEM SER RELACIONADOS A TUDO
                CREATE TABLE IF NOT EXISTS gti_events (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    ev_name VARCHAR(100),
                    ev_sector VARCHAR(50),
                    ev_description VARCHAR(8000),
                    ev_date_create TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ev_date_start TIMESTAMP NOT NULL,
                    ev_date_end TIMESTAMP DEFAULT NULL,
                    user_id_user UUID, --FK
                    sector_id_sector UUID, --FK
                    machines_id_machines UUID, --FK
                    CONSTRAINT fk_events_user FOREIGN KEY (user_id_user) REFERENCES gti_users(id),
                    CONSTRAINT fk_events_sector FOREIGN KEY (sector_id_sector) REFERENCES gti_sectors(id),
                    CONSTRAINT fk_events_machines FOREIGN KEY (machines_id_machines) REFERENCES gti_machines(id)
                );
                -- GERA REGISTRO DE LOGIN DE USUARIOS
                CREATE TABLE IF NOT EXISTS users_has_machines (
                    user_id_user UUID, --FK
                    machines_id_machines UUID, --FK
                    mc_date_start TIMESTAMP NOT NULL,
                    mc_date_end TIMESTAMP DEFAULT NULL,
                    PRIMARY KEY (user_id_user, machines_id_machines, mc_date_start),
                    CONSTRAINT fk_user_machines_user FOREIGN KEY (user_id_user) REFERENCES gti_sectors(id),
                    CONSTRAINT fk_user_machines_machines FOREIGN KEY (machines_id_machines) REFERENCES gti_machines(id)
                );
~~~
