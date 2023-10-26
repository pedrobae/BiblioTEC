import psycopg2
from datetime import date

# Registro de Exemplar

# Registro de Matricula

# Realizar Emprestimo
def emprestimo(cod_mat, cod_exemp):
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
        
        insert_script = 'INSERT INTO emprestimo (cod_matricula, cod_exemplar, dt_emprestimo) VALUES (%s, %s, %s)'
        insert_values = (cod_mat, cod_exemp, date.today)
        dt_dev_prev_script = 'UPDATE emprestimo SET dt_prevista_devolucao = dt_emprestimo + 14'
        
        cur.execute(insert_script, insert_values)
        cur.execute(dt_dev_prev_script)
    
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()
    
# Realizar Reserva (definir a ordem para calcular o data de emprestimo prevista)

# Transformar Reserva em Emprestimo (após uma devolucao)


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

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if con is not None:
        con.close()
