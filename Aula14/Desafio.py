# 1) Elabore uma tabela do Python com os campos ID e valor. Em seguida, insira 1.000.000 registros randômicos 1 a 100 no mesmo. Finalmente, meça a performance da tabela usando o BETWEEN e OPERADOR RELACIONAL para buscar valores entre 30 e 70 e veja qual o método de busca é mais eficiente.

import sqlite3
import random
import time
 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn
 
def create_table(conn):
    sql_create_table = """CREATE TABLE IF NOT EXISTS dados (
                            id INTEGER PRIMARY KEY,
                            valor INTEGER NOT NULL
                        );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except sqlite3.Error as e:
        print(e)
 
def insert_random_data(conn, num_records):
    try:
        c = conn.cursor()
        for _ in range(num_records):
            valor = random.randint(1, 100)
            c.execute("INSERT INTO dados (valor) VALUES (?)", (valor,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
 
def measure_between_performance(conn):
    start_time = time.time()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM dados WHERE valor BETWEEN 30 AND 70")
    count = c.fetchone()[0]
    end_time = time.time()
    return count, end_time - start_time
 
def measure_relational_operator_performance(conn):
    start_time = time.time()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM dados WHERE valor >= 30 AND valor <= 70")
    count = c.fetchone()[0]
    end_time = time.time()
    return count, end_time - start_time
 
def main():
    database = r"C:\\Users\\gabriel.gsouza\\Documents\\Visualização_Dados\\Aula14\\dados.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        insert_random_data(conn, 1000000)
        count_between, time_between = measure_between_performance(conn)
        count_relational, time_relational = measure_relational_operator_performance(conn)
        print("Consulta usando BETWEEN:")
        print("Número de registros encontrados:", count_between)
        print("Tempo de execução:", time_between, "segundos")
        print("\nConsulta usando OPERADOR RELACIONAL:")
        print("Número de registros encontrados:", count_relational)
        print("Tempo de execução:", time_relational, "segundos")
        conn.close()
    else:
        print("Erro! Não foi possível criar a conexão com o banco de dados.")
 
if __name__ == '__main__':
    main()
