--Ciação do Banco de dados 
CREATE DATABASE sistema_de_vendas;

-- Criação da tabela de Clientes
CREATE TABLE cliente (
    id_cliente INT SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    CPF VARCHAR(14) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    data_cadastro DATE NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Criação da tabela de Categorias
CREATE TABLE categoria (
    id_categoria INT SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    descricao TEXT
);

-- Criação da tabela de Produtos 
CREATE TABLE produto (
    id_produto INT SERIAL PRIMARY KEY,
    id_categoria INT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

-- Criação da tabela de Estoque
CREATE TABLE estoque (
    id_estoque INT SERIAL PRIMARY KEY,
    id_produto INT NOT NULL,
    quantidade_disponivel INT NOT NULL DEFAULT 0,
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

-- Criação da tabela de Endereços
CREATE TABLE endereco (
    id_endereco INT SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    logradouro VARCHAR(255) NOT NULL,
    numero VARCHAR(20) NOT NULL,
    CEP VARCHAR(9) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- Criação da tabela de Pedidos
CREATE TABLE pedido (
    id_pedido INT SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_pedido DATETIME NOT NULL,
    valor_total DECIMAL(10, 2) DEFAULT 0.00,
    status VARCHAR(50) DEFAULT 'Pendente',
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- Criação da tabela de Itens do Pedido
CREATE TABLE itemPedido (
    id_itemPedido INT SERIAL PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

-- Criação da tabela de Pagamentos
CREATE TABLE pagamento (
    id_pagamento INT SERIAL PRIMARY KEY,
    id_pedido INT NOT NULL,
    metodo_pagamento VARCHAR(50) NOT NULL,
    status_pagamento VARCHAR(50) NOT NULL,
    data_pagamento DATETIME,
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido)
);

-- Criação da tabela de Entregas
CREATE TABLE entrega (
    id_entrega INT SERIAL PRIMARY KEY,
    id_pedido INT NOT NULL,
    transportadora VARCHAR(100),
    codigo_rastreio VARCHAR(100),
    custo_frete DECIMAL(10, 2),
    data_envio DATETIME,
    data_entrega_estimada DATE,
    data_entrega_real DATE,
    status VARCHAR(50),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido)
);


-- Tabela para Log de exclusão de pedidos, utilizada pelo Trigger
CREATE TABLE log_pedidos_excluidos (
    id_log SERIAL PRIMARY KEY,
    id_pedido_excluido INT,
    id_cliente INT,
    valor_total_pedido DECIMAL(10, 2),
    data_exclusao TIMESTAMP NOT NULL
);