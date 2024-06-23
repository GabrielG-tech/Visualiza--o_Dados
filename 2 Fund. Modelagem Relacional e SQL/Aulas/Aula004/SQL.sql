-- 1º Desafio
-- Em uma escola é necessário registrar os alunos que possuem os seguintes campos: id (PK), nome e idade e
-- uma tabela de cursos com os campos id (PK), nome e duração. Há uma tabela chamada inscrições que relaciona
-- estas duas através das chaves primárias. Faça o que se pede:
-- 1) Elabore um modelo DER para este problema;
-- 2) Faça o teste no SQLITE, incluindo registros em cada tabela;
-- 3) Consultar todos os alunos inscritos no curso de matemática;
-- 4) Consultar todos os cursos em que um aluno específico está inscrito;
-- 5) Consultar todas as inscrições feitas.
-- 6) Faça um programa Python que permita cadastrar alunos, cursos e verificar e fazer inscrições através da tabela
-- Inscrições.
-- Visual Paradigm Modelo ER
-- https://online.visual-paradigm.com/pt/diagrams/features/erd-tool/


CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    idade INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS cursos(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(255) UNIQUE NOT NULL,
    ducacao INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS INSCRICOES(
    aluno_id INTEGER,
    curso_id INTEGER,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    PRIMARY KEY(aluno_id, curso_id)
    );

INSERT INTO alunos(nome, idade) VALUES 
    ('João', 20),
    ('Renata', 30),
    ('Pedro', 40);

INSERT INTO cursos(nome, duracao) VALUES
    ('Matemática', 120),
    ('História', 100),
    ('Física', 80),
    ('Biologia', 80);

INSERT INTO inscricoes(aluno_id, curso_id) VALUES
    (1,1),
    (1,4),
    (2,2),
    (3,3),
    (3,1);

SELECT alunos.nome, curso.nome
FROM inscricoes
JOIN alunos ON inscricoes.aluno_id=alunos_id
JOIN cursos ON inscricoes.curso_id=cursos_id
WHERE cursos.nome='Matemática';

-- ou
-- SELECT alunos.nome
-- FROM alunos
-- INNER JOIN inscricoes
-- ON alunos.id=inscricoes.aluno_id
-- INNER JOIN cursos
-- ON inscricoes.curso_id=curso_id
-- WHERE cursos.nome='Matemática';

-- --------------------------------------

CREATE TABLE alunos (
	ID INTEGER PRIMARY KEY,
    nome varchar(255),
  	idade INTEGER
);

CREATE TABLE cursos (
	ID INTEGER PRIMARY KEY,
    nome varchar(255),
  	duração INTEGER
);

CREATE TABLE inscricoes (
  	alunoID INTEGER,
  	cursoID INTEGER,
  	FOREIGN KEY (alunoID) REFERENCES alunos(ID),
  	FOREIGN KEY (cursoID) REFERENCES cursos(ID),
  	PRIMARY KEY (alunoID, cursoID)
);

INSERT INTO alunos (nome, idade) VALUES
	("giovani", 19),
	("gabriel", 18);

INSERT INTO cursos (nome, duração) VALUES
	("Matemática", 50), 
	("Português", 50);

INSERT INTO inscricoes (alunoID, cursoID) VALUES
	(1,2), -- giovani inscrito em português
	(2,1); -- gabriel inscrito em matemática
	
SELECT alunos.nome AS nome_aluno
FROM alunos
JOIN inscricoes ON alunos.ID = inscricoes.alunoID
WHERE inscricoes.cursoID = 1; -- ID do curso de Matemática

SELECT cursos.nome AS nome_curso
FROM cursos
JOIN inscricoes ON cursos.ID = inscricoes.cursoID
WHERE inscricoes.alunoID = 1; -- ID do aluno giovani

SELECT * FROM inscricoes;

SELECT alunos.nome AS nome_aluno, cursos.nome AS nome_curso
FROM inscricoes
JOIN alunos ON inscricoes.alunoID = alunos.ID
JOIN cursos ON inscricoes.cursoID = cursos.ID;
