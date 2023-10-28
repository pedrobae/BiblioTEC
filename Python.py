import psycopg2
from datetime import datetime
from datetime import date
from datetime import timedelta

# Registro de Exemplar


# Registro de Matricula


# Realizar Emprestimo - Checa reservas para atualizar datas previstas e preeencher data de emprestimo)
def emprestimo(cod_mat, cod_exemp):
    con = None
    try:
        with psycopg2.connect(
                        database = "teste", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
        
            with con.cursor() as cur:
        
                today = date.today()
                
                select_emp = "SELECT * FROM emprestimo WHERE emprestimo.cod_exemplar = {0} AND emprestimo.dt_devolucao IS NULL".format(str(cod_exemp))
                cur.execute(select_emp)
                emprestimo = cur.fetchall()
                
                if emprestimo == []:
                    select_script = "SELECT * FROM reserva WHERE reserva.cod_exemplar = {0} AND reserva.dt_emprestimo IS NULL".format(str(cod_exemp))
                    cur.execute(select_script)
                    queue = []
                    for tuple in cur.fetchall():
                        queue.append(tuple)

                    if queue == []:
                        insert_emp = "INSERT INTO emprestimo (cod_matricula, cod_exemplar, dt_emprestimo) VALUES ({0}, {1}, '{2}')".format(cod_mat, cod_exemp, str(today))
                        update_emp = "UPDATE emprestimo SET dt_prevista_devolucao = dt_emprestimo + 14"
                        cur.execute(insert_emp)
                        cur.execute(update_emp)
                        
                    elif cod_mat == queue[0][1]:
                        insert_emp = "INSERT INTO emprestimo (cod_matricula, cod_exemplar, dt_emprestimo) VALUES ({0}, {1}, '{2}')".format(cod_mat, cod_exemp, str(today))
                        update_emp = "UPDATE emprestimo SET dt_prevista_devolucao = dt_emprestimo + 14"
                        cur.execute(insert_emp)
                        cur.execute(update_emp)
                        
                        update_res = "UPDATE reserva SET dt_emprestimo = '{0}' WHERE cod_reserva = {1}".format(str(today), queue[0][0])
                        cur.execute(update_res)

                        delay = today - queue[0][4]
                        for i in range(1, len(queue)):
                            new_dt_prev = queue[i][4] + delay
                            update_dt_prev = "UPDATE reserva SET dt_prevista_emprestimo = '{0}' WHERE dt_prevista_emprestimo = '{1}'".format(str(new_dt_prev), str(queue[i][4]))
                            cur.execute(update_dt_prev)

                    else:
                        print("O exemplar está reservado.")
                else:
                    print("O exemplar está emprestado, realize a devolução primeiro.")
        
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()


# Realizar Reserva - Define a ordem para calcular a data de emprestimo prevista
def reserva(cod_mat, cod_exemp):
    con = None
    try:
        with psycopg2.connect(
                        database = "teste", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
                
            with con.cursor() as cur:
        
                today = date.today()
                now = datetime.now()
                
                select_emp = "SELECT * FROM emprestimo WHERE emprestimo.cod_exemplar = {0} AND emprestimo.dt_devolucao IS NULL".format(str(cod_exemp))
                cur.execute(select_emp)
                emprestimo = cur.fetchall()  
                
                if emprestimo != []:
                    select_script = "SELECT * FROM reserva WHERE reserva.cod_exemplar = {0} AND reserva.dt_emprestimo IS NULL".format(str(cod_exemp))
                    cur.execute(select_script)
                    queue = [today]
                    for tuple in cur.fetchall():
                        queue.append(tuple[4])
            
                    delay = max(queue) + timedelta(14)
                    insert_script = "INSERT INTO reserva (cod_matricula, cod_exemplar, dt_reserva, dt_prevista_emprestimo) VALUES ({0}, {1}, '{2}', '{3}')".format(cod_mat, cod_exemp, str(now), str(delay))
                    cur.execute(insert_script)
                    
                else:
                        print("O exemplar está disponível.")
            
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()


# Devoluçao - Acusa uma reserva
def devolucao(cod_exemp):
    con = None
    try:
        with psycopg2.connect(
                        database = "teste", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
                
                with con.cursor() as cur:
            
                    today = date.today()
                    now = datetime.now()
                    
                    select_emp = "SELECT * FROM emprestimo WHERE emprestimo.cod_exemplar = {0} AND emprestimo.dt_devolucao IS NULL".format(str(cod_exemp))
                    cur.execute(select_emp)
                    emprestimo = cur.fetchall() 
                    
                    if emprestimo != []:
                        cod_emp = emprestimo[0][0]
                    
                        update_emp = "UPDATE emprestimo SET dt_devolucao = '{0}' WHERE cod_emprestimo = {1}".format(str(today), cod_emp)
                        cur.execute(update_emp)
                        
                        select_res = "SELECT * FROM reserva WHERE reserva.cod_exemplar = {0} AND reserva.dt_emprestimo IS NULL".format(str(cod_exemp))
                        cur.execute(select_res)
                        reservas = cur.fetchall()
                        
                        if reservas != []:
                            cod_mat = reservas[0][1]
                            
                            select_mat = "SELECT * FROM matricula WHERE matricula.cod_matricula = {0}".format(str(cod_mat))           
                            cur.execute(select_mat)
                            matricula_reserva = cur.fetchall()
                            
                            print("O livro está reservado por", matricula_reserva[0][3], "- e-mail - ", matricula_reserva[0][7])
                       
                        else:
                            print("O exemplar não está reservado.")
                            
                    else:
                        print("O exemplar não está emprestado.")
                        
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()

'''
--> Exemplo de Conexão

con = None
cur = None
try:
    with psycopg2.connect(
                    database = "BiblioTEC", 
                    user = "postgres", 
                    password = "123456", 
                    host = "localhost",
                    port = "5432") as con:

        with con.cursor() as cur:
            
            # codigo aqui
    
except Exception as error:
    print(error)
finally:
    if con is not None:
        con.close()
'''
