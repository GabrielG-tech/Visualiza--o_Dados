import sqlite3

PATH = '2 Fund. Modelagem Relacional e SQL\\AT\\Ex04\\'
NOME_DB = 'biblioteca.db'
DATABASE = PATH + NOME_DB

def criar_banco():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS autores (
                        id_autor INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
                        id_categoria INTEGER PRIMARY KEY,
                        categoria TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS editoras (
                        id_editora INTEGER PRIMARY KEY,
                        editora TEXT NOT NULL,
                        pais_publicacao TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id_livro INTEGER PRIMARY KEY,
                        titulo TEXT NOT NULL,
                        id_autor INTEGER NOT NULL,
                        id_categoria INTEGER NOT NULL,
                        id_editora INTEGER NOT NULL,
                        FOREIGN KEY(id_autor) REFERENCES autores(id_autor),
                        FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria),
                        FOREIGN KEY(id_editora) REFERENCES editoras(id_editora))''')

    conn.commit()
    conn.close()

def inserir_dados_exemplo():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM autores")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO autores (id_autor, nome) VALUES (1, 'Fyodor Dostoyevsky')")
        cursor.execute("INSERT INTO autores (id_autor, nome) VALUES (2, 'George Orwell')")
        cursor.execute("INSERT INTO autores (id_autor, nome) VALUES (3, 'Franz Kafka')")
        cursor.execute("INSERT INTO autores (id_autor, nome) VALUES (4, 'Antoine de Saint-Exupéry')")

    cursor.execute("SELECT COUNT(*) FROM categorias")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO categorias (id_categoria, categoria) VALUES (1, 'Ficção')")

    cursor.execute("SELECT COUNT(*) FROM editoras")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO editoras (id_editora, editora, pais_publicacao) VALUES (1, 'Penguin Books', 'Rússia')")
        cursor.execute("INSERT INTO editoras (id_editora, editora, pais_publicacao) VALUES (2, 'Vintage Books', 'Áustria')")
        cursor.execute("INSERT INTO editoras (id_editora, editora, pais_publicacao) VALUES (3, 'Penguin Books', 'Reino Unido')")
        cursor.execute("INSERT INTO editoras (id_editora, editora, pais_publicacao) VALUES (4, 'Vintage Books', 'França')")

    cursor.execute("SELECT COUNT(*) FROM livros")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO livros (id_livro, titulo, id_autor, id_categoria, id_editora) VALUES (1, 'Crime e Castigo', 1, 1, 1)")
        cursor.execute("INSERT INTO livros (id_livro, titulo, id_autor, id_categoria, id_editora) VALUES (2, '1984', 2, 1, 1)")
        cursor.execute("INSERT INTO livros (id_livro, titulo, id_autor, id_categoria, id_editora) VALUES (3, 'O Processo', 3, 1, 2)")
        cursor.execute("INSERT INTO livros (id_livro, titulo, id_autor, id_categoria, id_editora) VALUES (4, 'O Pequeno Príncipe', 4, 1, 2)")

    conn.commit()
    conn.close()

def cadastrar_livro(titulo, id_autor, id_categoria, id_editora):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (titulo, id_autor, id_categoria, id_editora) VALUES (?, ?, ?, ?)",
                   (titulo, id_autor, id_categoria, id_editora))
    conn.commit()
    conn.close()

def cadastrar_autor(nome):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO autores (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

def cadastrar_categoria(categoria):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categorias (categoria) VALUES (?)", (categoria,))
    conn.commit()
    conn.close()

def cadastrar_editora(editora, pais_publicacao):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO editoras (editora, pais_publicacao) VALUES (?, ?)", (editora, pais_publicacao))
    conn.commit()
    conn.close()

def imprimir_todos_livros():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def imprimir_todos_autores():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autores")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def imprimir_todas_categorias():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def imprimir_todas_editoras():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM editoras")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def imprimir_livros_por_autor(id_autor):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE id_autor=?", (id_autor,))
    for row in cursor.fetchall():
        print(row)
    conn.close()

def menu():
    criar_banco()
    inserir_dados_exemplo()
    while True:
        print("\nMenu:")
        print("[1] Imprimir todos os livros")
        print("[2] Imprimir todos os autores")
        print("[3] Imprimir todas as categorias")
        print("[4] Imprimir todas as editoras")
        print("[5] Imprimir livros por autor")
        print("[6] Cadastrar novo livro")
        print("[7] Cadastrar novo autor")
        print("[8] Cadastrar nova categoria")
        print("[9] Cadastrar nova editora")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            imprimir_todos_livros()
        elif opcao == "2":
            imprimir_todos_autores()
        elif opcao == "3":
            imprimir_todas_categorias()
        elif opcao == "4":
            imprimir_todas_editoras()
        elif opcao == "5":
            id_autor = int(input("Digite o ID do autor: "))
            imprimir_livros_por_autor(id_autor)
        elif opcao == "6":
            titulo = input("Digite o título do livro: ")
            id_autor = int(input("Digite o ID do autor: "))
            id_categoria = int(input("Digite o ID da categoria: "))
            id_editora = int(input("Digite o ID da editora: "))
            cadastrar_livro(titulo, id_autor, id_categoria, id_editora)
        elif opcao == "7":
            nome = input("Digite o nome do autor: ")
            cadastrar_autor(nome)
        elif opcao == "8":
            categoria = input("Digite a categoria: ")
            cadastrar_categoria(categoria)
        elif opcao == "9":
            editora = input("Digite o nome da editora: ")
            pais_publicacao = input("Digite o país de publicação: ")
            cadastrar_editora(editora, pais_publicacao)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
