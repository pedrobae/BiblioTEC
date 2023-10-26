import psycopg2
from datetime import date
con = None
cur = None
try:
    con = psycopg2.connect(
        database = "BiblioTEC", 
        user = "postgres", 
        password = "123456", 
        host = "localhost",
        port = "5432"
        )

    cur = con.cursor()

    # Registro de Exemplar
    
    # Registro de Matricula
    
    # Realizar Emprestimo
    
    # Realizar Reserva (definir a ordem para calcular o data de emprestimo prevista)
    
    # Transformar Reserva em Emprestimo (após uma devolucao)
    

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if con is not None:
        con.close()
