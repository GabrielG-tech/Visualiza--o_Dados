CREATE TABLE Pedido (
    id_pedido INT PRIMARY KEY,
    data DATE NOT NULL,
    Quantidade INT,
    id_produto INT,
    id_cliente INT,
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE Produto (
    id_produto INT PRIMARY KEY,
    nome VARCHAR(100),
    preco REAL
);

CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);
