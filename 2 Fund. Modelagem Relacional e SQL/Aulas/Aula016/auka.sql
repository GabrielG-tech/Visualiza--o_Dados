-- Criando uma tabela de contas bancárias
CREATE TABLE IF NOT EXISTS contas (
  num_conta INTEGER PRIMARY KEY,
  nome_cliente VARCHAR(100),
  saldo FLOAT
);

INSERT INTO contas (num_conta, nome_cliente, saldo) VALUES 
  (1, 'João', 1000.00),
  (2, 'Maria', 1500.00),
  (3, 'José', 200.75);

DELIMITER //

CREATE PROCEDURE obter_saldo (IN p_num_conta INTEGER)
BEGIN
  SELECT nome_cliente, saldo FROM contas WHERE num_conta = p_num_conta;
END //
DELIMITER; 

CALL obter_saldo(2);