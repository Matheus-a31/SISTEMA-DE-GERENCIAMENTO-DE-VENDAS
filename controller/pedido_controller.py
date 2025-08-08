from model.pedido_model import Pedido

class PedidoController:
    def __init__(self):
        self.model = Pedido(id_pedido=None, id_cliente=None, data_pedido=None, valor_total=None, status=None)

    def listar(self):
        return self.model.listar_pedido()

    def inserir(self, id_cliente, data_pedido, valor_total, status):
        novo_pedido = Pedido(id_pedido=None, id_cliente=id_cliente, data_pedido=data_pedido, valor_total=valor_total, status=status)
        return self.model.inserir_pedido(novo_pedido)

    def atualizar(self, id_pedido, id_cliente, data_pedido, valor_total, status):
        pedido_atualizado = Pedido(id_pedido=id_pedido, id_cliente=id_cliente, data_pedido=data_pedido, valor_total=valor_total, status=status)
        return self.model.atualizar_pedido(pedido_atualizado)

    def deletar(self, id_pedido):
        return self.model.deletar(id_pedido)

    def buscar_por_id(self, id_pedido):
        return self.model.buscar_pedido_por_id(id_pedido)
    
    def buscar_pela_data(self, data_pedido):
        return self.model.buscar_pedido_pela_data(data_pedido)
    
    def mostrar_log_exclusao(self, id_pedido=None):
        return self.model.mostrar_log_exclusao(id_pedido)