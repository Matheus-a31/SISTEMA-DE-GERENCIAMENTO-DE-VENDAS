from database.conexao import conexao as conectar

class Endereco:
    def __init__(self, id_endereco, id_cliente, logradouro, numero, cep, cidade, estado):
        self.id_endereco = id_endereco
        self.id_cliente = id_cliente
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
    
    def listar_endereco(self):
        conn = conectar()
        if not conn: return []
        enderecos = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_endereco, id_cliente, logradouro, numero, cep, cidade, estado FROM endereco ORDER BY id_cliente")
                for row in cur.fetchall():
                    enderecos.append(Endereco(*row))
        finally:
            conn.close()
        return enderecos

    def inserir_endereco(self, endereco: "Endereco"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO endereco (id_cliente, logradouro, numero, cep, cidade, estado) VALUES (%s, %s, %s, %s, %s, %s)",
                    (endereco.id_cliente, endereco.logradouro, endereco.numero, endereco.cep, endereco.cidade, endereco.estado)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir endereço: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    def deletar_endereco(self, id_endereco):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM endereco WHERE id_endereco = %s", (id_endereco,))
                conn.commit()
        except Exception as e:
            print(f"Erro ao deletar endereço: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def atualizar_endereco(self, endereco: "Endereco"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE endereco SET id_cliente = %s, logradouro = %s, numero = %s, cep = %s, cidade = %s, estado = %s WHERE id_endereco = %s",
                    (endereco.id_cliente, endereco.logradouro, endereco.numero, endereco.cep, endereco.cidade, endereco.estado, endereco.id_endereco)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar endereço: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def buscar_endereco_por_id(self, id_endereco):
        conn = conectar()
        if not conn: return None
        endereco = None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_endereco, id_cliente, logradouro, numero, cep, cidade, estado FROM endereco WHERE id_endereco = %s", (id_endereco,))
                row = cur.fetchone()
                if row:
                    endereco = Endereco(*row)
        except Exception as e:
            print(f"Erro ao buscar endereço por ID: {e}")
            return None
        finally:
            conn.close()
        return endereco

    def buscar_endereco_por_cidade(self, cidade):
        conn = conectar()
        if not conn: return []
        enderecos = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_endereco, id_cliente, logradouro, numero, cep, cidade, estado FROM endereco WHERE cidade = %s", (cidade,))
                for row in cur.fetchall():
                    enderecos.append(Endereco(*row))
        except Exception as e:
            print(f"Erro ao buscar endereços por cidade: {e}")
            return []
        finally:
            conn.close()
        return enderecos
        