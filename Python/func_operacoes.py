import psycopg2
from datetime import datetime, date, timedelta

# Realizar Emprestimo - Checa reservas para atualizar datas previstas e preeencher data de emprestimo)
def emprestimo(cod_mat, cod_exemp, today = date.today()):
    retorno = 0
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
        
            with con.cursor() as cur:
        
                select_emp = "SELECT * FROM emprestimo WHERE emprestimo.cod_exemplar = {0} AND emprestimo.dt_devolucao IS NULL".format(str(cod_exemp))
                cur.execute(select_emp)
                emprestimo = cur.fetchall()
                
                if emprestimo == []:
                    select_script = "SELECT * FROM reserva  r WHERE r.cod_exemplar = {0} AND r.situacao_res = 'ATIVA' ORDER BY r.dt_reserva ASC".format(str(cod_exemp))
                    cur.execute(select_script)
                    queue = []
                    
                    for tuple in cur.fetchall():
                        queue.append(tuple)

                    if queue == []:
                        insert_emp = "INSERT INTO emprestimo (cod_matricula, cod_exemplar, dt_emprestimo) VALUES ({0}, {1}, '{2}')".format(cod_mat, cod_exemp, str(today))
                        update_emp = "UPDATE emprestimo SET dt_prevista_devolucao = dt_emprestimo + 14"
                        cur.execute(insert_emp)
                        cur.execute(update_emp)
                        
                        update_exemp = "UPDATE exemplar SET cod_situacao = 2 WHERE cod_exemplar = {0}".format(cod_exemp)
                        cur.execute(update_exemp)
                        
                        # print("Empréstimo Efetuado")
                        retorno = "Empréstimo Efetuado."
                        
                    elif int(cod_mat) == int(queue[0][1]):
                        insert_emp = "INSERT INTO emprestimo (cod_matricula, cod_exemplar, dt_emprestimo) VALUES ({0}, {1}, '{2}')".format(cod_mat, cod_exemp, str(today))
                        update_emp = "UPDATE emprestimo SET dt_prevista_devolucao = dt_emprestimo + 14"
                        cur.execute(insert_emp)
                        cur.execute(update_emp)
                        
                        update_exemp = "UPDATE exemplar SET cod_situacao = 2 WHERE cod_exemplar = {0}".format(cod_exemp)
                        cur.execute(update_exemp)
                        
                        update_res = "UPDATE reserva SET dt_emprestimo = '{0}', situacao_res = 'INATIVA' WHERE cod_reserva = {1}".format(str(today), queue[0][0])
                        cur.execute(update_res)

                        delay = today - queue[0][4]
                        for i in range(1, len(queue)):
                            new_dt_prev = queue[i][4] + delay
                            update_dt_prev = "UPDATE reserva SET dt_prevista_emprestimo = '{0}' WHERE dt_prevista_emprestimo = '{1}'".format(str(new_dt_prev), str(queue[i][4]))
                            cur.execute(update_dt_prev)

                        # print("Empréstimo Efetuado")
                        retorno = "Empréstimo Efetuado."

                    else:
                        # print("O exemplar está reservado.")
                        retorno = "O exemplar está reservado."
                else:
                    # print("O exemplar está emprestado, realize a devolução primeiro.")
                    retorno = "O exemplar está emprestado."
        
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    return retorno



# Realizar Reserva - Define a ordem para calcular a data de emprestimo prevista
def reserva(cod_mat, cod_exemp, today = date.today(), now = datetime.now()):
    retorno = 0
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
                
            with con.cursor() as cur:
        
                select_emp = "SELECT * FROM emprestimo WHERE emprestimo.cod_exemplar = {0} AND emprestimo.dt_devolucao IS NULL".format(str(cod_exemp))
                cur.execute(select_emp)
                emprestimo = cur.fetchall()  
                
                if emprestimo != []:
                    select_script = "SELECT * FROM reserva r WHERE r.cod_exemplar = {0} AND r.situacao_res = 'ATIVA' ORDER BY r.dt_reserva ASC".format(str(cod_exemp))
                    cur.execute(select_script)
                    queue = [today]
                    for tuple in cur.fetchall():
                        queue.append(tuple[4])
            
                    delay = max(queue) + timedelta(14)
                    insert_script = "INSERT INTO reserva (cod_matricula, cod_exemplar, dt_reserva, dt_prevista_emprestimo) VALUES ({0}, {1}, '{2}', '{3}')".format(cod_mat, cod_exemp, str(now), str(delay))
                    cur.execute(insert_script)

                    # print("Reserva Efetuada")
                    retorno = "Reserva Efetuada.\nA data prevista de Empréstimo é " + str(delay)
                    
                else:
                    # print("O exemplar está disponível.")
                    retorno = "O exemplar está disponível."
            
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    return retorno



# Devoluçao - Acusa uma reserva
def devolucao(cod_exemp, today = date.today(), now = datetime.now()):
    retorno = 0
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
            
            with con.cursor() as cur:
            
                select_emp = "SELECT * FROM emprestimo WHERE emprestimo.cod_exemplar = {0} AND emprestimo.dt_devolucao IS NULL".format(str(cod_exemp))
                cur.execute(select_emp)
                emprestimo = cur.fetchall() 
                
                if emprestimo != []:
                    cod_emp = emprestimo[0][0]
                
                    update_emp = "UPDATE emprestimo SET dt_devolucao = '{0}' WHERE cod_emprestimo = {1}".format(str(now), cod_emp)
                    cur.execute(update_emp)

                    update_exemp = "UPDATE exemplar SET cod_situacao = 1 WHERE cod_exemplar = {0}".format(cod_exemp)
                    cur.execute(update_exemp)
                    
                    select_res = "SELECT * FROM reserva r WHERE r.cod_exemplar = {0} AND r.situacao_res = 'ATIVA' ORDER BY r.dt_reserva ASC".format(str(cod_exemp))
                    cur.execute(select_res)
                    reservas = cur.fetchall()

                    if reservas != []:
                        cod_mat = reservas[0][1]
                        
                        select_mat = "SELECT * FROM matricula WHERE matricula.cod_matricula = {0}".format(str(cod_mat))           
                        cur.execute(select_mat)
                        matricula_reserva = cur.fetchall()
                        
                        # print("O exemplar está reservado por", matricula_reserva[0][3], "- e-mail: ", matricula_reserva[0][7], "- Codigo de Matricula: ", matricula_reserva[0][0])
                        retorno = "Devolução efetuada.\nO exemplar está reservado por " + str(matricula_reserva[0][3]) + "\ne-mail: " + str(matricula_reserva[0][7]) +"\nCodigo de Matricula: " + str(matricula_reserva[0][0])
                        
                    else:
                        # print("O exemplar não está reservado.")
                        retorno = "Devolução efetuada.\nO exemplar não está reservado."
                        
                else:
                    # print("O exemplar não está emprestado.")
                    retorno = "O exemplar não está emprestado."
                    
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    return retorno
