import psycopg2
from datetime import datetime
from datetime import date
from datetime import timedelta


# Registro de Exemplar


# Registro de Matricula


# Realizar Emprestimo
def emprestimo(cod_mat, cod_exemp):
    con = None
    cur = None
    try:
        con = psycopg2.connect(
            database = "teste", 
            user = "postgres", 
            password = "123456", 
            host = "localhost",
            port = "5432"
            )
        cur = con.cursor()  
        
        today = datetime.date.today()
        
        insert_script = 'INSERT INTO emprestimo (cod_matricula, cod_exemplar, dt_emprestimo) VALUES (%s, %s, %s)'
        insert_values = (cod_mat, cod_exemp, str(today))
        update_script = 'UPDATE emprestimo SET dt_prevista_devolucao = dt_emprestimo + 14'
        
        cur.execute(insert_script, insert_values)
        cur.execute(update_script)

        con.commit()
    
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()


# Realizar Reserva (definir a ordem para calcular o data de emprestimo prevista)
def reserva(cod_mat, cod_exemp):
    con = None
    cur = None
    try:
        con = psycopg2.connect(
            database = "teste", 
            user = "postgres", 
            password = "123456", 
            host = "localhost",
            port = "5432"
            )
        cur = con.cursor() 
        
        today = date.today()
        now = datetime.now()
        
        select_script = ('SELECT * FROM reserva WHERE reserva.cod_exemplar = (%s) AND reserva.dt_emprestimo IS NULL')
        select_values = (str(cod_exemp))
        cur.execute(select_script, select_values)

        queue = [today]
        for tuple in cur.fetchall():
            queue.append(tuple[4])

        delay = max(queue) + timedelta(14)
        
        insert_script = 'INSERT INTO reserva (cod_matricula, cod_exemplar, dt_reserva, dt_prevista_emprestimo) VALUES (%s, %s, %s, %s)'
        insert_values = (cod_mat, cod_exemp, str(now), str(delay))
        cur.execute(insert_script, insert_values)
        
        con.commit()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()


# Transformar Reserva em Emprestimo (após uma devolucao)


#Exemlo de Conexão
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

    # codigo aqui
    
    con.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if con is not None:
        con.close()
