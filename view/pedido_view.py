from controller.pedido_controller import PedidoController
from controller.cliente_controller import ClienteController
from controller.itemPedido_controller import ItemPedidoController
from controller.produto_controller import ProdutoController
from datetime import datetime

class PedidoView:
    def __init__(self):
        self.controller = PedidoController()
        self.cliente_controller = ClienteController()
        self.item_controller = ItemPedidoController()
        self.produto_controller = ProdutoController()

    def menu(self):
        while True:
            print("\n--- Menu Pedidos ---")
            print("1. Listar Pedidos")
            print("2. inserir Pedido")
            print("3. Atualizar Pedido")
            print("4. deletar Pedido")
            print("5. Buscar por ID")
            print("6. Buscar por Data")
            print("7. Mostrar Log de Exclusão")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar()
            elif opcao == "2":
                self.inserir()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.deletar()
            elif opcao == "5":
                self.buscar_por_id()
            elif opcao == "6":
                self.buscar_por_data()
            elif opcao == "7":
                self.mostrar_log_exclusao()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar(self):
        pedidos = self.controller.listar()
        print("\nLista de Pedidos:")
        for ped in pedidos:
            cliente = self.cliente_controller.buscar_por_id(ped.id_cliente)
            cliente_nome = cliente.nome if cliente else "Desconhecido"
            print(f"ID: {ped.id_pedido} | Data: {ped.data_pedido} | Cliente: {cliente_nome}")
            print(f"Valor Total: R${ped.valor_total:.2f} | Status: {ped.status}")
            
            # Listar itens do pedido
            itens = self.item_controller.buscar_por_pedido(ped.id_pedido)
            if itens:
                print("Itens do Pedido:")
                for item in itens:
                    produto = self.produto_controller.buscar_por_id(item.id_produto)
                    prod_nome = produto.nome if produto else "Desconhecido"
                    print(f"  - {prod_nome} | Quantidade: {item.quantidade} | Preço Unitário: R${item.preco_unitario:.2f}")

    def inserir(self):
        print("\nNovo Pedido:")
        # Listar clientes disponíveis
        clientes = self.cliente_controller.listar()
        print("\nClientes disponíveis:")
        for cli in clientes:
            print(f"ID: {cli.id_cliente} | Nome: {cli.nome}")
        
        id_cliente = int(input("ID do Cliente: "))
        data_pedido = datetime.now().strftime("%Y-%m-%d")
        valor_total = 0.0  # Será calculado com os itens
        status = "Pendente"
        
        # inserir o pedido
        if self.controller.inserir(id_cliente, data_pedido, valor_total, status):
            print("Pedido criado com sucesso!")
            # Buscar o ID do pedido recém-criado
            pedidos = self.controller.listar()
            novo_pedido = pedidos[0]  # Assumindo que o mais recente é o primeiro
            print(f"Pedido ID: {novo_pedido.id_pedido}")
        else:
            print("Erro ao inserir pedido.")

    def atualizar(self):
        self.listar()
        id_pedido = int(input("ID do pedido a atualizar: "))
        
        # Buscar pedido existente
        pedido = self.controller.buscar_por_id(id_pedido)
        if not pedido:
            print("Pedido não encontrado!")
            return
            
        print("\nDeixe em branco para manter o valor atual")
        # Listar clientes disponíveis
        clientes = self.cliente_controller.listar()
        print("\nClientes disponíveis:")
        for cli in clientes:
            print(f"ID: {cli.id_cliente} | Nome: {cli.nome}")
        
        id_cliente = input(f"ID Cliente [{pedido.id_cliente}]: ") or pedido.id_cliente
        data_pedido = input(f"Data [{pedido.data_pedido}]: ") or pedido.data_pedido
        status = input(f"Status [{pedido.status}]: ") or pedido.status
        
        # O valor total é calculado automaticamente com base nos itens
        if self.controller.atualizar(id_pedido, id_cliente, data_pedido, pedido.valor_total, status):
            print("Pedido atualizado com sucesso!")
        else:
            print("Erro ao atualizar pedido.")

    def deletar(self):
        self.listar()
        id_pedido = int(input("ID do pedido a deletar: "))
        if self.controller.deletar(id_pedido):
            print("Pedido cancelado com sucesso!")
        else:
            print("Erro ao deletar pedido.")

    def buscar_por_id(self):
        id_pedido = int(input("ID do pedido: "))
        pedido = self.controller.buscar_por_id(id_pedido)
        if pedido:
            cliente = self.cliente_controller.buscar_por_id(pedido.id_cliente)
            cliente_nome = cliente.nome if cliente else "Desconhecido"
            print(f"\nDetalhes do Pedido:")
            print(f"ID: {pedido.id_pedido} | Data: {pedido.data_pedido} | Cliente: {cliente_nome}")
            print(f"Valor Total: R${pedido.valor_total:.2f} | Status: {pedido.status}")
            
            # Listar itens do pedido
            itens = self.item_controller.buscar_por_pedido(pedido.id_pedido)
            if itens:
                print("Itens do Pedido:")
                for item in itens:
                    produto = self.produto_controller.buscar_por_id(item.id_produto)
                    prod_nome = produto.nome if produto else "Desconhecido"
                    print(f"  - {prod_nome} | Quantidade: {item.quantidade} | Preço Unitário: R${item.preco_unitario:.2f}")
        else:
            print("Pedido não encontrado!")

    def buscar_por_data(self):
        data = input("Data do pedido (AAAA-MM-DD): ")
        pedidos = self.controller.buscar_pela_data(data)
        if pedidos:
            print("\nPedidos encontrados:")
            for pedido in pedidos:
                cliente = self.cliente_controller.buscar_por_id(pedido.id_cliente)
                cliente_nome = cliente.nome if cliente else "Desconhecido"
                print(f"ID: {pedido.id_pedido} | Data: {pedido.data_pedido} | Cliente: {cliente_nome}")
                print(f"Valor Total: R${pedido.valor_total:.2f} | Status: {pedido.status}")
        else:
            print("Nenhum pedido encontrado nesta data!")
            
    def mostrar_log_exclusao(self):
        print("\n--- Logs de Exclusão de Pedidos ---")
        print("1. Buscar por ID de pedido")
        print("2. Listar todos os logs")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            id_pedido = input("Digite o ID do pedido: ")
            logs = self.controller.mostrar_log_exclusao(id_pedido)
        elif opcao == "2":
            logs = self.controller.mostrar_log_exclusao()
        elif opcao == "0":
            return
        else:
            print("Opção inválida!")
            return
        
        if not logs:
            print("\nNenhum log encontrado.")
            return
        
        print("\n{:<5} {:<15} {:<10} {:<15} {:<20}".format(
            "ID Log", "ID Pedido", "ID Cliente", "Valor Total", "Data Exclusão"))
        print("-"*70)
        
        for log in logs:
            print("{:<5} {:<15} {:<10} R${:<13.2f} {:<20}".format(
                log[0], log[1], log[2], float(log[3]), str(log[4])))