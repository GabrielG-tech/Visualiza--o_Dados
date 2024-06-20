CREATE TABLE IF NOT EXISTS livro (
  LivroID INTEGER PRIMARY KEY,
  Titulo VARCHAR(100) NOT NULL,
  Preco FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS autor (
  AutorID INTEGER PRIMARY KEY,
  AutorNome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS categoria (
  CategoriaID INTEGER PRIMARY KEY,
  CategoriaNome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS editora (
  EditoraID INTEGER PRIMARY KEY,
  EditoraNome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS livraria (
  LivroID INTEGER NOT NULL,
  AutorID INTEGER NOT NULL,
  CategoriaID INTEGER NOT NULL,
  EditoraID INTEGER NOT NULL,
  FOREIGN KEY (LivroID) REFERENCES livro(LivroID),
  FOREIGN KEY (AutorID) REFERENCES autor(AutorID),
  FOREIGN KEY (CategoriaID) REFERENCES categoria(CategoriaID),
  FOREIGN KEY (EditoraID) REFERENCES editora(EditoraID),
  PRIMARY KEY (LivroID, AutorID, CategoriaID, EditoraID)
);

INSERT INTO livro (Titulo, Preco) VALUES 
('Dom Quixote', 50.00),
('Guerra e Paz', 60.00),
('O Hobbit', 45.00),
('1984', 40.00),
('O Senhor dos Anéis', 70.00);

INSERT INTO autor (AutorID, AutorNome) VALUES 
(101, 'Miguel de Cervantes'),
(102, 'Liev Tolstói'),
(103, 'J.R.R. Tolkien'),
(104, 'George Orwell');

INSERT INTO categoria (CategoriaNome) VALUES
('Romance'),
('Fantasia'),
('Distopia');

INSERT INTO editora (EditoraID, EditoraNome) VALUES 
(201, 'Editora A'),
(202, 'Editora B'),
(203, 'Editora C');

INSERT INTO livraria (LivroID, AutorID, CategoriaID, EditoraID) VALUES
(1,101,1,201),
(2,102,1,202),
(3,103,2,201),
(4,104,3,203),
(5,103,2,201);

SELECT 
L.LivroID AS LivroID, 
L.Titulo AS Titulo,
A.AutorID AS AutorID,
A.AutorNome AS AutorNome,
C.CategoriaID AS CategoriaID,
C.CategoriaNome AS CategoriaNome,
E.EditoraID AS EditoraID,
E.EditoraNome AS EditoraNome, 
L.Preco AS Preco
FROM livraria LIV
JOIN livro L ON L.LivroID = LIV.LivroID
JOIN autor A ON A.AutorID = LIV.AutorID
JOIN categoria C ON C.CategoriaID = LIV.CategoriaID
JOIN editora E ON E.EditoraID = LIV.EditoraID;