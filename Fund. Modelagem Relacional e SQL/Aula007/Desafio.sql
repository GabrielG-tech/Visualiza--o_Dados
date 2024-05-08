-- Exemplo UNIQUE
CREATE TABLE alunos (
    id aluno INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    id_identificação TEXT UNIQUE
)
INSERT INTO alunos (nome, idade, id_identificacao) VALUES
    ('João', 15,123456),
    ('Maria', 16, 789012),
    ('Pedro', 14, 345678);
INSERT INTO alunos (nome, idade, id identificacao) VALUES
    ('Ana', 17, 123456;) -- Este registro não será inserido devido à restrição UNIQUE
SELECT * FROM alunos;

-- Exemplo NOT NULL
CREATE TABLE funcionarios (
    id_funcionario INTEGER PRIMARY KEY, Do
    nome TEXT,
    cargo TEXT,
    email TEXT NOT NULL
    )

INSERT INTO funcionarios (nome, cargo, email) VALUES
    ('João Silva', 'Analista de Vendas", "joao(Qexample.com'),
    ('Maria Santos', "Engenheira de Software", 'maria&Qexample.com'),
    ('Pedro Oliveira', 'Gerente de Projetos', 'pedro(Qexample.com');
INSERT INTO funcionarios (nome, cargo, email) VALUES
    ('Ana Lima', 'Analista de Marketing', NULL); -- Esta inserção será rejeitada devido à restrição NOT NULL
SELECT * FROM funcionarios:
