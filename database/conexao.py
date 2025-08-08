import psycopg2

def conexao():
	return psycopg2.connect(
     host="localhost",
     database="sistema_de_vendas",
     user="postgres", 
     password="9950"
    )