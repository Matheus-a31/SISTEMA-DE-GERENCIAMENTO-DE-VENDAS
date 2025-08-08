from model.entrega_model import Entrega

class EntregaController:
    def __init__(self):
        self.model = Entrega(id_entrega=None, id_pedido=None, transportadora=None, 
                           codigo_rastreio=None, custo_frete=None, data_envio=None,
                           data_entrega_estimada=None, data_entrega_real=None, status=None)
    def listar(self):
        return self.model.listar_entregas()

    def inserir(self, id_pedido, transportadora, codigo_rastreio, custo_frete, data_envio, data_entrega_estimada, data_entrega_real, status):
        # Cria uma nova instância de Entrega com os dados fornecidos
        nova_entrega = Entrega(id_entrega=None, id_pedido=id_pedido, transportadora=transportadora, 
                               codigo_rastreio=codigo_rastreio, custo_frete=custo_frete, data_envio=data_envio, 
                               data_entrega_estimada=data_entrega_estimada, 
                               data_entrega_real=data_entrega_real, status=status)
        return self.model.inserir_entrega(nova_entrega)

    def atualizar(self, id_entrega, id_pedido, transportadora, codigo_rastreio, 
              custo_frete, data_envio, data_entrega_estimada, data_entrega_real, status):
        entrega_atualizada = Entrega(
            id_entrega=id_entrega,
            id_pedido=id_pedido,
            transportadora=transportadora,
            codigo_rastreio=codigo_rastreio,
            custo_frete=custo_frete,
            data_envio=data_envio,
            data_entrega_estimada=data_entrega_estimada,
            data_entrega_real=data_entrega_real,
            status=status
        )
        return self.model.atualizar_entrega(entrega_atualizada)

    def deletar(self, id_entrega):
        return self.model.deletar_entrega(id_entrega)

    def buscar_por_id(self, id_entrega):
        return self.model.buscar_entrega_por_id(id_entrega)
    
    def buscar_por_status(self, status):
        return self.model.buscar_entrega_por_status(status)
    