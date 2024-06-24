import sqlite3

PATH = '2 Fund. Modelagem Relacional e SQL/AT/Ex03/'
NOME_DB = "universidade"

def criar_tabelas():
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno (
        id_aluno INTEGER PRIMARY KEY,
        nome_aluno TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS disciplina (
        id_disciplina INTEGER PRIMARY KEY,
        nome_disciplina TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS matricula (
        id_aluno INTEGER,
        id_disciplina INTEGER,
        FOREIGN KEY (id_aluno) REFERENCES aluno (id_aluno),
        FOREIGN KEY (id_disciplina) REFERENCES disciplina (id_disciplina),
        PRIMARY KEY (id_aluno, id_disciplina)
    )
    ''')

    conn.commit()
    conn.close()

def inserir_dados():
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM aluno')
    if cursor.fetchone()[0] == 0:
        alunos = [(1, 'Alice'), (2, 'Bob'), (3, 'Carol')]
        cursor.executemany('INSERT INTO aluno (id_aluno, nome_aluno) VALUES (?, ?)', alunos)

    cursor.execute('SELECT COUNT(*) FROM disciplina')
    if cursor.fetchone()[0] == 0:
        disciplinas = [(1, 'Matemática'), (2, 'Física'), (3, 'Química'), (4, 'Biologia')]
        cursor.executemany('INSERT INTO disciplina (id_disciplina, nome_disciplina) VALUES (?, ?)', disciplinas)

    cursor.execute('SELECT COUNT(*) FROM matricula')
    if cursor.fetchone()[0] == 0:
        matriculas = [(1, 1), (1, 2), (2, 3), (3, 4), (3, 3), (3, 1)]
        cursor.executemany('INSERT INTO matricula (id_aluno, id_disciplina) VALUES (?, ?)', matriculas)

    conn.commit()
    conn.close()

def cadastrar_aluno():
    id_aluno = int(input("Digite o ID do aluno: "))
    nome_aluno = input("Digite o nome do aluno: ")
    
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO aluno (id_aluno, nome_aluno) VALUES (?, ?)', (id_aluno, nome_aluno))
    conn.commit()
    conn.close()
    print("Aluno cadastrado com sucesso!")

def cadastrar_disciplina():
    id_disciplina = int(input("Digite o ID da disciplina: "))
    nome_disciplina = input("Digite o nome da disciplina: ")

    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO disciplina (id_disciplina, nome_disciplina) VALUES (?, ?)', (id_disciplina, nome_disciplina))
    conn.commit()
    conn.close()
    print("Disciplina cadastrada com sucesso!")

def matricular_aluno():
    id_aluno = int(input("Digite o ID do aluno: "))
    id_disciplina = int(input("Digite o ID da disciplina: "))

    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO matricula (id_aluno, id_disciplina) VALUES (?, ?)', (id_aluno, id_disciplina))
    conn.commit()
    conn.close()
    print("Aluno matriculado com sucesso!")

def imprimir_alunos():
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM aluno')
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(aluno)
    conn.close()

def imprimir_disciplinas():
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM disciplina')
    disciplinas = cursor.fetchall()
    for disciplina in disciplinas:
        print(disciplina)
    conn.close()

def imprimir_disciplinas_aluno():
    id_aluno = int(input("Digite o ID do aluno: "))
    
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT d.nome_disciplina FROM disciplina d
    JOIN matricula m ON d.id_disciplina = m.id_disciplina
    WHERE m.id_aluno = ?
    ''', (id_aluno,))
    disciplinas = cursor.fetchall()
    for disciplina in disciplinas:
        print(disciplina)
    conn.close()

def imprimir_alunos_disciplina():
    id_disciplina = int(input("Digite o ID da disciplina: "))

    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT a.nome_aluno FROM aluno a
    JOIN matricula m ON a.id_aluno = m.id_aluno
    WHERE m.id_disciplina = ?
    ''', (id_disciplina,))
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(aluno)
    conn.close()

def mostrar_menu():
    print("\nMenu:")
    print("1. Cadastrar aluno")
    print("2. Cadastrar disciplina")
    print("3. Matricular aluno em disciplina")
    print("4. Imprimir todos os alunos")
    print("5. Imprimir todas as disciplinas")
    print("6. Imprimir todas as disciplinas de um aluno")
    print("7. Imprimir todos os alunos de uma disciplina")
    print("8. Sair")

criar_tabelas()
inserir_dados()

while True:
    mostrar_menu()

    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            cadastrar_aluno()
        elif escolha == 2:
            cadastrar_disciplina()
        elif escolha == 3:
            matricular_aluno()
        elif escolha == 4:
            imprimir_alunos()
        elif escolha == 5:
            imprimir_disciplinas()
        elif escolha == 6:
            imprimir_disciplinas_aluno()
        elif escolha == 7:
            imprimir_alunos_disciplina()
        elif escolha == 8:
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
    except ValueError:
        print("Por favor, digite um número correspondente à opção desejada.")
