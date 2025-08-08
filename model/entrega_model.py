from datetime import datetime
from database.conexao import conexao as conectar

class Entrega:
    def __init__(self, id_entrega, id_pedido, transportadora, codigo_rastreio, custo_frete,
                 data_envio, data_entrega_estimada, data_entrega_real, status):
        self.id_entrega = id_entrega
        self.id_pedido = id_pedido
        self.transportadora = transportadora
        self.codigo_rastreio = codigo_rastreio
        self.custo_frete = custo_frete
        self.data_envio = data_envio
        self.data_entrega_estimada = data_entrega_estimada
        self.data_entrega_real = data_entrega_real
        self.status = status

    def listar_entregas(self):
        conn = conectar()
        if not conn: return []
        entregas = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_entrega, id_pedido, transportadora, codigo_rastreio, custo_frete, "
                            "data_envio, data_entrega_estimada, data_entrega_real, status FROM entrega ORDER BY id_entrega")
                for row in cur.fetchall():
                    entregas.append(Entrega(*row))
        finally:
            conn.close()
        return entregas

    def inserir_entrega(self, entrega: "Entrega"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO entrega (id_pedido, transportadora, codigo_rastreio, custo_frete, "
                    "data_envio, data_entrega_estimada, data_entrega_real, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (entrega.id_pedido, entrega.transportadora, entrega.codigo_rastreio,
                    entrega.custo_frete, entrega.data_envio, entrega.data_entrega_estimada,
                    entrega.data_entrega_real, entrega.status)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir entrega: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    def deletar_entrega(self, id_entrega):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM entrega WHERE id_entrega = %s", (id_entrega,))
                conn.commit()
        except Exception as e:
            print(f"Erro ao deletar entrega: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    def atualizar_entrega(self, entrega: "Entrega"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE entrega SET id_pedido = %s, transportadora = %s, codigo_rastreio = %s, "
                    "custo_frete = %s, data_envio = %s, data_entrega_estimada = %s, "
                    "data_entrega_real = %s, status = %s WHERE id_entrega = %s",
                    (entrega.id_pedido, entrega.transportadora, entrega.codigo_rastreio,
                    entrega.custo_frete, entrega.data_envio, entrega.data_entrega_estimada,
                    entrega.data_entrega_real, entrega.status, entrega.id_entrega)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar entrega: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    def buscar_entrega_por_id(self, id_entrega):
        conn = conectar()
        if not conn: return None
        entrega = None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_entrega, id_pedido, transportadora, codigo_rastreio, custo_frete, "
                            "data_envio, data_entrega_estimada, data_entrega_real, status FROM entrega WHERE id_entrega = %s",
                            (id_entrega,))
                row = cur.fetchone()
                if row:
                    entrega = Entrega(*row)
        finally:
            conn.close()
        return entrega

    def buscar_entrega_por_status(self, status):
        conn = conectar()
        if not conn: return []
        entregas = []
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id_entrega, id_pedido, transportadora, codigo_rastreio, custo_frete,
                        data_envio, data_entrega_estimada, data_entrega_real, status
                    FROM entrega 
                    WHERE status = %s
                    ORDER BY data_envio DESC
                    """, (status,))
                for row in cur.fetchall():
                    entregas.append(Entrega(*row))
        except Exception as e:
            print(f"Erro ao buscar entregas por status: {e}")
            return []
        finally:
            conn.close()
        return entregas