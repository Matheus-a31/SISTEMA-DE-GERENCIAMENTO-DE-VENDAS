from controller.pagamento_controller import PagamentoController
from controller.pedido_controller import PedidoController
from datetime import datetime

class PagamentoView:
    def __init__(self):
        self.controller = PagamentoController()
        self.pedido_controller = PedidoController()

    def menu(self):
        while True:
            print("\n--- Menu Pagamentos ---")
            print("1. Listar Pagamentos")
            print("2. Registrar Pagamento")
            print("3. Atualizar Pagamento")
            print("4. Cancelar Pagamento")
            print("5. Buscar por ID")
            print("6. Buscar por Método")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar()
            elif opcao == "2":
                self.registrar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.cancelar()
            elif opcao == "5":
                self.buscar_por_id()
            elif opcao == "6":
                self.buscar_por_metodo()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar(self):
        pagamentos = self.controller.listar()
        print("\nLista de Pagamentos:")
        for pag in pagamentos:
            print(f"ID: {pag.id_pagamento} | Pedido ID: {pag.id_pedido}")
            print(f"Método: {pag.metodo_pagamento} | Status: {pag.status_pagamento}")
            print(f"Data: {pag.data_pagamento}")

    def registrar(self):
        print("\nRegistrar Pagamento:")
        # Listar pedidos disponíveis
        pedidos = self.pedido_controller.listar()
        print("\nPedidos disponíveis:")
        for ped in pedidos:
            print(f"ID: {ped.id_pedido} | Valor: R${ped.valor_total:.2f} | Status: {ped.status}")
        
        id_pedido = int(input("ID do Pedido: "))
        metodo_pagamento = input("Método de Pagamento (Cartão/Dinheiro/Pix): ")
        status_pagamento = "Aprovado"  # Pode ser ajustado conforme necessidade
        data_pagamento = datetime.now().strftime("%Y-%m-%d")
        
        if self.controller.inserir(id_pedido, metodo_pagamento, status_pagamento, data_pagamento):
            print("Pagamento registrado com sucesso!")
        else:
            print("Erro ao registrar pagamento.")

    def atualizar(self):
        self.listar()
        id_pagamento = int(input("ID do pagamento a atualizar: "))
        
        # Buscar pagamento existente
        pagamento = self.controller.buscar_por_id(id_pagamento)
        if not pagamento:
            print("Pagamento não encontrado!")
            return
            
        print("\nDeixe em branco para manter o valor atual")
        # Listar pedidos disponíveis
        pedidos = self.pedido_controller.listar()
        print("\nPedidos disponíveis:")
        for ped in pedidos:
            print(f"ID: {ped.id_pedido} | Valor: R${ped.valor_total:.2f}")
        
        id_pedido = input(f"ID Pedido [{pagamento.id_pedido}]: ") or pagamento.id_pedido
        metodo_pagamento = input(f"Método [{pagamento.metodo_pagamento}]: ") or pagamento.metodo_pagamento
        status_pagamento = input(f"Status [{pagamento.status_pagamento}]: ") or pagamento.status_pagamento
        data_pagamento = input(f"Data [{pagamento.data_pagamento}]: ") or pagamento.data_pagamento
        
        if self.controller.atualizar(id_pagamento, id_pedido, metodo_pagamento, status_pagamento, data_pagamento):
            print("Pagamento atualizado com sucesso!")
        else:
            print("Erro ao atualizar pagamento.")

    def cancelar(self):
        self.listar()
        id_pagamento = int(input("ID do pagamento a cancelar: "))
        if self.controller.deletar(id_pagamento):
            print("Pagamento cancelado com sucesso!")
        else:
            print("Erro ao cancelar pagamento.")

    def buscar_por_id(self):
        id_pagamento = int(input("ID do pagamento: "))
        pagamento = self.controller.buscar_por_id(id_pagamento)
        if pagamento:
            print(f"\nDetalhes do Pagamento:")
            print(f"ID: {pagamento.id_pagamento} | Pedido ID: {pagamento.id_pedido}")
            print(f"Método: {pagamento.metodo_pagamento} | Status: {pagamento.status_pagamento}")
            print(f"Data: {pagamento.data_pagamento}")
        else:
            print("Pagamento não encontrado!")

    def buscar_por_metodo(self):
        metodo = input("Método de Pagamento: ")
        pagamentos = self.controller.buscar_por_metodo(metodo)
        if pagamentos:
            print("\nPagamentos encontrados:")
            for pag in pagamentos:
                print(f"ID: {pag.id_pagamento} | Pedido ID: {pag.id_pedido}")
                print(f"Método: {pag.metodo_pagamento} | Status: {pag.status_pagamento}")
                print(f"Data: {pag.data_pagamento}")
        else:
            print("Nenhum pagamento encontrado com este método!")