from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# CRIA O ARQUIVO DE BANCO DE DADOS DA PASTA ATUAL
db = create_engine("sqlite:///banco.db")
# CRIA A BASE DO BANCO DE DADOS
Base = declarative_base()

# CRIA AS CLASSES QUE GERAM AS TABELAS DO BANCO DE DADOS
# Usuarios
class User(Base):
    __tablename__ = "users" # Define manualmente o nome da tabela

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name =  Column("name", String)
    email =  Column("email", String, nullable=False)
    passwd =  Column("passwd", String, nullable=False)
    active =  Column("active", Boolean)
    admin =  Column("status", Boolean)

# Identifica quando a classe é iniciada e chama a função para essa classe somente.
    def __init__(self, name, email, passwd, active=True, admin=False):
        self.name = name
        self.email = email
        self.passwd = passwd
        self.active = active
        self.admin = admin

# Pedido
class Request(Base):
    __tablename__ = "requests"

# lista de tuplas para o ChoiceType do sqlalchemy_utils, que serve para definir valores especificos para uma variavel
#    STATUS_PEDIDOS = (
#        ("PENDENTE","PENDENTE"),
#        ("CANCELADO","CANCELADO"),
#        ("FINALIZADO","FINALIZADO"),
#    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente, cencelado, finalizado
    user = Column("user", ForeignKey("users.id")) # FK  da tabela users
    price = Column("price", Float)
    # items = Column("items", String)

    def __init__(self, user, status="PENDENTE", price=0):
        self.user = user
        self.price = price
        self.status = status
    

# ItensPedido
class ItemRequest(Base):
    __tablename__ = "itens_request"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    amount = Column("amount", Integer)
    flavor =  Column("flavor", String)
    size =  Column("size", String)
    unit_price =  Column("unit_preice", Float)
    request =  Column("request", ForeignKey("requests.id"))

    def __init__(self, amount, flavor, size, unit_price, request):
        self.amount = amount
        self.flavor = flavor
        self.size = size
        self.unit_price = unit_price
        self.request = request


# EXECUTA A CRIAÇAO DOS METODOS DO SEU BANCO DE DADOS - CRIA EFETIVAMENTE O BANCO DE DADOS
