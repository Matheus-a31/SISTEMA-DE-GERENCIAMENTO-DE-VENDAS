from model.estoque_model import Estoque

class EstoqueController:
    def __init__(self):
        # A instância base pode ser usada para chamar os métodos que não dependem de um objeto específico
        self.model = Estoque(id_estoque=None, id_produto=None, quantidade_disponivel=None)

    def listar(self):
        return self.model.listar_estoque()

    def inserir(self, id_produto, quantidade_disponivel):
        novo_item = Estoque(id_estoque=None, id_produto=id_produto, quantidade_disponivel=quantidade_disponivel)
        return self.model.inserir_estoque(novo_item)

    def atualizar(self, id_estoque, id_produto, quantidade_disponivel):
        item_atualizado = Estoque(id_estoque=id_estoque, id_produto=id_produto, quantidade_disponivel=quantidade_disponivel)
        return self.model.atualizar_estoque(item_atualizado)

    def deletar(self, id_estoque):
        return self.model.deletar_estoque(id_estoque)

    def buscar_por_id(self, id_estoque):
        return self.model.buscar_estoque_por_id(id_estoque)
    
    def buscar_por_produto(self, id_produto):
        return self.model.buscar_estoque_por_produto(id_produto)