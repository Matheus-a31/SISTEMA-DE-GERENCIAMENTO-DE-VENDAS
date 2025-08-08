from database.conexao import conexao as conectar

class Estoque:
    def __init__(self, id_estoque, id_produto, quantidade_disponivel):
        self.id_estoque = id_estoque
        self.id_produto = id_produto
        self.quantidade_disponivel = quantidade_disponivel

    
    def listar_estoque(self):
        conn = conectar()
        if not conn: return []
        estoque = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_estoque, id_produto, quantidade_disponivel FROM estoque ORDER BY id_produto")
                for row in cur.fetchall():
                    estoque.append(Estoque(*row))
        finally:
            conn.close()
        return estoque

    
    def inserir_estoque(self, estoque: "Estoque"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO estoque (id_produto, quantidade_disponivel) VALUES (%s, %s)",
                    (estoque.id_produto, estoque.quantidade_disponivel)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir estoque: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    
    def deletar_estoque(self, id_estoque):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM estoque WHERE id_estoque = %s", (id_estoque,))
                conn.commit()
        except Exception as e:
            print(f"Erro ao deletar estoque: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    
    def atualizar_estoque(self, estoque: "Estoque"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE estoque SET id_produto = %s, quantidade_disponivel = %s WHERE id_estoque = %s",
                    (estoque.id_produto, estoque.quantidade_disponivel, estoque.id_estoque)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar estoque: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    
    def buscar_estoque_por_id(self, id_estoque):
        conn = conectar()
        if not conn: return None
        estoque = None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_estoque, id_produto, quantidade_disponivel FROM estoque WHERE id_estoque = %s", (id_estoque,))
                row = cur.fetchone()
                if row:
                    estoque = Estoque(*row)
        except Exception as e:
            print(f"Erro ao buscar estoque por ID: {e}")
            return estoque
        finally:
            conn.close()
        return estoque

    
    def buscar_estoque_por_produto(self, id_produto):
        conn = conectar()
        if not conn: return None
        estoque = None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_estoque, id_produto, quantidade_disponivel FROM estoque WHERE id_produto = %s", (id_produto,))
                row = cur.fetchone()
                if row:
                    estoque = Estoque(*row)
        except Exception as e:
            print(f"Erro ao buscar estoque por produto: {e}")
            return estoque
        finally:
            conn.close()
        return estoque