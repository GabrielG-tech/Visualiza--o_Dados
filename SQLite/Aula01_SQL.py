import sqlite3 # pip install db-sqlite3       Dia: 18/03/2024
import os

# Verifica se a pasta "SQLite" existe e cria se não existir
if not os.path.exists("SQLite"):
    os.makedirs("SQLite")

# Estabelecendo a conexão com o banco de dados dentro da pasta "SQLite"
conn = sqlite3.connect('SQLite/exemplo.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Criando uma tabela chamada pessoas"
cursor.execute( "CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)")

# Inserindo alguns dados na tabela
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ('João', 25))
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ('Maria', 30))
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ('Ana', 22))

# Commitando as ateraçõesna
conn.commit()

# Lendo os dados da tabela
cursor.execute("SELECT * FROM pessoas")
pessoas = cursor.fetchall()

# Exibindo os dados lidos
for pessoa in pessoas:
    print(pessoa)

# Fechando a conexão
conn.close()