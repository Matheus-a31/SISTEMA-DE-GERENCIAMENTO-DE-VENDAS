from controller.categoria_controller import CategoriaController

class CategoriaView:
    def __init__(self):
        self.controller = CategoriaController()

    def menu(self):
        while True:
            print("\n--- Menu Categorias ---")
            print("1. Listar Categorias")
            print("2. Adicionar Categoria")
            print("3. Atualizar Categoria")
            print("4. Remover Categoria")
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
        categorias = self.controller.listar()
        print("\nLista de Categorias:")
        for cat in categorias:
            print(f"ID: {cat.id_categoria} | Nome: {cat.nome} | Descrição: {cat.descricao}")

    def adicionar(self):
        print("\nNova Categoria:")
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        if self.controller.inserir(nome, descricao):
            print("Categoria adicionada com sucesso!")
        else:
            print("Erro ao adicionar categoria.")

    def atualizar(self):
        self.listar()
        id_categoria = int(input("ID da categoria a atualizar: "))
        nome = input("Novo nome (deixe em branco para manter): ")
        descricao = input("Nova descrição (deixe em branco para manter): ")
        
        # Buscar categoria existente
        categoria = self.controller.buscar_por_id(id_categoria)
        if not categoria:
            print("Categoria não encontrada!")
            return
            
        nome = nome if nome else categoria.nome
        descricao = descricao if descricao else categoria.descricao
        
        if self.controller.atualizar(id_categoria, nome, descricao):
            print("Categoria atualizada com sucesso!")
        else:
            print("Erro ao atualizar categoria.")

    def remover(self):
        self.listar()
        id_categoria = int(input("ID da categoria a remover: "))
        if self.controller.deletar(id_categoria):
            print("Categoria removida com sucesso!")
        else:
            print("Erro ao remover categoria.")

    def buscar_por_id(self):
        id_categoria = int(input("ID da categoria: "))
        categoria = self.controller.buscar_por_id(id_categoria)
        if categoria:
            print(f"\nDetalhes da Categoria:")
            print(f"ID: {categoria.id_categoria} | Nome: {categoria.nome} | Descrição: {categoria.descricao}")
        else:
            print("Categoria não encontrada!")

    def buscar_por_nome(self):
        nome = input("Nome da categoria: ")
        categoria = self.controller.buscar_por_nome(nome)
        if categoria:
            print(f"\nDetalhes da Categoria:")
            print(f"ID: {categoria.id_categoria} | Nome: {categoria.nome} | Descrição: {categoria.descricao}")
        else:
            print("Categoria não encontrada!")