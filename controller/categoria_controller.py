from model.categoria_model import Categoria

class CategoriaController:
    def __init__(self):
        self.model = Categoria(id_categoria=None, nome=None, descricao=None)

    def listar(self):
        return self.model.listar_categorias()

    def inserir(self, nome, descricao):
        nova_categoria = Categoria(id_categoria=None, nome=nome, descricao=descricao)
        return self.model.inserir_categorias(nova_categoria)

    def atualizar(self, id_categoria, nome, descricao):
        categoria_atualizada = Categoria(id_categoria=id_categoria, nome=nome, descricao=descricao)
        return self.model.atualizar_categoria(categoria_atualizada)

    def deletar(self, id_categoria):
        return self.model.deletar_categoria(id_categoria)

    def buscar_por_id(self, id_categoria):
        return self.model.buscar_categoria_por_id(id_categoria)
    
    def buscar_por_nome(self, nome):
        return self.model.buscar_categoria_por_nome(nome)