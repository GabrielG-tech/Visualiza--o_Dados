-- Implementar com Python *

-- Inserindo dados na tabela de produtos
INSERT OR IGNORE INTO produtos (nome, preco, estoque) VALUES
('Produto A', 10.99, 100),
('Produto B', 20.49, 50),
('Produto C', 15.75, 75);

-- Inserindo dados na tabela de clientes
INSERT OR IGNORE INTO clientes (nome, email, endereco) VALUES
('Cliente 1', 'clientelCexample.com', 'Rua A, 123'),
('Cliente 2', 'cliente2Cexample.com', 'Av. B, 456'),
('Cliente 3', 'cliente3Cexample.com', 'Praça C, 789');

-- Inserindo dados na tabela de pedidos
INSERT OR IGNORE INTO pedidos (id_cliente, data_pedido) VALUES
    (1, '2024-05-01'),
    (2, '2024-05-05'),
    (3, '2024-04-10');

-- Inserindo dados na tabela de detalhes_pedido
INSERT OR IGNORE INTO detalhes_pedido (id pedido, id produto,
quantidade) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 3),
(3, 1, 1),
(3, 2, 2),
(3, 3, 1);

-- Ex E
SELECT clientes.nome AS nome_cliente,
SUM(produtos.preco * detalhes pedido.quantidade) AS total_gasto
FROM clientes
JOIN pedidos ON clientes.id = pedidos.id cliente
JOIN detalhes_pedido ON pedidos.id = detalhes_pedido.id_pedido
JOIN produtos ON detalhes_pedido.id_produto = produtos.id
GROUP BY clientes.id;

-- Ex F
SELECT *
FROM produtos
WHERE preco < 20;

-- Ex G
SELECT DISTINCT clientes.nome AS nome_cliente
FROM clientes
JOIN pedidos ON clientes.id = pedidos.id_cliente
WHERE pedidos.data_pedido BETWEEN date('2024-04-04') AND
date('now');|
