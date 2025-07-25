import psycopg2


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Roxo#800",
            host="192.168.82.22",
            port=5432
        )
        print("Conexão bem-sucedida!")
        return conn
    except psycopg2.Error as e:
        print(f"Error ao conectar ao banco de dados: {e}")
        return None

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


create_user_table()

