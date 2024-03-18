import sqlite3 
import os

def criar_tabela(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS visitantes (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, email TEXT)")

def inserir_visitante(cursor, nome, idade, email):
    cursor.execute("INSERT INTO visitantes (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))

def exibir_visitantes(cursor):
    cursor.execute("SELECT * FROM visitantes")
    visitantes = cursor.fetchall()
    for visitante in visitantes:
        print(visitante)

def menu():
    print("1. Inserir visitante")
    print("2. Exibir visitantes")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

# Verifica se a pasta "Desafio01_SQLite" existe e cria se não existir
if not os.path.exists("Desafio01_SQLite"):
    os.makedirs("Desafio01_SQLite")

# Estabelecendo a conexão com o banco de dados dentro da pasta "SQLite"
conn = sqlite3.connect('Desafio01_SQLite/banco.db')
cursor = conn.cursor()

criar_tabela(cursor)

# # Inserindo cadastros pré-preenchidos
# inserir_visitante(cursor, "João", 25, "joao@example.com")
# inserir_visitante(cursor, "Maria", 30, "maria@example.com")
# inserir_visitante(cursor, "Ana", 22, "ana@example.com")
# conn.commit()

while True:
    escolha = menu()
    if escolha == '1':
        nome = input("Digite o nome do visitante: ")
        idade = int(input("Digite a idade do visitante: "))
        email = input("Digite o email do visitante: ")
        inserir_visitante(cursor, nome, idade, email)
        conn.commit()
    elif escolha == '2':
        exibir_visitantes(cursor)
    elif escolha == '3':
        break
    else:
        print("Opção inválida!")

# Fechando a conexão
conn.close()
