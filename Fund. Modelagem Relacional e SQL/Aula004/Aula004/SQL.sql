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