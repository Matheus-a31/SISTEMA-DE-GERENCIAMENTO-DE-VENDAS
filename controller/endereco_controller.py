from model.endereco_model import Endereco

class EnderecoController:
    def __init__(self):
        self.model = Endereco(id_endereco=None, id_cliente=None, logradouro=None, numero=None, cidade=None, estado=None, cep=None)

    def listar(self):
        return self.model.listar_endereco()

    def inserir(self, id_cliente, logradouro, numero, cidade, estado, cep):
        novo_endereco = Endereco(id_endereco=None, id_cliente=id_cliente, logradouro=logradouro, numero=numero, cidade=cidade, estado=estado, cep=cep)
        return self.model.inserir_endereco(novo_endereco)

    def atualizar(self, id_endereco, id_cliente, logradouro, numero, cidade, estado, cep):
        endereco_atualizado = Endereco(id_endereco=id_endereco, id_cliente=id_cliente, logradouro=logradouro, numero=numero, cidade=cidade, estado=estado, cep=cep)
        return self.model.atualizar_endereco(endereco_atualizado)

    def deletar(self, id_endereco):
        return self.model.deletar_endereco(id_endereco)

    def buscar_por_id(self, id_endereco):
        return self.model.buscar_endereco_por_id(id_endereco)
    
    def buscar_por_cidade(self, cidade):
        return self.model.buscar_endereco_por_cidade(cidade)