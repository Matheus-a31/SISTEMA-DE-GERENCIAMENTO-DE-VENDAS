--1)
-- Atualiza o estoque após um item ser inserido no Pedido
CREATE OR REPLACE FUNCTION fn_atualiza_estoque_apos_insert() 
RETURNS TRIGGER AS $$
BEGIN
    UPDATE estoque
    SET quantidade_disponivel = quantidade_disponivel - NEW.quantidade
    WHERE id_produto = NEW.id_produto;
	RETURN NEW; 
END;
$$ LANGUAGE plpgsql;

-- Trigger
CREATE TRIGGER tg_atualiza_estoque_apos_insert
AFTER INSERT ON itemPedido
FOR EACH ROW
EXECUTE FUNCTION fn_atualiza_estoque_apos_insert();



--2)registrar exclusão de pedidos
CREATE OR REPLACE FUNCTION fn_log_exclusao_pedido() 
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO log_pedidos_excluidos (id_pedido_excluido, id_cliente, valor_total_pedido, data_exclusao)
    VALUES (OLD.id_pedido, OLD.id_cliente, OLD.valor_total, NOW());
    
    RETURN OLD; 
END;
$$ LANGUAGE plpgsql;

-- Trigger
CREATE TRIGGER tg_log_exclusao_pedido
AFTER DELETE ON pedido
FOR EACH ROW
EXECUTE FUNCTION fn_log_exclusao_pedido();

--3)Impedir a exclusão de um produto se ainda tiver estoque

CREATE OR REPLACE FUNCTION fn_impede_exclusao_produto_com_estoque() 
RETURNS TRIGGER AS $$
DECLARE
    quantidade_em_estoque INT;
BEGIN
    SELECT quantidade_disponivel INTO quantidade_em_estoque
    FROM estoque
    WHERE id_produto = OLD.id_produto;
    
    IF FOUND AND quantidade_em_estoque > 0 THEN
        RAISE EXCEPTION 'Não é possível excluir um produto que ainda possui estoque.';
    END IF;
    
    RETURN OLD; -- Permite a exclusão se a condição não for atendida.
END;
$$ LANGUAGE plpgsql;

--Trigger
CREATE TRIGGER tg_impede_exclusao_produto_com_estoque
BEFORE DELETE ON produto
FOR EACH ROW
EXECUTE FUNCTION fn_impede_exclusao_produto_com_estoque();


--4) Verificar disponibilidade no estoque antes de inserir

CREATE OR REPLACE FUNCTION fn_verifica_estoque_antes_de_inserir() 
RETURNS TRIGGER AS $$
DECLARE
    disponivel INT;
BEGIN
    SELECT quantidade_disponivel INTO disponivel
    FROM estoque
    WHERE id_produto = NEW.id_produto;
    
    IF NOT FOUND OR NEW.quantidade > disponivel THEN
        RAISE EXCEPTION 'Estoque insuficiente para a quantidade solicitada.';
    END IF;
    
    RETURN NEW; -- Permite a inserção se houver estoque
END;
$$ LANGUAGE plpgsql;

--Trigger
CREATE TRIGGER tg_verifica_estoque_antes_de_inserir
BEFORE INSERT ON itemPedido
FOR EACH ROW
EXECUTE FUNCTION fn_verifica_estoque_antes_de_inserir();


--5) atualiza valor total do pedido
CREATE OR REPLACE FUNCTION fn_atualiza_valor_total_pedido() 
RETURNS TRIGGER AS $$
DECLARE
    id_pedido_afetado INT;
BEGIN
    -- Determina qual id_pedido usar (da linha nova ou da antiga)
    IF (TG_OP = 'DELETE') THEN
        id_pedido_afetado := OLD.id_pedido;
    ELSE
        id_pedido_afetado := NEW.id_pedido;
    END IF;

    -- Atualiza o valor total no pedido correspondente
    UPDATE pedido
    SET valor_total = (
        SELECT COALESCE(SUM(quantidade * preco_unitario), 0)
        FROM itemPedido
        WHERE id_pedido = id_pedido_afetado
    )
    WHERE id_pedido = id_pedido_afetado;

    -- Retorna a tupla apropriada
    IF (TG_OP = 'DELETE') THEN
        RETURN OLD;
    ELSE
        RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;

--Triggers 
CREATE TRIGGER tg_valor_total_apos_insert
AFTER INSERT ON itemPedido
FOR EACH ROW
EXECUTE FUNCTION fn_atualiza_valor_total_pedido();

CREATE TRIGGER tg_valor_total_apos_update
AFTER UPDATE ON itemPedido
FOR EACH ROW
EXECUTE FUNCTION fn_atualiza_valor_total_pedido();

CREATE TRIGGER tg_valor_total_apos_delete
AFTER DELETE ON itemPedido
FOR EACH ROW
EXECUTE FUNCTION fn_atualiza_valor_total_pedido();