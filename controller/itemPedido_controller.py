from model.itemPedido_model import ItemPedido

class ItemPedidoController:
    def __init__(self):
        self.model = ItemPedido(id_itemPedido=None, id_pedido=None, id_produto=None, quantidade=None, preco_unitario=None)

    def listar(self):
        return self.model.listar_itemPedido()

    def inserir(self, id_pedido, id_produto, quantidade, preco_unitario):
        novo_item = ItemPedido(id_itemPedido=None, id_pedido=id_pedido, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario)
        return self.model.inserir_itemPedido(novo_item)

    def atualizar(self, id_item, id_pedido, id_produto, quantidade, preco_unitario):
        item_atualizado = ItemPedido(id_itemPedido=id_item, id_pedido=id_pedido, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario)
        return self.model.atualizar_itemPedido(item_atualizado)

    def deletar(self, id_item):
        return self.model.deletar_itemPedido(id_item)

    def buscar_por_id(self, id_item):
        return self.model.buscar_itemPedido_por_id(id_item)
    
    def buscar_por_pedido(self, id_pedido):
        return self.model.buscar_itens_por_pedido(id_pedido)
    