from controller.comandos_avancados_controller import ComandosAvancadosController

class ComandosAvancadosView:
    def __init__(self):
        self.controller = ComandosAvancadosController()

    def menu(self):
        while True:
            print("\n--- Comandos Avançados ---")
            print("1. Listar Produtos com Categorias")
            print("2. Listar Pedidos com Clientes")
            print("3. Calcular Total Gasto por Cliente")
            print("4. Encontrar Produtos Nunca Vendidos")
            print("5. Clientes com Gastos Acima de X")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar_produtos_com_categoria()
            elif opcao == "2":
                self.listar_pedidos_com_cliente()
            elif opcao == "3":
                self.calcular_total_gasto_por_cliente()
            elif opcao == "4":
                self.encontrar_produtos_nunca_vendidos()
            elif opcao == "5":
                self.clientes_com_gastos_acima_de()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def listar_produtos_com_categoria(self):
        resultados = self.controller.listar_produtos_com_categoria()
        print("\nProdutos com Categorias:")
        for row in resultados:
            print(f"Produto: {row[0]} | Preço: R${row[1]:.2f} | Categoria: {row[2]}")

    def listar_pedidos_com_cliente(self):
        resultados = self.controller.listar_pedidos_com_cliente()
        print("\nPedidos com Clientes:")
        for row in resultados:
            print(f"Pedido ID: {row[0]} | Data: {row[1]} | Cliente: {row[2]} | Total: R${row[3]:.2f}")

    def calcular_total_gasto_por_cliente(self):
        resultados = self.controller.calcular_total_gasto_por_cliente()
        print("\nTotal Gasto por Cliente:")
        for row in resultados:
            print(f"Cliente: {row[0]} | Nº Pedidos: {row[1]} | Total Gasto: R${row[2]:.2f}")

    def encontrar_produtos_nunca_vendidos(self):
        resultados = self.controller.encontrar_produtos_nunca_vendidos()
        print("\nProdutos Nunca Vendidos:")
        for row in resultados:
            print(f"Produto: {row[0]} | Preço: R${row[1]:.2f}")

    def clientes_com_gastos_acima_de(self):
        valor_minimo = float(input("Digite o valor mínimo: "))
        resultados = self.controller.clientes_com_gastos_acima_de(valor_minimo)
        print(f"\nClientes com Gastos Acima de R${valor_minimo:.2f}:")
        for row in resultados:
            print(f"Cliente: {row[0]} | Total Gasto: R${row[1]:.2f}")