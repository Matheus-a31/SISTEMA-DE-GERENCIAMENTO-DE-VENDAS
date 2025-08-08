from controller.cliente_controller import ClienteController
from datetime import datetime

class ClienteView:
    def __init__(self):
        self.controller = ClienteController()

    def menu(self):
        while True:
            print("\n--- Menu Clientes ---")
            print("1. Listar Clientes")
            print("2. Adicionar Cliente")
            print("3. Atualizar Cliente")
            print("4. Remover Cliente")
            print("5. Buscar por ID")
            print("6. Buscar por CPF")
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
                self.buscar_por_cpf()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar(self):
        clientes = self.controller.listar()
        print("\nLista de Clientes:")
        for cli in clientes:
            print(f"ID: {cli.id_cliente} | Nome: {cli.nome} | CPF: {cli.cpf} | Telefone: {cli.telefone} | Email: {cli.email} | Cadastro: {cli.data_cadastro}")

    def adicionar(self):
        print("\nNovo Cliente:")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        data_cadastro = datetime.now().strftime("%Y-%m-%d")
        
        if self.controller.inserir(nome, cpf, telefone, data_cadastro, email):
            print("Cliente adicionado com sucesso!")
        else:
            print("Erro ao adicionar cliente.")

    def atualizar(self):
        self.listar()
        id_cliente = int(input("ID do cliente a atualizar: "))
        
        # Buscar cliente existente
        cliente = self.controller.buscar_por_id(id_cliente)
        if not cliente:
            print("Cliente não encontrado!")
            return
            
        print("\nDeixe em branco para manter o valor atual")
        nome = input(f"Nome [{cliente.nome}]: ") or cliente.nome
        cpf = input(f"CPF [{cliente.cpf}]: ") or cliente.cpf
        telefone = input(f"Telefone [{cliente.telefone}]: ") or cliente.telefone
        email = input(f"Email [{cliente.email}]: ") or cliente.email
        
        if self.controller.atualizar(id_cliente, nome, cpf, telefone, cliente.data_cadastro, email):
            print("Cliente atualizado com sucesso!")
        else:
            print("Erro ao atualizar cliente.")

    def remover(self):
        self.listar()
        id_cliente = int(input("ID do cliente a remover: "))
        if self.controller.deletar(id_cliente):
            print("Cliente removido com sucesso!")
        else:
            print("Erro ao remover cliente.")

    def buscar_por_id(self):
        id_cliente = int(input("ID do cliente: "))
        cliente = self.controller.buscar_por_id(id_cliente)
        if cliente:
            print(f"\nDetalhes do Cliente:")
            print(f"ID: {cliente.id_cliente} | Nome: {cliente.nome} | CPF: {cliente.cpf}")
            print(f"Telefone: {cliente.telefone} | Email: {cliente.email} | Cadastro: {cliente.data_cadastro}")
        else:
            print("Cliente não encontrado!")

    def buscar_por_cpf(self):
        cpf = input("CPF do cliente: ")
        clientes = self.controller.buscar_por_cpf(cpf)
        if clientes:
            print("\nClientes encontrados:")
            for cliente in clientes:
                print(f"ID: {cliente.id_cliente} | Nome: {cliente.nome} | CPF: {cliente.cpf}")
        else:
            print("Nenhum cliente encontrado com este CPF!")