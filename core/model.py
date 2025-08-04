cur.execute("""
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
            """)