import sqlite3

PATH = '2 Fund. Modelagem Relacional e SQL\\AT\\Ex02\\'
NOME_DB = 'biblioteca'

def criar_bd():
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Autor (
        ID_Autor INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Data_Nascimento TEXT,
        Nacionalidade TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livro (
        ID_Livro INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo TEXT NOT NULL,
        Ano_Publicacao INTEGER,
        Genero TEXT,
        ID_Autor INTEGER,
        FOREIGN KEY(ID_Autor) REFERENCES Autor(ID_Autor)
    )
    ''')

    conn.commit()
    conn.close()

# Funções de CRUD para Autores
def cadastrar_autor(nome, data_nascimento, nacionalidade):
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Autor (Nome, Data_Nascimento, Nacionalidade)
    VALUES (?, ?, ?)
    ''', (nome, data_nascimento, nacionalidade))

    conn.commit()
    conn.close()

def editar_autor(id_autor, nome, data_nascimento, nacionalidade):
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE Autor
    SET Nome = ?, Data_Nascimento = ?, Nacionalidade = ?
    WHERE ID_Autor = ?
    ''', (nome, data_nascimento, nacionalidade, id_autor))

    conn.commit()
    conn.close()

def excluir_autor(id_autor):
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM Autor WHERE ID_Autor = ?
    ''', (id_autor,))

    conn.commit()
    conn.close()

# Funções de CRUD para Livros
def cadastrar_livro(titulo, ano_publicacao, genero, id_autor):
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Livro (Titulo, Ano_Publicacao, Genero, ID_Autor)
    VALUES (?, ?, ?, ?)
    ''', (titulo, ano_publicacao, genero, id_autor))

    conn.commit()
    conn.close()

def editar_livro(id_livro, titulo, ano_publicacao, genero, id_autor):
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE Livro
    SET Titulo = ?, Ano_Publicacao = ?, Genero = ?, ID_Autor = ?
    WHERE ID_Livro = ?
    ''', (titulo, ano_publicacao, genero, id_autor, id_livro))

    conn.commit()
    conn.close()

def excluir_livro(id_livro):
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM Livro WHERE ID_Livro = ?
    ''', (id_livro,))

    conn.commit()
    conn.close()

# Funções para listar autores e livros
def listar_autores():
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Autor')
    autores = cursor.fetchall()

    conn.close()
    return autores

def listar_livros():
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Livro')
    livros = cursor.fetchall()

    conn.close()
    return livros

def listar_livros_por_autor(id_autor):
    conn = sqlite3.connect(f'{PATH}{NOME_DB}.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM Livro WHERE ID_Autor = ?
    ''', (id_autor,))
    livros = cursor.fetchall()

    conn.close()
    return livros

def mostrar_menu():
    print("\nMenu:")
    print("[1] Cadastrar autor")
    print("[2] Cadastrar livro")
    print("[3] Editar autor")
    print("[4] Excluir autor")
    print("[5] Editar livro")
    print("[6] Excluir livro")
    print("[7] Listar todos os autores")
    print("[8] Listar todos os livros")
    print("[9] Listar livros por autor")
    print("[0] Sair")

criar_bd()

# cadastrar_autor("J.K. Rowling", "1965-07-31", "Britânica")
# cadastrar_autor("George R.R. Martin", "1948-09-20", "Americano")

# cadastrar_livro("Harry Potter e a Pedra Filosofal", 1997, "Fantasia", 1)
# cadastrar_livro("Harry Potter e a Câmara Secreta", 1998, "Fantasia", 1)
# cadastrar_livro("A Guerra dos Tronos", 1996, "Fantasia", 2)
# cadastrar_livro("A Fúria dos Reis", 1998, "Fantasia", 2)

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do autor: ")
        data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
        nacionalidade = input("Nacionalidade: ")
        cadastrar_autor(nome, data_nascimento, nacionalidade)
    elif opcao == '2':
        titulo = input("Título do livro: ")
        ano_publicacao = int(input("Ano de publicação: "))
        genero = input("Gênero: ")
        id_autor = int(input("ID do autor: "))
        cadastrar_livro(titulo, ano_publicacao, genero, id_autor)
    elif opcao == '3':
        id_autor = int(input("ID do autor: "))
        nome = input("Nome do autor: ")
        data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
        nacionalidade = input("Nacionalidade: ")
        editar_autor(id_autor, nome, data_nascimento, nacionalidade)
    elif opcao == '4':
        id_autor = int(input("ID do autor: "))
        excluir_autor(id_autor)
    elif opcao == '5':
        id_livro = int(input("ID do livro: "))
        titulo = input("Título do livro: ")
        ano_publicacao = int(input("Ano de publicação: "))
        genero = input("Gênero: ")
        id_autor = int(input("ID do autor: "))
        editar_livro(id_livro, titulo, ano_publicacao, genero, id_autor)
    elif opcao == '6':
        id_livro = int(input("ID do livro: "))
        excluir_livro(id_livro)
    elif opcao == '7':
        autores = listar_autores()
        for autor in autores:
            print(autor)
    elif opcao == '8':
        livros = listar_livros()
        for livro in livros:
            print(livro)
    elif opcao == '9':
        id_autor = int(input("ID do autor: "))
        livros = listar_livros_por_autor(id_autor)
        for livro in livros:
            print(livro)
    elif opcao == '0':
        print("Fim do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")
