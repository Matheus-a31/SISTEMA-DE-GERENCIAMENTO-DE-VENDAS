from controller.endereco_controller import EnderecoController
from view.cliente_view import ClienteView

class EnderecoView:
    def __init__(self):
        self.controller = EnderecoController()
        self.cliente_view = ClienteView()

    def menu(self):
        while True:
            print("\n--- Menu Endereços ---")
            print("1. Listar Endereços")
            print("2. Adicionar Endereço")
            print("3. Atualizar Endereço")
            print("4. Remover Endereço")
            print("5. Buscar por ID")
            print("6. Buscar por Cidade")
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
                self.buscar_por_cidade()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar(self):
        enderecos = self.controller.listar()
        print("\nLista de Endereços:")
        for end in enderecos:
            print(f"ID: {end.id_endereco} | Cliente ID: {end.id_cliente} | {end.logradouro}, {end.numero}")
            print(f"CEP: {end.cep} | {end.cidade}/{end.estado}")

    def adicionar(self):
        print("\nNovo Endereço:")
        self.cliente_view.listar()
        id_cliente = int(input("ID do Cliente: "))
        logradouro = input("Logradouro: ")
        numero = input("Número: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        
        if self.controller.inserir(id_cliente, logradouro, numero, cidade, estado, cep):
            print("Endereço adicionado com sucesso!")
        else:
            print("Erro ao adicionar endereço.")

    def atualizar(self):
        self.listar()
        id_endereco = int(input("ID do endereço a atualizar: "))
        
        # Buscar endereço existente
        endereco = self.controller.buscar_por_id(id_endereco)
        if not endereco:
            print("Endereço não encontrado!")
            return
            
        print("\nDeixe em branco para manter o valor atual")
        self.cliente_view.listar()
        id_cliente = input(f"ID Cliente [{endereco.id_cliente}]: ") or endereco.id_cliente
        logradouro = input(f"Logradouro [{endereco.logradouro}]: ") or endereco.logradouro
        numero = input(f"Número [{endereco.numero}]: ") or endereco.numero
        cidade = input(f"Cidade [{endereco.cidade}]: ") or endereco.cidade
        estado = input(f"Estado [{endereco.estado}]: ") or endereco.estado
        cep = input(f"CEP [{endereco.cep}]: ") or endereco.cep
        
        if self.controller.atualizar(id_endereco, id_cliente, logradouro, numero, cidade, estado, cep):
            print("Endereço atualizado com sucesso!")
        else:
            print("Erro ao atualizar endereço.")

    def remover(self):
        self.listar()
        id_endereco = int(input("ID do endereço a remover: "))
        if self.controller.deletar(id_endereco):
            print("Endereço removido com sucesso!")
        else:
            print("Erro ao remover endereço.")

    def buscar_por_id(self):
        id_endereco = int(input("ID do endereço: "))
        endereco = self.controller.buscar_por_id(id_endereco)
        if endereco:
            print(f"\nDetalhes do Endereço:")
            print(f"ID: {endereco.id_endereco} | Cliente ID: {endereco.id_cliente}")
            print(f"Endereço: {endereco.logradouro}, {endereco.numero}")
            print(f"CEP: {endereco.cep} | {endereco.cidade}/{endereco.estado}")
        else:
            print("Endereço não encontrado!")

    def buscar_por_cidade(self):
        cidade = input("Cidade: ")
        enderecos = self.controller.buscar_por_cidade(cidade)
        if enderecos:
            print("\nEndereços encontrados:")
            for end in enderecos:
                print(f"ID: {end.id_endereco} | Cliente ID: {end.id_cliente} | {end.logradouro}, {end.numero}")
                print(f"CEP: {end.cep} | {end.cidade}/{end.estado}")
        else:
            print("Nenhum endereço encontrado nesta cidade!")