# Sistema de Gerenciamento de Vendas

Este projeto é um sistema de gerenciamento de vendas desenvolvido em Python, utilizando uma interface de linha de comando (CLI) para interação com o usuário. O sistema permite o controle completo de entidades essenciais de um processo de vendas, como clientes, produtos, pedidos e estoque, com todos os dados persistidos em um banco de dados PostgreSQL.

## Arquitetura

O projeto foi estruturado seguindo o padrão de arquitetura **Model-View-Controller (MVC)** para garantir uma boa separação de responsabilidades, facilitando a manutenção e a escalabilidade do código.

  * **Model**: Camada responsável pela interação com o banco de dados. Contém a lógica de negócio, as regras de validação e as consultas SQL para manipular os dados. (Ex: `cliente_model.py`, `produto_model.py`).
  * **View**: Camada de apresentação responsável pela interface com o usuário. No caso deste projeto, é a interface de linha de comando que exibe menus, solicita dados e apresenta os resultados. (Ex: `cliente_view.py`, `produto_view.py`).
  * **Controller**: Camada que atua como intermediário entre o *Model* e a *View*. Recebe as solicitações do usuário (através da View), aciona os métodos apropriados no *Model* para processar os dados e retorna os resultados para a *View* exibir.

## Funcionalidades Principais

O sistema oferece gerenciamento completo (CRUD - Criar, Ler, Atualizar, Deletar) para as seguintes entidades:

  * **Categorias**: Gerenciamento de categorias de produtos.
  * **Clientes**: Cadastro e gerenciamento de informações de clientes.
  * **Endereços**: Controle dos endereços associados aos clientes.
  * **Produtos**: Gerenciamento de produtos, incluindo nome, descrição e preço.
  * **Estoque**: Controle da quantidade de cada produto disponível em estoque.
  * **Pedidos**: Criação e acompanhamento de pedidos de vendas.
  * **Itens de Pedido**: Detalhamento dos produtos contidos em cada pedido.
  * **Pagamentos**: Registro e consulta de informações de pagamento dos pedidos.
  * **Entregas**: Gerenciamento do processo de entrega, incluindo rastreamento e status.

### Comandos Avançados

Além das operações básicas de CRUD, o sistema possui um módulo para consultas complexas e geração de relatórios, como:

  * Listar todos os produtos com suas respectivas categorias.
  * Listar todos os pedidos com os dados do cliente associado.
  * Calcular o valor total gasto por cada cliente.
  * Encontrar produtos que nunca foram vendidos.
  * Listar clientes que gastaram acima de um determinado valor.

## Tecnologias Utilizadas

  * **Linguagem**: Python 3
  * **Banco de Dados**: PostgreSQL
  * **Conector**: `psycopg2`

## Pré-requisitos

Antes de executar o projeto, você precisará ter o seguinte instalado em sua máquina:

  * Python 3
  * PostgreSQL

## Configuração e Execução

Siga os passos abaixo para configurar e executar o projeto:

1.  **Clone o Repositório**

    ```bash
    git clone https://github.com/Matheus-a31/SISTEMA-DE-GERENCIAMENTO-DE-VENDAS.git
    ```

2.  **Instale as Dependências**
    O projeto utiliza a biblioteca `psycopg2` para se conectar ao PostgreSQL. Instale-a usando pip:

    ```bash
    pip install psycopg2-binary
    ```

3.  **Configure o Banco de Dados**

      * Certifique-se de que o seu serviço do PostgreSQL está ativo.
      * Crie um banco de dados com o nome `sistema_de_vendas`.
      * Execute os scripts SQL necessários para criar todas as tabelas (ex: `clientes`, `produtos`, `pedidos`, etc.) no banco de dados `sistema_de_vendas`.
      * Verifique e, se necessário, altere as credenciais de conexão no arquivo `conexao.py` para que correspondam à sua configuração local (host, database, user, password).

4.  **Execute a Aplicação**
    Para iniciar o sistema, execute o arquivo `main.py`:

    ```bash
    python main.py
    ```


    Isso abrirá o menu principal no seu terminal, onde você poderá navegar pelas diferentes opções do sistema.

