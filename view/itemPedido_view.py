from controller.itemPedido_controller import ItemPedidoController
from controller.pedido_controller import PedidoController
from controller.produto_controller import ProdutoController

class ItemPedidoView:
    def __init__(self):
        self.controller = ItemPedidoController()
        self.pedido_controller = PedidoController()
        self.produto_controller = ProdutoController()

    def menu(self):
        while True:
            print("\n--- Menu Itens de Pedido ---")
            print("1. Listar Itens de Pedido")
            print("2. Adicionar Item a Pedido")
            print("3. Atualizar Item de Pedido")
            print("4. Remover Item de Pedido")
            print("5. Buscar por ID")
            print("6. Buscar por Pedido")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar()
            elif opcao == "2":
                self.adicionar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.remover()
            elif opcao == "5":
                self.buscar_por_id()
            elif opcao == "6":
                self.buscar_por_pedido()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar(self):
        itens = self.controller.listar()
        print("\nLista de Itens de Pedido:")
        for item in itens:
            pedido = self.pedido_controller.buscar_por_id(item.id_pedido)
            produto = self.produto_controller.buscar_por_id(item.id_produto)
            
            pedido_info = f"Pedido ID: {item.id_pedido}"
            if pedido:
                pedido_info += f" (Valor Total: R${pedido.valor_total:.2f})"
                
            prod_info = f"Produto ID: {item.id_produto}"
            if produto:
                prod_info += f" ({produto.nome})"
            
            print(f"ID: {item.id_itemPedido} | {pedido_info} | {prod_info}")
            print(f"Quantidade: {item.quantidade} | Preço Unitário: R${item.preco_unitario:.2f}")
            print(f"Subtotal: R${item.quantidade * item.preco_unitario:.2f}")

    def adicionar(self):
        print("\nAdicionar Item a Pedido:")
        # Listar pedidos disponíveis
        pedidos = self.pedido_controller.listar()
        print("\nPedidos disponíveis:")
        for ped in pedidos:
            print(f"ID: {ped.id_pedido} | Valor Total: R${ped.valor_total:.2f} | Status: {ped.status}")
        
        id_pedido = int(input("ID do Pedido: "))
        
        # Listar produtos disponíveis
        produtos = self.produto_controller.listar()
        print("\nProdutos disponíveis:")
        for prod in produtos:
            print(f"ID: {prod.id_produto} | Nome: {prod.nome} | Preço: R${prod.preco:.2f}")
        
        id_produto = int(input("ID do Produto: "))
        quantidade = int(input("Quantidade: "))
        
        # Buscar preço do produto
        produto = self.produto_controller.buscar_por_id(id_produto)
        if not produto:
            print("Produto não encontrado!")
            return
            
        preco_unitario = produto.preco
        
        if self.controller.inserir(id_pedido, id_produto, quantidade, preco_unitario):
            print("Item adicionado ao pedido com sucesso!")
            
            # Atualizar valor total do pedido
            self._atualizar_valor_pedido(id_pedido)
        else:
            print("Erro ao adicionar item ao pedido.")

    def atualizar(self):
        self.listar()
        id_item = int(input("ID do item a atualizar: "))
        
        # Buscar item existente
        item = self.controller.buscar_por_id(id_item)
        if not item:
            print("Item não encontrado!")
            return
            
        print("\nDeixe em branco para manter o valor atual")
        # Listar pedidos disponíveis
        pedidos = self.pedido_controller.listar()
        print("\nPedidos disponíveis:")
        for ped in pedidos:
            print(f"ID: {ped.id_pedido} | Valor Total: R${ped.valor_total:.2f}")
        
        id_pedido = input(f"ID Pedido [{item.id_pedido}]: ") or item.id_pedido
        
        # Listar produtos disponíveis
        produtos = self.produto_controller.listar()
        print("\nProdutos disponíveis:")
        for prod in produtos:
            print(f"ID: {prod.id_produto} | Nome: {prod.nome} | Preço: R${prod.preco:.2f}")
        
        id_produto = input(f"ID Produto [{item.id_produto}]: ") or item.id_produto
        quantidade = input(f"Quantidade [{item.quantidade}]: ") or item.quantidade
        
        # Se o produto foi alterado, buscar novo preço
        if str(id_produto) != str(item.id_produto):
            produto = self.produto_controller.buscar_por_id(id_produto)
            if not produto:
                print("Produto não encontrado!")
                return
            preco_unitario = produto.preco
        else:
            preco_unitario = item.preco_unitario
        
        if self.controller.atualizar(id_item, id_pedido, id_produto, int(quantidade), float(preco_unitario)):
            print("Item do pedido atualizado com sucesso!")
            
            # Atualizar valor total do pedido
            self._atualizar_valor_pedido(id_pedido)
        else:
            print("Erro ao atualizar item do pedido.")

    def remover(self):
        self.listar()
        id_item = int(input("ID do item a remover: "))
        
        # Buscar item para obter o ID do pedido
        item = self.controller.buscar_por_id(id_item)
        if not item:
            print("Item não encontrado!")
            return
            
        if self.controller.deletar(id_item):
            print("Item removido do pedido com sucesso!")
            
            # Atualizar valor total do pedido
            self._atualizar_valor_pedido(item.id_pedido)
        else:
            print("Erro ao remover item do pedido.")

    def buscar_por_id(self):
        id_item = int(input("ID do item: "))
        item = self.controller.buscar_por_id(id_item)
        if item:
            pedido = self.pedido_controller.buscar_por_id(item.id_pedido)
            produto = self.produto_controller.buscar_por_id(item.id_produto)
            
            pedido_info = f"Pedido ID: {item.id_pedido}"
            if pedido:
                pedido_info += f" (Valor Total: R${pedido.valor_total:.2f})"
                
            prod_info = f"Produto ID: {item.id_produto}"
            if produto:
                prod_info += f" ({produto.nome})"
            
            print(f"\nDetalhes do Item:")
            print(f"ID: {item.id_itemPedido} | {pedido_info} | {prod_info}")
            print(f"Quantidade: {item.quantidade} | Preço Unitário: R${item.preco_unitario:.2f}")
            print(f"Subtotal: R${item.quantidade * item.preco_unitario:.2f}")
        else:
            print("Item não encontrado!")

    def buscar_por_pedido(self):
        id_pedido = int(input("ID do Pedido: "))
        itens = self.controller.buscar_por_pedido(id_pedido)
        if itens:
            pedido = self.pedido_controller.buscar_por_id(id_pedido)
            print(f"\nItens do Pedido {id_pedido}:")
            if pedido:
                print(f"Cliente ID: {pedido.id_cliente} | Valor Total: R${pedido.valor_total:.2f}")
            
            total = 0
            for item in itens:
                produto = self.produto_controller.buscar_por_id(item.id_produto)
                prod_info = f"Produto ID: {item.id_produto}"
                if produto:
                    prod_info += f" ({produto.nome})"
                
                subtotal = item.quantidade * item.preco_unitario
                total += subtotal
                
                print(f"ID: {item.id_itemPedido} | {prod_info}")
                print(f"Quantidade: {item.quantidade} | Preço Unitário: R${item.preco_unitario:.2f}")
                print(f"Subtotal: R${subtotal:.2f}")
                print("-" * 40)
            
            print(f"Total do Pedido: R${total:.2f}")
        else:
            print("Nenhum item encontrado para este pedido!")

    def _atualizar_valor_pedido(self, id_pedido):
        # Calcular novo valor total do pedido
        itens = self.controller.buscar_por_pedido(id_pedido)
        valor_total = sum(item.quantidade * item.preco_unitario for item in itens)
        
        # Buscar pedido existente
        pedido = self.pedido_controller.buscar_por_id(id_pedido)
        if not pedido:
            return
            
        # Atualizar pedido com novo valor total
        self.pedido_controller.atualizar(
            pedido.id_pedido, 
            pedido.id_cliente, 
            pedido.data_pedido, 
            valor_total, 
            pedido.status
        )