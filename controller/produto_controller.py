from model.produto_model import Produto

class ProdutoController:
    def __init__(self):
        self.model = Produto(id_produto=None, id_categoria=None, nome=None, descricao=None, preco=None)

    def listar(self):
        return self.model.listar_produtos()

    def inserir(self, id_categoria, nome, descricao, preco):
        novo_produto = Produto(id_produto=None, id_categoria=id_categoria, nome=nome, descricao=descricao, preco=preco)
        return self.model.inserir_produto(novo_produto)

    def atualizar(self, id_produto, id_categoria, nome, descricao, preco):
        produto_atualizado = Produto(id_produto=id_produto, id_categoria=id_categoria, nome=nome, descricao=descricao, preco=preco)
        return self.model.atualizar_produto(produto_atualizado)

    def deletar(self, id_produto):
        return self.model.deletar_produto(id_produto)

    def buscar_por_id(self, id_produto):
        return self.model.buscar_produto_por_id(id_produto)

    def buscar_pelo_nome(self, nome):
        return self.model.buscar_produto_pelo_nome(nome)