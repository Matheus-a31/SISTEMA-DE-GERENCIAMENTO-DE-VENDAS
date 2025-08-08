from model.comandos_avancados_model import ComansdosAvancadosModel

class ComandosAvancadosController:
    def __init__(self):
        # Instancia o modelo que contém as consultas
        self.model = ComansdosAvancadosModel()

    def listar_produtos_com_categoria(self):
        return self.model.listar_produtos_com_categoria() #

    def listar_pedidos_com_cliente(self):
        return self.model.listar_pedidos_com_cliente() 
            
    def calcular_total_gasto_por_cliente(self):
        return self.model.calcular_total_gasto_por_cliente() 
    
    def encontrar_produtos_nunca_vendidos(self):
        return self.model.encontrar_produtos_nunca_vendidos() 
    
    def clientes_com_gastos_acima_de(self, valor_minimo):
        return self.model.clientes_com_gastos_acima_de(valor_minimo) 