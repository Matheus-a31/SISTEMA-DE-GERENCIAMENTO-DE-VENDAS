from database.conexao import conexao as conectar

class ItemPedido:
    def __init__(self, id_itemPedido, id_pedido, id_produto, quantidade, preco_unitario):
        self.id_itemPedido = id_itemPedido
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def listar_itemPedido(self):
        conn = conectar()
        if not conn: return []
        itens = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_itemPedido, id_pedido, id_produto, quantidade, preco_unitario FROM itemPedido ORDER BY id_itemPedido")
                for row in cur.fetchall():
                    itens.append(ItemPedido(*row))
        finally:
            conn.close()
        return itens

    def inserir_itemPedido(self, item: "ItemPedido"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO itemPedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)",
                    (item.id_pedido, item.id_produto, item.quantidade, item.preco_unitario)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir item de pedido: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def deletar_itemPedido(self, id_itemPedido):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM itemPedido WHERE id_itemPedido = %s", (id_itemPedido,))
                conn.commit()
        except Exception as e:
            print(f"Erro ao deletar item de pedido: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def atualizar_itemPedido(self, item: "ItemPedido"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE itemPedido SET id_pedido = %s, id_produto = %s, quantidade = %s, preco_unitario = %s WHERE id_itemPedido = %s",
                    (item.id_pedido, item.id_produto, item.quantidade, item.preco_unitario, item.id_itemPedido)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar item de pedido: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    def buscar_itemPedido_por_id(self, id_itemPedido):
        conn = conectar()
        if not conn: return None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_itemPedido, id_pedido, id_produto, quantidade, preco_unitario FROM itemPedido WHERE id_itemPedido = %s", (id_itemPedido,))
                row = cur.fetchone()
                if row:
                    return ItemPedido(*row)
        except Exception as e:
            print(f"Erro ao buscar item de pedido por ID: {e}")
        finally:
            conn.close()
        return None

    def buscar_itens_por_pedido(self, id_pedido):
        conn = conectar()
        if not conn: return []
        itens = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_itemPedido, id_pedido, id_produto, quantidade, preco_unitario FROM itemPedido WHERE id_pedido = %s", (id_pedido,))
                for row in cur.fetchall():
                    itens.append(ItemPedido(*row))
        except Exception as e:
            print(f"Erro ao buscar itens por pedido: {e}")
        finally:
            conn.close()
        return itens