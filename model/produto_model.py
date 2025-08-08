from database.conexao import conexao as conectar

class Produto:
    def __init__(self, id_produto, id_categoria, nome, descricao, preco):
        self.id_produto = id_produto
        self.id_categoria = id_categoria
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
    
    def listar_produtos(self):
        conn = conectar()
        if not conn: return []
        produtos = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_produto, id_categoria, nome, descricao, preco FROM produto ORDER BY nome")
                for row in cur.fetchall():
                    produtos.append(Produto(*row))
        finally:
            conn.close()
        return produtos

    def inserir_produto(self, produto: "Produto"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO produto (id_categoria, nome, descricao, preco) VALUES (%s, %s, %s, %s)",
                    (produto.id_categoria, produto.nome, produto.descricao, produto.preco)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def deletar_produto(self, id_produto):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM produto WHERE id_produto = %s", (id_produto,))
                conn.commit()
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def atualizar_produto(self, produto: "Produto"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE produto SET id_categoria = %s, nome = %s, descricao = %s, preco = %s WHERE id_produto = %s",
                    (produto.id_categoria, produto.nome, produto.descricao, produto.preco, produto.id_produto)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def buscar_produto_por_id(self, id_produto):
        conn = conectar()
        if not conn: return None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_produto, id_categoria, nome, descricao, preco FROM produto WHERE id_produto = %s", (id_produto,))
                row = cur.fetchone()
                if row:
                    return Produto(*row)
        except Exception as e:
            print(f"Erro ao buscar produto por ID: {e}")
        finally:
            conn.close()
        return None

    def buscar_produto_pelo_nome(self, nome):
        conn = conectar()
        if not conn: return []
        produtos = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_produto, id_categoria, nome, descricao, preco FROM produto WHERE nome ILIKE %s ORDER BY nome", (f'%{nome}%',))
                for row in cur.fetchall():
                    produtos.append(Produto(*row))
        except Exception as e:
            print(f"Erro ao buscar produto pelo nome: {e}")
        finally:
            conn.close()
        return produtos