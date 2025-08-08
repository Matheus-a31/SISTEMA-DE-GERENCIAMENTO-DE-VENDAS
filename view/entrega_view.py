from controller.entrega_controller import EntregaController
from controller.pedido_controller import PedidoController
from controller.endereco_controller import EnderecoController
from datetime import datetime, timedelta

class EntregaView:
    def __init__(self):
        self.controller = EntregaController()
        self.pedido_controller = PedidoController()
        self.endereco_controller = EnderecoController()

    def menu(self):
        while True:
            print("\n--- Menu Entregas ---")
            print("1. Listar Entregas")
            print("2. Registrar Entrega")
            print("3. Atualizar Entrega")
            print("4. Cancelar Entrega")
            print("5. Buscar por ID")
            print("6. Buscar por Status")
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
                self.buscar_por_status()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar(self):
        entregas = self.controller.listar()
        print("\nLista de Entregas:")
        for ent in entregas:
            print(f"ID: {ent.id_entrega} | Pedido ID: {ent.id_pedido}")
            print(f"Transportadora: {ent.transportadora} | Código Rastreio: {ent.codigo_rastreio}")
            print(f"Data Envio: {ent.data_envio} | Data Estimada: {ent.data_entrega_estimada}")
            print(f"Status: {ent.status}")

    def registrar(self):
        print("\nRegistrar Entrega:")
        # Listar pedidos disponíveis
        pedidos = self.pedido_controller.listar()
        print("\nPedidos disponíveis:")
        for ped in pedidos:
            print(f"ID: {ped.id_pedido} | Valor: R${ped.valor_total:.2f}")
        
        id_pedido = int(input("ID do Pedido: "))
        transportadora = input("Transportadora: ")
        codigo_rastreio = input("Código de Rastreio: ")
        custo_frete = float(input("Custo do Frete: "))
        data_envio = datetime.now().strftime("%Y-%m-%d")
        data_entrega_estimada = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")  # 7 dias após envio
        status = "Em trânsito"
        
        if self.controller.inserir(id_pedido, transportadora, codigo_rastreio, custo_frete, data_envio, data_entrega_estimada, None, status):
            print("Entrega registrada com sucesso!")
        else:
            print("Erro ao registrar entrega.")

    def atualizar(self):
        self.listar()
        id_entrega = int(input("ID da entrega a atualizar: "))
        
        # Buscar entrega existente
        entrega = self.controller.buscar_por_id(id_entrega)
        if not entrega:
            print("Entrega não encontrada!")
            return
        
        print("\nDeixe em branco para manter o valor atual")
        # Listar pedidos disponíveis
        pedidos = self.pedido_controller.listar()
        print("\nPedidos disponíveis:")
        for ped in pedidos:
            print(f"ID: {ped.id_pedido} | Valor: R${ped.valor_total:.2f}")
        
        id_pedido = input(f"ID Pedido [{entrega.id_pedido}]: ") or entrega.id_pedido
        transportadora = input(f"Transportadora [{entrega.transportadora}]: ") or entrega.transportadora
        codigo_rastreio = input(f"Código Rastreio [{entrega.codigo_rastreio}]: ") or entrega.codigo_rastreio
        custo_frete = input(f"Custo Frete [{entrega.custo_frete}]: ") or entrega.custo_frete
        data_envio = input(f"Data Envio [{entrega.data_envio}]: ") or entrega.data_envio
        data_entrega_estimada = input(f"Data Estimada [{entrega.data_entrega_estimada}]: ") or entrega.data_entrega_estimada
        data_entrega_real = input(f"Data Real [{'Não entregue' if not entrega.data_entrega_real else entrega.data_entrega_real}]: ") or entrega.data_entrega_real
        status = input(f"Status [{entrega.status}]: ") or entrega.status
        
        if self.controller.atualizar(
            id_entrega=id_entrega,
            id_pedido=id_pedido,
            transportadora=transportadora,
            codigo_rastreio=codigo_rastreio,
            custo_frete=float(custo_frete),
            data_envio=data_envio,
            data_entrega_estimada=data_entrega_estimada,
            data_entrega_real=data_entrega_real,
            status=status
        ):
            print("Entrega atualizada com sucesso!")
        else:
            print("Erro ao atualizar entrega.")

    def cancelar(self):
        self.listar()
        id_entrega = int(input("ID da entrega a cancelar: "))
        if self.controller.deletar(id_entrega):
            print("Entrega cancelada com sucesso!")
        else:
            print("Erro ao cancelar entrega.")

    def buscar_por_id(self):
        id_entrega = int(input("ID da entrega: "))
        entrega = self.controller.buscar_por_id(id_entrega)
        if entrega:
            print(f"\nDetalhes da Entrega:")
            print(f"ID: {entrega.id_entrega} | Pedido ID: {entrega.id_pedido}")
            print(f"Transportadora: {entrega.transportadora} | Código Rastreio: {entrega.codigo_rastreio}")
            print(f"Data Envio: {entrega.data_envio} | Data Estimada: {entrega.data_entrega_estimada}")
            if entrega.data_entrega_real:
                print(f"Data Real: {entrega.data_entrega_real}")
            print(f"Status: {entrega.status}")
        else:
            print("Entrega não encontrada!")

    def buscar_por_status(self):
        status = input("Status da entrega (ex: 'Em trânsito', 'Entregue', 'Pendente'): ")
        entregas = self.controller.buscar_por_status(status)
        if entregas:
            print("\nEntregas encontradas:")
            for entrega in entregas:
                print(f"ID: {entrega.id_entrega} | Pedido ID: {entrega.id_pedido}")
                print(f"Transportadora: {entrega.transportadora} | Status: {entrega.status}")
                print(f"Data Envio: {entrega.data_envio} | Data Entrega: {entrega.data_entrega_real or 'Não entregue'}")
        else:
            print("Nenhuma entrega encontrada com este status!")