from controller.estoque_controller import EstoqueController
from controller.produto_controller import ProdutoController

class EstoqueView:
    def __init__(self):
        self.controller = EstoqueController()
        self.produto_controller = ProdutoController()

    def menu(self):
        while True:
            print("\n--- Menu Estoque ---")
            print("1. Listar Estoque")
            print("2. Adicionar Item ao Estoque")
            print("3. Atualizar Item no Estoque")
            print("4. Remover Item do Estoque")
            print("5. Buscar por ID")
            print("6. Buscar por Produto")
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
                self.buscar_por_produto()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar(self):
        itens = self.controller.listar()
        print("\nLista de Estoque:")
        for item in itens:
            produto = self.produto_controller.buscar_por_id(item.id_produto)
            prod_nome = produto.nome if produto else "Desconhecido"
            print(f"ID: {item.id_estoque} | Produto: {prod_nome} | Quantidade: {item.quantidade_disponivel}")

    def adicionar(self):
        print("\nNovo Item no Estoque:")
        # Listar produtos disponíveis
        produtos = self.produto_controller.listar()
        print("\nProdutos disponíveis:")
        for prod in produtos:
            print(f"ID: {prod.id_produto} | Nome: {prod.nome}")
        
        id_produto = int(input("ID do Produto: "))
        quantidade = int(input("Quantidade: "))
        
        if self.controller.inserir(id_produto, quantidade):
            print("Item adicionado ao estoque com sucesso!")
        else:
            print("Erro ao adicionar item ao estoque.")

    def atualizar(self):
        self.listar()
        id_estoque = int(input("ID do item no estoque a atualizar: "))
        
        # Buscar item existente
        item = self.controller.buscar_por_id(id_estoque)
        if not item:
            print("Item não encontrado no estoque!")
            return
            
        print("\nDeixe em branco para manter o valor atual")
        # Listar produtos disponíveis
        produtos = self.produto_controller.listar()
        print("\nProdutos disponíveis:")
        for prod in produtos:
            print(f"ID: {prod.id_produto} | Nome: {prod.nome}")
        
        id_produto = input(f"ID Produto [{item.id_produto}]: ") or item.id_produto
        quantidade = input(f"Quantidade [{item.quantidade_disponivel}]: ") or item.quantidade_disponivel
        
        if self.controller.atualizar(id_estoque, id_produto, int(quantidade)):
            print("Item do estoque atualizado com sucesso!")
        else:
            print("Erro ao atualizar item do estoque.")

    def remover(self):
        self.listar()
        id_estoque = int(input("ID do item no estoque a remover: "))
        if self.controller.deletar(id_estoque):
            print("Item removido do estoque com sucesso!")
        else:
            print("Erro ao remover item do estoque.")

    def buscar_por_id(self):
        id_estoque = int(input("ID do item no estoque: "))
        item = self.controller.buscar_por_id(id_estoque)
        if item:
            produto = self.produto_controller.buscar_por_id(item.id_produto)
            prod_nome = produto.nome if produto else "Desconhecido"
            print(f"\nDetalhes do Item no Estoque:")
            print(f"ID: {item.id_estoque} | Produto: {prod_nome} | Quantidade: {item.quantidade_disponivel}")
        else:
            print("Item não encontrado no estoque!")

    def buscar_por_produto(self):
        id_produto = int(input("ID do Produto: "))
        item = self.controller.buscar_por_produto(id_produto)
        if item:
            produto = self.produto_controller.buscar_por_id(item.id_produto)
            prod_nome = produto.nome if produto else "Desconhecido"
            print(f"\nDetalhes do Item no Estoque:")
            print(f"ID: {item.id_estoque} | Produto: {prod_nome} | Quantidade: {item.quantidade_disponivel}")
        else:
            print("Nenhum item encontrado para este produto!")