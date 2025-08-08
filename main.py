from view.categoria_view import CategoriaView
from view.cliente_view import ClienteView
from view.endereco_view import EnderecoView
from view.produto_view import ProdutoView
from view.estoque_view import EstoqueView
from view.pedido_view import PedidoView
from view.pagamento_view import PagamentoView
from view.entrega_view import EntregaView
from view.comandos_avancados_view import ComandosAvancadosView
from view.itemPedido_view import ItemPedidoView


def main():
    categoria_view = CategoriaView()
    cliente_view = ClienteView()
    endereco_view = EnderecoView()
    produto_view = ProdutoView()
    estoque_view = EstoqueView()
    pedido_view = PedidoView()
    pagamento_view = PagamentoView()
    entrega_view = EntregaView()
    comandos_view = ComandosAvancadosView()
    item_pedido_view = ItemPedidoView()

    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE VENDAS ===")
        print("1. Categorias")
        print("2. Clientes")
        print("3. Endereços")
        print("4. Produtos")
        print("5. Estoque")
        print("6. Pedidos")
        print("7. Itens de Pedido")  
        print("8. Pagamentos")
        print("9. Entregas")
        print("10. Comandos Avançados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            categoria_view.menu()
        elif opcao == "2":
            cliente_view.menu()
        elif opcao == "3":
            endereco_view.menu()
        elif opcao == "4":
            produto_view.menu()
        elif opcao == "5":
            estoque_view.menu()
        elif opcao == "6":
            pedido_view.menu()
        elif opcao == "7":  
            item_pedido_view.menu()
        elif opcao == "8":
            pagamento_view.menu()
        elif opcao == "9":
            entrega_view.menu()
        elif opcao == "10":
            comandos_view.menu()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            
            
if __name__ == "__main__":
    main()