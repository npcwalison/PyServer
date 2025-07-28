import psycopg2
from .get_connection import get_connection

def create_user_table():
    try:
        conn = get_connection()
        if conn is None:
            print(f"Não foi possivel conectar ao banco de dados!")
            return
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS gti_sectors (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    sc_name VARCHAR(100),
                );
                CREATE TABLE IF NOT EXISTS gti_users (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    name VARCHAR(100),
                    sr_email VARCHAR(100),
                    sr_sector VARCHAR(50),
                    sector_id_sector INT --FK
                );
                CREATE TABLE IF NOT EXISTS gti_machines (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    mh_name VARCHAR(100),
                    mh_system_op VARCHAR(45),
                    mh_motherboard VARCHAR(100),
                    mh_processor VARCHAR(100),
                    mh_memory_ram VARCHAR(100),
                    mh_storege VARCHAR(100),
                    sector_id_sector VARCHAR(50),
                );
                CREATE TABLE IF NOT EXISTS gti_events (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    vt_name VARCHAR(100),
                    vt_sector VARCHAR(50),
                    vt_wage NUMERIC(15, 4)
                );
                CREATE TABLE IF NOT EXISTS users_has_machines (
                    user_id_user INT --FK
                    machines_id_machines INT --FK
                )
            """)

            conn.commit()
            print("Tabela 'usuarios' criada com sucesso!")
        except psycopg2.Error as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            if conn:
                conn.close()
    except Exception as e:
        print(f"Não foi possivel conectar ao banco de dados: {e}")