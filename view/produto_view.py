from controller.produto_controller import ProdutoController
from controller.categoria_controller import CategoriaController

class ProdutoView:
    def __init__(self):
        self.controller = ProdutoController()
        self.categoria_controller = CategoriaController()

    def menu(self):
        while True:
            print("\n--- Menu Produtos ---")
            print("1. Listar Produtos")
            print("2. Adicionar Produto")
            print("3. Atualizar Produto")
            print("4. Remover Produto")
            print("5. Buscar por ID")
            print("6. Buscar por Nome")
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
                self.buscar_por_nome()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar(self):
        produtos = self.controller.listar()
        print("\nLista de Produtos:")
        for prod in produtos:
            categoria = self.categoria_controller.buscar_por_id(prod.id_categoria)
            cat_nome = categoria.nome if categoria else "Desconhecida"
            print(f"ID: {prod.id_produto} | Nome: {prod.nome} | Preço: R${prod.preco:.2f}")
            print(f"Categoria: {cat_nome} | Descrição: {prod.descricao}")

    def adicionar(self):
        print("\nNovo Produto:")
        # Listar categorias disponíveis
        categorias = self.categoria_controller.listar()
        print("\nCategorias disponíveis:")
        for cat in categorias:
            print(f"ID: {cat.id_categoria} | Nome: {cat.nome}")
        
        id_categoria = int(input("ID da Categoria: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        
        if self.controller.inserir(id_categoria, nome, descricao, preco):
            print("Produto adicionado com sucesso!")
        else:
            print("Erro ao adicionar produto.")

    def atualizar(self):
        self.listar()
        id_produto = int(input("ID do produto a atualizar: "))
        
        # Buscar produto existente
        produto = self.controller.buscar_por_id(id_produto)
        if not produto:
            print("Produto não encontrado!")
            return
            
        print("\nDeixe em branco para manter o valor atual")
        # Listar categorias disponíveis
        categorias = self.categoria_controller.listar()
        print("\nCategorias disponíveis:")
        for cat in categorias:
            print(f"ID: {cat.id_categoria} | Nome: {cat.nome}")
        
        id_categoria = input(f"ID Categoria [{produto.id_categoria}]: ") or produto.id_categoria
        nome = input(f"Nome [{produto.nome}]: ") or produto.nome
        descricao = input(f"Descrição [{produto.descricao}]: ") or produto.descricao
        preco = input(f"Preço [{produto.preco}]: ") or produto.preco
        
        if self.controller.atualizar(id_produto, id_categoria, nome, descricao, float(preco)):
            print("Produto atualizado com sucesso!")
        else:
            print("Erro ao atualizar produto.")

    def remover(self):
        self.listar()
        id_produto = int(input("ID do produto a remover: "))
        if self.controller.deletar(id_produto):
            print("Produto removido com sucesso!")
        else:
            print("Erro ao remover produto.")

    def buscar_por_id(self):
        id_produto = int(input("ID do produto: "))
        produto = self.controller.buscar_por_id(id_produto)
        if produto:
            categoria = self.categoria_controller.buscar_por_id(produto.id_categoria)
            cat_nome = categoria.nome if categoria else "Desconhecida"
            print(f"\nDetalhes do Produto:")
            print(f"ID: {produto.id_produto} | Nome: {produto.nome} | Preço: R${produto.preco:.2f}")
            print(f"Categoria: {cat_nome} | Descrição: {produto.descricao}")
        else:
            print("Produto não encontrado!")

    def buscar_por_nome(self):
        nome = input("Nome do produto: ")
        produtos = self.controller.buscar_pelo_nome(nome)
        if produtos:
            print("\nProdutos encontrados:")
            for produto in produtos:
                categoria = self.categoria_controller.buscar_por_id(produto.id_categoria)
                cat_nome = categoria.nome if categoria else "Desconhecida"
                print(f"ID: {produto.id_produto} | Nome: {produto.nome} | Preço: R${produto.preco:.2f}")
                print(f"Categoria: {cat_nome}")
        else:
            print("Nenhum produto encontrado com este nome!")