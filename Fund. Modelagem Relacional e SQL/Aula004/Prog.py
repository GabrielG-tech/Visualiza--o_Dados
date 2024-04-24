import sqlite3
import os

def inic_db():
    # Obtendo o caminho do diretório atual
    diretorio_atual = os.getcwd()
    
    # Criando o caminho completo para a pasta "Fund. Modelagem Relacional e SQL" dentro da pasta "Aula004"
    caminho_pasta = os.path.join(diretorio_atual, "Aula004", "Fund. Modelagem Relacional e SQL")
    
    # Criando o caminho completo para o banco de dados dentro da pasta específica
    caminho_banco = os.path.join(caminho_pasta, "exemplo.db")

    # Verificando se o diretório existe
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        print(f"Diretório {caminho_pasta} criado com sucesso.")

    try:
        # Estabelecendo a conexão com o banco de dados (se não existir, será criado)
        conn = sqlite3.connect(caminho_banco)
        print(f"Banco de dados {caminho_banco} conectado com sucesso.")

        # Criando um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Criando tabelas de alunos, cursos e inscrições
        cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                            id INTEGER PRIMARY KEY,
                            nome VARCHAR(255) NOT NULL,
                            idade INTEGER NOT NULL);''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS cursos (
                            id INTEGER PRIMARY KEY,
                            nome VARCHAR(255) UNIQUE NOT NULL,
                            duracao INTEGER NOT NULL);''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS inscricoes (
                            aluno_id INTEGER,
                            curso_id INTEGER,
                            FOREIGN KEY (aluno_id) REFERENCES alunos(id),
                            FOREIGN KEY (curso_id) REFERENCES cursos(id),
                            PRIMARY KEY(aluno_id, curso_id));''')

        # Commitando as alterações
        conn.commit()
        print("Tabelas criadas com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ou criar tabelas: {e}")
    finally:
        conn.close()

def listar_alunos():
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos;")

    alunos = cursor.fetchall()

    print()
    print('=========================')
    for aluno in alunos:
        print(aluno)
    print('=========================')
    print()

    conn.close()

def incluir_aluno():
    listar_alunos()

    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    nome = input("Nome: ")
    idade = input("Idade: ")

    cursor.execute("INSERT OR IGNORE INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade))

    conn.commit()
    conn.close()

def listar_cursos():
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cursos;")

    cursos = cursor.fetchall()

    print()
    print('=========================')
    for curso in cursos:
        print(curso)
    print('=========================')
    print()

    conn.close()

def incluir_curso():
    listar_cursos()

    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    nome = input("Nome do curso: ")
    duracao = input("Duração do curso: ")

    cursor.execute("INSERT OR IGNORE INTO cursos (nome, duracao) VALUES (?, ?)", (nome, duracao))

    conn.commit()
    conn.close()

def listar_inscricoes():
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT alunos.nome, cursos.nome FROM inscricoes JOIN alunos ON inscricoes.aluno_id = alunos.id JOIN cursos ON inscricoes.curso_id = cursos.id;")

    inscricoes = cursor.fetchall()

    print()
    print('=========================')
    for inscricao in inscricoes:
        print(inscricao)
    print('=========================')
    print()

    conn.close()

def incluir_inscricao():
    listar_alunos()
    listar_cursos()

    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    aluno_id = input("ID do aluno: ")
    curso_id = input("ID do curso: ")

    cursor.execute("INSERT OR IGNORE INTO inscricoes (aluno_id, curso_id) VALUES (?, ?)", (aluno_id, curso_id))

    conn.commit()
    conn.close()

# Programa principal
inic_db()

while True:
    print("==== SISTEMA DE INSCRIÇÕES ====")
    print("[1] Incluir aluno")
    print("[2] Incluir curso")
    print("[3] Incluir inscrição")
    print("[4] Listar alunos")
    print("[5] Listar cursos")
    print("[6] Listar inscrições")
    print("[7] Sair")
    inp = input("Escolha a opção: ")

    if inp == '1':
        incluir_aluno()
    elif inp == '2':
        incluir_curso()
    elif inp == '3':
        incluir_inscricao()
    elif inp == '4':
        listar_alunos()
    elif inp == '5':
        listar_cursos()
    elif inp == '6':
        listar_inscricoes()
    elif inp == '7':
        print("==== FIM DO PROGRAMA ====")
        break
    else:
        print("==== OPÇÃO INVÁLIDA!!! ====")
