import sqlite3 
import os

def criar_tabela(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios (id INTEGER PRIMARY KEY, nome TEXT, telefone TEXT, email TEXT, endereco TEXT, sexo TEXT, pix TEXT, horario_entrada TEXT, horario_saida TEXT, foto TEXT, cpf TEXT, dn TEXT, cartao TEXT, cargo TEXT)")

def inserir_funcionario(cursor, nome, telefone, email, endereco, sexo, pix, horario_entrada, horario_saida, foto, cpf, dn, cartao, cargo):
    cursor.execute("INSERT INTO funcionarios (nome, telefone, email, endereco, sexo, pix, horario_entrada, horario_saida, foto, cpf, dn, cartao, cargo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome, telefone, email, endereco, sexo, pix, horario_entrada, horario_saida, foto, cpf, dn, cartao, cargo))

def exibir_funcionarios(cursor):
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    for funcionario in funcionarios:
        print(f"Id: {funcionario[0]} Nome: {funcionario[1]} Cargo: {funcionario[13]} Horario Entrada: {funcionario[7]} Horario Saida: {funcionario[8]}")

def incluir(cursor):
    nome = input("Entre com o nome: ")
    telefone = input("Entre com o telefone: ")
    email = input("Entre com o email: ")
    endereco = input("Entre com o endereco: ")
    sexo = input("Entre com o sexo: ")
    pix = input("Entre com o pix: ")
    horario_entrada = input("Entre com o horario_entrada: ")
    horario_saida = input("Entre com o horario_saida: ")
    foto = input("Entre com o foto: ")
    cpf = input("Entre com o cpf: ")
    dn = input("Entre com o dn: ")
    cartao = input("Entre com o cartao: ")
    cargo = input("Entre com o cargo: ")
    inserir_funcionario(cursor, nome, telefone, email, endereco, sexo, pix, horario_entrada, horario_saida, foto, cpf, dn, cartao, cargo)
    conn.commit()

def listar(cursor):
    exibir_funcionarios(cursor)

def menu():
    print("\n" + "="*8 + " Sistema de Ponto " + "="*8)
    print("[1] - Incluir")
    print("[2] - Listar")
    print("[3] - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

# Verifica se a pasta "PontoEletronico" existe e cria se não existir
if not os.path.exists("Aula17/PontoEletronico"):
    os.makedirs("Aula17/PontoEletronico")

# Estabelecendo a conexão com o banco de dados dentro da pasta "SQLite"
conn = sqlite3.connect('Aula17/PontoEletronico/banco.db')
cursor = conn.cursor()

criar_tabela(cursor)

# Inserindo cadastros pré-preenchidos
inserir_funcionario(cursor, "Gabriel", "(21) 9 8765-1848", "gabriel@email.com", "Casa dos bobos nº0", "Masculino", "(21) 9 87645-1848", "13:00:00", "19:00:00", "imagem", "123.456.789-00", "11/07/2003", "123456789", "Estágiario de Desenvolvimento")
inserir_funcionario(cursor, "Ronaldo", "(21) 9 8765-1848", "ronaldo@email.com", "Casa dos bobos nº2", "Masculino", "(21) 9 87645-1849", "10:30:00", "19:30:00", "imagem", "123.456.789-00", "15/08/1994", "123456799", "Analista")
conn.commit()

while True:
    escolha = menu()
    if escolha == '1':
        incluir(cursor)
    elif escolha == '2':
        listar(cursor)
    elif escolha == '3':
        break
    else:
        print("Opção inválida!")

# Fechando a conexão
conn.close()
