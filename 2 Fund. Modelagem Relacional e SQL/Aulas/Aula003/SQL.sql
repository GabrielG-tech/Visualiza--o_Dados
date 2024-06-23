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