from database.conexao import conexao as conectar

class Cliente:
    def __init__(self, id_cliente, nome, cpf, telefone, data_cadastro, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.data_cadastro = data_cadastro
        self.email = email

    def listar_cliente(self):
        conn = conectar()
        if not conn: return []
        clientes = []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id_cliente, nome, cpf, telefone, data_cadastro, email FROM cliente ORDER BY nome")
                for row in cur.fetchall():
                    clientes.append(Cliente(*row))
        finally:
            conn.close()
        return clientes

    def inserir_cliente(self, cliente: "Cliente"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO cliente (nome, cpf, telefone, data_cadastro, email) VALUES (%s, %s, %s, %s, %s)",
                    (cliente.nome, cliente.cpf, cliente.telefone, cliente.data_cadastro, cliente.email)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao inserir cliente: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
    
    def deletar_cliente(self, id_cliente):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
                conn.commit()
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True
        
    def atualizar_cliente(self, cliente: "Cliente"):
        conn = conectar()
        if not conn: return False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE cliente SET nome = %s, cpf = %s, telefone = %s, data_cadastro = %s, email = %s WHERE id_cliente = %s",
                    (cliente.nome, cliente.cpf, cliente.telefone, cliente.data_cadastro, cliente.email, cliente.id_cliente)
                )
                conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
        return True

    def busca_id_cliente(self, id_cliente):
            conn = conectar()
            if not conn: return None
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM cliente WHERE id_cliente = %s", (id_cliente,))
                    row = cur.fetchone()
                    if row:
                        return Cliente(*row)
                    return None
            except Exception as e:
                print(f"Erro ao buscar cliente por ID: {e}")
                return None
            finally:
                conn.close()
    
    def buscar_cpf_cliente(self, cpf):
            conn = conectar()
            if not conn: return None
            try:
                with conn.cursor() as cur:
                    # Usamos LIKE para permitir buscas parciais, mas poderia ser '=' para busca exata
                    cur.execute("SELECT * FROM cliente WHERE cpf LIKE %s", (f"%{cpf}%",))
                    clientes = []
                    for row in cur.fetchall():
                        clientes.append(Cliente(*row))
                    return clientes
            except Exception as e:
                print(f"Erro ao buscar cliente por CPF: {e}")
                return []
            finally:
                conn.close()
                