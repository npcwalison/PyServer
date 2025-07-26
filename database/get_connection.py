import psycopg2


def get_connection():
    # trabalho 192.168.82.22
    # casa 172.28.122.156
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Roxo#800",
            host="172.28.122.156",
            port=5432
        )
        print("Conexão bem-sucedida!")
        return conn
    except psycopg2.Error as e:
        print(f"Error ao conectar ao banco de dados: {e}")
        return None
