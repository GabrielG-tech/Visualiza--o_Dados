#*  *   *   *   *   *   *   *
#*   Programa agendamento   *
#*  *   *   *   *   *   *   *
import sqlite3
import sys
import re
import os

# Nome da pasta onde o arquivo será gerado
pasta_resultados = "C:\\Users\\gabriel.gsouza\\Documents\\Visualização_Dados\\Aula14\\RegX_CRUD"

# Verifica se a pasta existe, senão a cria
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)

# Nome do arquivo de saída
nome_arquivo = os.path.join(pasta_resultados, "cadastros.db")

# Inicialização de DB
def inic_db():
    conn = sqlite3.connect(nome_arquivo)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS visitantes
                  (id INTEGER PRIMARY KEY,
                   nome VARCHAR(100),
                   telefone VARCHAR(20),
                   email VARCHAR(50),
                   idade INTEGER,
                   sexo VARCHAR(1),
                   data_agendamento VARCHAR(10),
                   especialidade VARCHAR(50))''')    
    return

# Incluir dados
def incluir_db():
    conn = sqlite3.connect(nome_arquivo)
    cursor = conn.cursor()
    nome=input("Nome: ")
    padrao = r'^\(\d{2}\)\d{5}-\d{4}$'
    telefone=''
    while not re.match(padrao, telefone):
        telefone=input("Telefone: ")
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'    
    email=''
    while not re.match(padrao, email):
        email=input("E-mail: ")
    idade=input("idade: ")
    sexo=input("Sexo (M/F): ")
    padrao = r'^\d{2}/\d{2}/\d{4}$'
    data_agendamento=''
    while not re.match(padrao, data_agendamento):
        data_agendamento=input("Data de agendamento (DD/MM/AAAA): ")
    especialidade=input("Especialidade: ")
    cursor.execute("INSERT INTO visitantes (nome, telefone, email,idade,sexo,data_agendamento,especialidade) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome,telefone,email,idade,sexo,data_agendamento,especialidade))
    conn.commit()
    return

# Listar dados
def listar_db():
    conn = sqlite3.connect(nome_arquivo)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM visitantes")
    pessoas = cursor.fetchall()
    print("\n"+ 30*"=" + " AGENDAMENTO CLÍNICA MÉDICA " + 30*"=")
    print("ID | nome | telefone | email | sexo | idade | data de agendamento | especialidade")
    for pessoa in pessoas:
        print(pessoa)
    print(88*"="+"\n")
    return

# Excluir dados
def excluir_db():
    listar_db()
    conn = sqlite3.connect(nome_arquivo)
    cursor = conn.cursor()
    idv=input("Escolha o ID a remover:")
    cursor.execute("DELETE FROM visitantes WHERE id=?",idv)
    conn.commit()
    listar_db()    
    return

# Atualizar dados
def atualizar_db():
    listar_db()
    conn = sqlite3.connect(nome_arquivo)
    cursor = conn.cursor()
    idv=input("Escolha o ID a atualizar:")
    print("==== CAMPO A ATUALIZAR ====")
    print("[1] Nome")
    print("[2] Telefone")
    print("[3] Email")
    print("[4] Idade")
    print("[5] Sexo")
    print("[6] Data de agendamento")
    print("[7] Especialidade")
    inp=input("\nEscolha a opção: ")
    novo=input("Novo dado: ")
    if (inp=='1'):
        cursor.execute("UPDATE visitantes SET nome=? WHERE id=?",(novo,idv))
        conn.commit()
    elif (inp=='2'):
        cursor.execute("UPDATE visitantes SET telefone=? WHERE id=?",(novo,idv))
        conn.commit()
    elif (inp=='3'):
        cursor.execute("UPDATE visitantes SET email=? WHERE id=?",(novo,idv))
        conn.commit()
    elif (inp=='4'):
        cursor.execute("UPDATE visitantes SET idade=? WHERE id=?",(novo,idv))
        conn.commit()
    elif (inp=='5'):
        cursor.execute("UPDATE visitantes SET sexo=? WHERE id=?",(novo,idv))
        conn.commit()
    elif (inp=='6'):
        cursor.execute("UPDATE visitantes SET data_agendamento=? WHERE id=?",(novo,idv))
        conn.commit()
    elif (inp=='7'):
        cursor.execute("UPDATE visitantes SET especialidade=? WHERE id=?",(novo,idv))
        conn.commit()
    else:
        print("Opção não cadastrada!!!")
    listar_db()    
    return

# Função para criar alguns cadastros por padrão
def criar_cadastros_padrao():
    conn = sqlite3.connect(nome_arquivo)
    cursor = conn.cursor()
    cadastros_padrao = [
        ("João", "(12)12345-6789", "joao@example.com", 30, "M", "10/03/2024", "Cardiologia"),
        ("Maria", "(21)98765-4321", "maria@example.com", 25, "F", "12/03/2024", "Pediatria"),
        ("José", "(34)56789-1234", "jose@example.com", 40, "M", "15/03/2024", "Ortopedia")
    ]
    cursor.executemany("INSERT INTO visitantes (nome, telefone, email, idade, sexo, data_agendamento, especialidade) VALUES (?, ?, ?, ?, ?, ?, ?)", cadastros_padrao)
    conn.commit()

# Programa principal
inic_db()
criar_cadastros_padrao()
while True:
    print("==== AGENDAMENTO CLÍNICA MÉDICA ====")
    print("[1] Incluir")
    print("[2] Listar")
    print("[3] Excluir")
    print("[4] Atualizar")
    print("[5] Sair")
    inp=input("\nEscolha a opção: ")
    if (inp=='1'):
        incluir_db()
    elif (inp=='2'):
        listar_db()
    elif (inp=='3'):
        excluir_db()
    elif (inp=='4'):
        atualizar_db()
    elif (inp=='5'):
        n = "="*4
        print(n+" FIM DO PROGRAMA AGENDAMENTO CLÍNICA MÉDICA "+n)        
        sys.exit()
    else:
        print("Opção inválida")