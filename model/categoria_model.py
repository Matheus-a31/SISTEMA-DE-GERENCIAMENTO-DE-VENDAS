from database.conexao import conexao as conectar

class Categoria:
    def __init__(self, id_categoria, nome, descricao):
        self.id_categoria = id_categoria
        self.nome = nome
        self.descricao = descricao

    def listar_categorias(self):
        conn = conectar()
        if not conn: return []
        categorias = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_categoria, nome, descricao FROM categoria ORDER BY nome")
                for row in cur.fetchall():
                    categorias.append(Categoria(*row))
        finally:
            conn.close()
        return categorias
    
    def inserir_categorias(self, categoria: "Categoria"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO categoria (nome, descricao) VALUES (%s, %s)",
                    (categoria.nome, categoria.descricao)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir categoria: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    def deletar_categoria(self, id_categoria):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM categoria WHERE id_categoria = %s", (id_categoria,))
                conn.commit()
        except Exception as e:
            print(f"Erro ao deletar categoria: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
        
    def atualizar_categoria(self, categoria: "Categoria"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE categoria SET nome = %s, descricao = %s WHERE id_categoria = %s",
                    (categoria.nome, categoria.descricao, categoria.id_categoria)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar categoria: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    def buscar_categoria_por_id(self, id_categoria):
        conn = conectar()
        if not conn: return None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_categoria, nome, descricao FROM categoria WHERE id_categoria = %s", (id_categoria,))
                row = cur.fetchone()
                if row:
                    return Categoria(*row)
        except Exception as e:
            print(f"Erro ao buscar categoria por ID: {e}")
        finally:
            conn.close()
        return None
    
    def buscar_categoria_por_nome(self, nome):
        conn = conectar()
        if not conn: return None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_categoria, nome, descricao FROM categoria WHERE nome = %s", (nome,))
                row = cur.fetchone()
                if row:
                    return Categoria(*row)
        except Exception as e:
            print(f"Erro ao buscar categoria por nome: {e}")
        finally:
            conn.close()
        return None
