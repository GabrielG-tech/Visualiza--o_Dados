-- Criar tabela Alunos
CREATE TABLE Alunos (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100)
);

-- Inserir dados na tabela Alunos
INSERT INTO Alunos (ID, Nome) VALUES
(1, 'João'),
(2, 'Maria');

-- Criar tabela Cursos
CREATE TABLE Cursos (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100)
);

-- Inserir dados na tabela Cursos
INSERT INTO Cursos (ID, Nome) VALUES
(1, 'Matemática'),
(2, 'Física'),
(3, 'Química'),
(4, 'Inglês'),
(5, 'História');

-- Criar tabela Matriculas com IDAluno como chave estrangeira
CREATE TABLE Matriculas (
    Aluno_ID INT,
    Curso_ID INT,
    PRIMARY KEY (Aluno_ID, Curso_ID),
    FOREIGN KEY (Aluno_ID) REFERENCES Alunos(ID),
    FOREIGN KEY (Curso_ID) REFERENCES Cursos(ID)
);

-- Inserir dados na tabela Matriculas
INSERT INTO Matriculas (Aluno_ID, Curso_ID) VALUES
(1, 1), -- João está matriculado em Matemática
(1, 2), -- João está matriculado em Física
(1, 3), -- João está matriculado em Química
(2, 4), -- Maria está matriculada em Inglês
(2, 5); -- Maria está matriculada em História
