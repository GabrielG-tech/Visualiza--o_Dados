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

    cursor.execute("INSERT INTO autores (id_autor, nome) VALUES (1, 'Fyodor Dostoyevsky')")
    cursor.execute("INSERT INTO autores (id_autor, nome) VALUES (2, 'George Orwell')")
    cursor.execute("INSERT INTO autores (id_autor, nome) VALUES (3, 'Franz Kafka')")
    cursor.execute("INSERT INTO autores (id_autor, nome) VALUES (4, 'Antoine de Saint-Exupéry')")

    cursor.execute("INSERT INTO categorias (id_categoria, categoria) VALUES (1, 'Ficção')")

    cursor.execute("INSERT INTO editoras (id_editora, editora, pais_publicacao) VALUES (1, 'Penguin Books', 'Rússia')")
    cursor.execute("INSERT INTO editoras (id_editora, editora, pais_publicacao) VALUES (2, 'Vintage Books', 'Áustria')")
    cursor.execute("INSERT INTO editoras (id_editora, editora, pais_publicacao) VALUES (3, 'Penguin Books', 'Reino Unido')")
    cursor.execute("INSERT INTO editoras (id_editora, editora, pais_publicacao) VALUES (4, 'Vintage Books', 'França')")

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

criar_banco()
# inserir_dados_exemplo()
# cadastrar_categoria('Romance')
# cadastrar_autor('Machado de Assis')
# cadastrar_editora('Livraria Garnier', 'Brasil')
# cadastrar_livro('Dom Casmurro', 5, 2, 5)
# cadastrar_autor('Dan Brown')
# cadastrar_livro('O Código Da Vinci', 6, 1, 4)

print("Todos os livros:")
imprimir_todos_livros()
print("\nTodos os autores:")
imprimir_todos_autores()
print("\nTodas as categorias:")
imprimir_todas_categorias()
print("\nTodas as editoras:")
imprimir_todas_editoras()
print("\nLivros publicados pelo autor 1:")
imprimir_livros_por_autor(6)

# Fazer menu e fazer mostrar por livro, categoria e obras do autor