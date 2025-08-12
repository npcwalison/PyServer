from core.models import db
from sqlalchemy.orm import sessionmaker


def catch_session():
    try:
        Session = sessionmaker(bind=db) # Criando ao conexão com banco de dados
        session = Session() # Abrindo uma sessão com banco de dados
        yield session # retorna o valor, sem rodar o codigo abaixo
    finally: # faz com se essa parte roda mesmo que o yield trave
        session.close() # Ferchar sessão