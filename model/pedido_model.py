from database.conexao import conexao as conectar
from datetime import datetime

class Pedido:
    def __init__(self, id_pedido, id_cliente, data_pedido, valor_total, status):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.data_pedido = data_pedido
        self.valor_total = valor_total
        self.status = status
    
    def listar_pedido(self):
        conn = conectar()
        if not conn: return []
        pedidos = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_pedido, id_cliente, data_pedido, valor_total, status FROM pedido ORDER BY data_pedido DESC")
                for row in cur.fetchall():
                    pedidos.append(Pedido(*row))
        finally:
            conn.close()
        return pedidos

    @classmethod
    def inserir_pedido(self, pedido: "Pedido"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO pedido (id_cliente, data_pedido, valor_total, status) VALUES (%s, %s, %s, %s)",
                    (pedido.id_cliente, pedido.data_pedido, pedido.valor_total, pedido.status)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir pedido: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    @classmethod
    def deletar(self, id_pedido):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                # Primeiro deleta os itens do pedido
                cur.execute("DELETE FROM itemPedido WHERE id_pedido = %s", (id_pedido,))
                # Depois deleta o pedido
                cur.execute("DELETE FROM pedido WHERE id_pedido = %s", (id_pedido,))
                conn.commit()
                return True
        except Exception as e:
            print(f"Erro ao deletar pedido: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    @classmethod
    def atualizar_pedido(self, pedido: "Pedido"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE pedido SET id_cliente = %s, data_pedido = %s, valor_total = %s, status = %s WHERE id_pedido = %s",
                    (pedido.id_cliente, pedido.data_pedido, pedido.valor_total, pedido.status, pedido.id_pedido)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar pedido: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    @classmethod
    def buscar_pedido_por_id(self, id_pedido):
        conn = conectar()
        if not conn: return None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_pedido, id_cliente, data_pedido, valor_total, status FROM pedido WHERE id_pedido = %s", (id_pedido,))
                row = cur.fetchone()
                if row:
                    return Pedido(*row)
        except Exception as e:
            print(f"Erro ao buscar pedido por ID: {e}")
            return None
        finally:
            conn.close()
        return None

    @classmethod
    def buscar_pedido_pela_data(self, data_pedido):
        conn = conectar()
        if not conn: return []
        pedidos = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_pedido, id_cliente, data_pedido, valor_total, status FROM pedido WHERE data_pedido = %s", (data_pedido,))
                for row in cur.fetchall():
                    pedidos.append(Pedido(*row))
        except Exception as e:
            print(f"Erro ao buscar pedidos pela data: {e}")
        finally:
            conn.close()
        
        return pedidos
    
    def mostrar_log_exclusao(self, id_pedido=None):
        conn = conectar()
        if not conn: return []
        try:
            with conn.cursor() as cur:
                if id_pedido:
                    cur.execute("""
                        SELECT id_log, id_pedido_excluido, id_cliente, 
                            valor_total_pedido, data_exclusao 
                        FROM log_pedidos_excluidos 
                        WHERE id_pedido_excluido = %s
                        ORDER BY data_exclusao DESC
                        """, (id_pedido,))
                else:
                    cur.execute("""
                        SELECT id_log, id_pedido_excluido, id_cliente, 
                            valor_total_pedido, data_exclusao 
                        FROM log_pedidos_excluidos 
                        ORDER BY data_exclusao DESC
                        """)
                return cur.fetchall()
        except Exception as e:
            print(f"Erro ao buscar logs de exclusão: {e}")
            return []
        finally:
            conn.close()
            

           
        


    