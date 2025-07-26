import psycopg2
from .get_connection import get_connection

def create_user_table():
    conn = get_connection()
    if conn is None:
        print(f"Não foi possivel conectar ao banco de dados: {e}")
        return
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usarios (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                name VARCHAR(100),
                sector VARCHAR(50),
                wage NUMERIC(15, 4)
            );
        """)

        conn.commit()
        print("Tabela 'usuarios' criada com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        if conn:
            conn.close()