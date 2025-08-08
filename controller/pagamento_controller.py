
from model.pagamento_model import Pagamento

class PagamentoController:
    def __init__(self):
        self.model = Pagamento(id_pagamento=None, id_pedido=None, metodo_pagamento=None, status_pagamento=None, data_pagamento=None)
        
    def listar(self):
        return self.model.listar_pagamentos()

    def inserir(self, id_pedido, metodo_pagamento, status_pagamento, data_pagamento):
        novo_pagamento = Pagamento(
            id_pagamento=None, 
            id_pedido=id_pedido, 
            metodo_pagamento=metodo_pagamento, 
            status_pagamento=status_pagamento, 
            data_pagamento=data_pagamento
        )
        return self.model.inserir_pagamento(novo_pagamento)
    
    def atualizar(self, id_pagamento, id_pedido, metodo_pagamento, status_pagamento, data_pagamento):
        pagamento_atualizado = Pagamento(
            id_pagamento=id_pagamento, 
            id_pedido=id_pedido, 
            metodo_pagamento=metodo_pagamento, 
            status_pagamento=status_pagamento, 
            data_pagamento=data_pagamento
        )
        return self.model.atualizar_pagamento(pagamento_atualizado)
    
    def deletar(self, id_pagamento):
        return self.model.deletar_pagamento(id_pagamento)
    
    def buscar_por_id(self, id_pagamento):
        return self.model.buscar_pagamento_por_id(id_pagamento)
    
    def buscar_por_metodo(self, metodo_pagamento):
        return self.model.buscar_pagamento_por_metodo(metodo_pagamento)