import psycopg2
import datetime

# Registro de Exemplar
'''
def nome_da_função (coluna1, coluna2, ..., colunaN):
    conecta no banco
        realiza o insert
    desconecta do banco
'''
# Registro de Matricula




# Registro de Livro




# Registro de Autor




'''
EXEMPLO DE CONEXÃO
con = None
try:
    with psycopg2.connect(
                    database = "BiblioTEC", 
                    user = "postgres", 
                    password = "123456", 
                    host = "localhost",
                    port = "5432") as con:
    
        with con.cursor() as cur:

            # Código aqui            

except Exception as error:
    print(error)
finally:
    if con is not None:
        con.close()
'''
