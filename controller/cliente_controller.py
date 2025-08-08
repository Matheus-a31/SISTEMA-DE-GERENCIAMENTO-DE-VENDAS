
from model.cliente_model import Cliente

class ClienteController:
    def __init__(self):
        self.model = Cliente(id_cliente=None, nome=None, cpf=None, telefone=None, data_cadastro=None, email=None)

    def listar(self):
        return self.model.listar_cliente()

    def inserir(self, nome, cpf, telefone, data_cadastro, email):
        novo_cliente = Cliente(id_cliente=None, nome=nome, cpf=cpf, telefone=telefone, data_cadastro=data_cadastro, email=email)
        return self.model.inserir_cliente(novo_cliente)

    def atualizar(self, id_cliente, nome, cpf, telefone, data_cadastro, email):
        cliente_atualizado = Cliente(id_cliente=id_cliente, nome=nome, cpf=cpf, telefone=telefone, data_cadastro=data_cadastro, email=email)
        return self.model.atualizar_cliente(cliente_atualizado)

    def deletar(self, id_cliente):
        return self.model.deletar_cliente(id_cliente)

    def buscar_por_id(self, id_cliente):
        return self.model.busca_id_cliente(id_cliente)
    
    def buscar_por_cpf(self, cpf):
        return self.model.buscar_cpf_cliente(cpf)