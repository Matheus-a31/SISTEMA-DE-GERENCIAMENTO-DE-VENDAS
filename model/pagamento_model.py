from database.conexao import conexao as conectar
from datetime import datetime

class Pagamento:
    def __init__(self, id_pagamento, id_pedido, metodo_pagamento, status_pagamento, data_pagamento):
        self.id_pagamento = id_pagamento
        self.id_pedido = id_pedido
        self.metodo_pagamento = metodo_pagamento
        self.status_pagamento = status_pagamento
        self.data_pagamento = data_pagamento

    def listar_pagamentos(self):
        conn = conectar()
        if not conn: return []
        pagamentos = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_pagamento, id_pedido, metodo_pagamento, status_pagamento, data_pagamento FROM pagamento ORDER BY data_pagamento")
                for row in cur.fetchall():
                    pagamentos.append(Pagamento(*row))
        finally:
            conn.close()
        return pagamentos

    def inserir_pagamento(self, pagamento: "Pagamento"):  
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO pagamento (id_pedido, metodo_pagamento, status_pagamento, data_pagamento) VALUES (%s, %s, %s, %s)",
                    (pagamento.id_pedido, pagamento.metodo_pagamento, pagamento.status_pagamento, pagamento.data_pagamento)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir pagamento: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def deletar_pagamento(self, id_pagamento): 
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM pagamento WHERE id_pagamento = %s", (id_pagamento,))
                conn.commit()
        except Exception as e:
            print(f"Erro ao deletar pagamento: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def atualizar_pagamento(self, pagamento: "Pagamento"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE pagamento SET id_pedido = %s, metodo_pagamento = %s, status_pagamento = %s, data_pagamento = %s WHERE id_pagamento = %s",
                    (pagamento.id_pedido, pagamento.metodo_pagamento, pagamento.status_pagamento, pagamento.data_pagamento, pagamento.id_pagamento)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar pagamento: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def buscar_pagamento_por_id(self, id_pagamento):
        conn = conectar()
        if not conn: return None
        pagamento = None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_pagamento, id_pedido, metodo_pagamento, status_pagamento, data_pagamento FROM pagamento WHERE id_pagamento = %s", (id_pagamento,))
                row = cur.fetchone()
                if row:
                    pagamento = Pagamento(*row)
        except Exception as e:
            print(f"Erro ao buscar pagamento por ID: {e}")
            return pagamento
        finally:
            conn.close()
        return pagamento
    
    def buscar_pagamento_por_metodo(self, metodo_pagamento):
        conn = conectar()
        if not conn: return []
        pagamentos = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_pagamento, id_pedido, metodo_pagamento, status_pagamento, data_pagamento FROM pagamento WHERE metodo_pagamento = %s", (metodo_pagamento,))
                for row in cur.fetchall():
                    pagamentos.append(Pagamento(*row))
        except Exception as e:
            print(f"Erro ao buscar pagamentos por método: {e}")
        finally:
            conn.close()
        return pagamentos