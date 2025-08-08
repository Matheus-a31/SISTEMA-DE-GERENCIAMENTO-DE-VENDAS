from database.conexao import conexao as conectar

class ComansdosAvancadosModel:
    
    def listar_produtos_com_categoria(self):
        conn = conectar()
        if not conn: return []
        try:
            with conn.cursor() as cur:
                sql = """
                    SELECT p.nome, p.preco, c.nome as categoria
                    FROM produto p
                    JOIN categoria c ON p.id_categoria = c.id_categoria
                    ORDER BY c.nome, p.nome;
                """
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()

    def listar_pedidos_com_cliente(self):
        conn = conectar()
        if not conn: return []
        try:
            with conn.cursor() as cur:
                sql = """
                    SELECT p.id_pedido, p.data_pedido, c.nome as cliente, p.valor_total
                    FROM pedido p
                    JOIN cliente c ON p.id_cliente = c.id_cliente
                    ORDER BY p.data_pedido DESC;
                """
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()
            
    def calcular_total_gasto_por_cliente(self):
        conn = conectar()
        if not conn: return []
        try:
            with conn.cursor() as cur:
                sql = """
                    SELECT c.nome, COUNT(p.id_pedido) as num_pedidos, SUM(p.valor_total) as total_gasto
                    FROM cliente c
                    JOIN pedido p ON c.id_cliente = p.id_cliente
                    GROUP BY c.nome
                    ORDER BY total_gasto DESC;
                """
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()
    
    def encontrar_produtos_nunca_vendidos(self):
        conn = conectar()
        if not conn: return []
        try:
            with conn.cursor() as cur:
                sql = """
                    SELECT p.nome, p.preco
                    FROM produto p
                    LEFT JOIN itemPedido ip ON p.id_produto = ip.id_produto
                    WHERE ip.id_itemPedido IS NULL;
                """
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()
    
    def clientes_com_gastos_acima_de(self, valor_minimo):
        conn = conectar()
        if not conn: return []
        try:
            with conn.cursor() as cur:
                sql = """
                    SELECT c.nome, SUM(p.valor_total) as total_gasto
                    FROM cliente c
                    JOIN pedido p ON c.id_cliente = p.id_cliente
                    GROUP BY c.nome
                    HAVING SUM(p.valor_total) > %s
                    ORDER BY total_gasto DESC;
                """
                cur.execute(sql, (valor_minimo,))
                return cur.fetchall()
        finally:
            conn.close()