import psycopg2
import random
from datetime import datetime, date, timedelta

# Registro de Exemplar




# Registro de Matricula




# Realizar Emprestimo - Checa reservas para atualizar datas previstas e preeencher data de emprestimo)
def emprestimo(cod_mat, cod_exemp, today = date.today()):
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
                        
                        print("Empréstimo Efetuado")
                        
                    elif cod_mat == queue[0][1]:
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

                        print("Empréstimo Efetuado")

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
def reserva(cod_mat, cod_exemp, today = date.today(), now = datetime.now()):
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

                    print("Reserva Efetuada")
                    
                else:
                    print("O exemplar está disponível.")
            
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()




# Devoluçao - Acusa uma reserva
def devolucao(cod_exemp, today = date.today(), now = datetime.now()):
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
                
                    update_emp = "UPDATE emprestimo SET dt_devolucao = '{0}' WHERE cod_emprestimo = {1}".format(str(today), cod_emp)
                    cur.execute(update_emp)

                    update_exemp = "UPDATE exemplar SET cod_situacao = 1 WHERE cod_exemplar = {0}".format(cod_exemp)
                    cur.execute(update_exemp)

                    print("Devolução Efetuada")
                    
                    select_res = "SELECT * FROM reserva r WHERE r.cod_exemplar = {0} AND r.situacao_res = 'ATIVA' ORDER BY r.dt_reserva ASC".format(str(cod_exemp))
                    cur.execute(select_res)
                    reservas = cur.fetchall()

                    if reservas != []:
                        cod_mat = reservas[0][1]
                        
                        select_mat = "SELECT * FROM matricula WHERE matricula.cod_matricula = {0}".format(str(cod_mat))           
                        cur.execute(select_mat)
                        matricula_reserva = cur.fetchall()
                        
                        print("O livro está reservado por", matricula_reserva[0][3], "- e-mail: ", matricula_reserva[0][7], "- Codigo de Matricula: ", matricula_reserva[0][0])
                           
                    else:
                        print("O exemplar não está reservado.")
                        
                else:
                    print("O exemplar não está emprestado.")
                    
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()




# Data - Maior ocorrencias para datas mais recentes
def timeline_ocu(dt_ini, dt_fim):
    interv = dt_fim - dt_ini
    distr = {}
    # Dividir o intervalo em n intervalos menores, com uma formula baseada na data
    for i in range(interv.days + 1):
        data = dt_ini + timedelta(days = i)
        mes = data.month
        dia = data.weekday()
        # Não ter emprestimos em fim de semana e nos meses de janeiro, julho e dexembro
        if dia > 4:

        elif mes in [12, 1, 7]:
            
        else:
            prob = i/interv.days
            list_ocu = [0, 1]
            distr[data] = random.choices(list_ocu, weights = [1 - prob, prob])[0]

    # Distribuição aleatória com pesos para o numero de ocorrencias
    for data in distr:
        list_n_ocu = [1,2,3,4,5,6]
        distr[data] = distr[data] * (random.choices(list_n_ocu, weights = [0.03, 0.17, 0.38, 0.31, 0.09, 0.02])[0])
        
    return distr




def ocurrence(data): 
    con = None
    try:
        with psycopg2.connect(database = "BiblioTEC", user = "postgres", password = "123456", host = "localhost", port = "5432") as con:
            with con.cursor() as cur:
                # Escolher uma matricula
                select_mat = "SELECT cod_matricula FROM matricula"
                cur.execute(select_mat)
                mat = random.choice(cur.fetchall())

                # Escolher um exemplar
                select_exemp = "SELECT cod_exemplar, cod_situacao FROM exemplar WHERE cod_situacao NOT IN (3, 4) AND dt_aquisicao < '{0}'".format(data)
                cur.execute(select_exemp)
                exemp = random.choice(cur.fetchall())

                # Livros emprestados viram reservas
                if exemp[1] == 2:
                    reserva(mat[0], exemp[0], data, data)
                    
                else:
                    # Checar reservas do exemplar 
                    select_res = "SELECT cod_matricula FROM reserva WHERE cod_exemplar = {0} AND situacao_res = 'ATIVA' ORDER BY dt_reserva ASC".format(exemp[0])
                    cur.execute(select_res)
                    reservas = cur.fetchall()
                    
                    if reservas == []:
                        emprestimo(mat[0], exemp[0], data)
                    
                    else:
                        mat_res = reservas[0]
                        emprestimo(mat_res[0], exemp[0], data)
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()




def update_dev(data):
    con = None
    try:
        with psycopg2.connect(database = "BiblioTEC", user = "postgres", password = "123456", host = "localhost", port = "5432") as con:
            with con.cursor() as cur:
                select_emp = "SELECT emp.cod_exemplar, emp.dt_prevista_devolucao FROM emprestimo emp JOIN exemplar exemp ON (emp.cod_exemplar = exemp.cod_exemplar) WHERE dt_devolucao is NULL AND exemp.cod_situacao != 4"
                cur.execute(select_emp)
                emp_ativos = cur.fetchall()
                
                for emp in emp_ativos:
                    delta = (emp[1] - data).days
                    prob_dev = 0
                    
                    if delta < 0:
                        prob_dev = (delta + 14)/100
                    elif delta < 3:
                        prob_dev = 0.2
                    elif delta < 180:
                        prob_dev = 1/(2*delta)
                    else:
                        update_loss = "UPDATE exemplar SET cod_situacao = 4 WHERE cod_exemplar = {0}".format(emp[0])
                        cur.execute(update_loss)
                        
                    flag_dev = random.choices([0, 1], weights = [1 - prob_dev, prob_dev])
                    if flag_dev == [1]:
                        devolucao(emp[0], data, data)
                        
                        # Checar as reservas do exemplar
                        select_res = "SELECT cod_matricula FROM reserva WHERE cod_exemplar = {0} AND situacao_res = 'ATIVA' ORDER BY dt_reserva ASC".format(emp[0])
                        cur.execute(select_res)
                        res = cur.fetchall()
                        
                        if res != []:
                            prob_emp = 0.8
                            
                            flag_emp = random.choices([0, 1], weights = [1 - prob_emp, prob_emp])
                            if flag_emp == [1]:                                                           
                                emprestimo(res[0], emp[0], data)
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()




def update_res(data):
    con = None
    try:
        with psycopg2.connect(database = "BiblioTEC", user = "postgres", password = "123456", host = "localhost", port = "5432") as con:
            with con.cursor() as cur:
                select_res = "SELECT r.dt_prevista_emprestimo, r.cod_reserva FROM reserva r JOIN exemplar ex ON (r.cod_exemplar = ex.cod_exemplar) WHERE r.situacao_res = 'ATIVA' AND ex.cod_situacao = 1 ORDER BY r.dt_reserva ASC"
                cur.execute(select_res)
                res_ativas = cur.fetchall()

                for res in res_ativas:
                    atraso = (res[0] - data).days
                    
                    if atraso > 7:
                        cancel_res = "UPDATE reserva SET situacao_res = 'CANCELADA' WHERE cod_reserva = {0}".format(res[1])
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()




def pop_bibliotec(dt_ini, dt_fim):
    distr = timeline_ocu(dt_ini, dt_fim)
    
    for data in distr:
    
        #DEVOLUÇÕES
        update_dev(data)

        # RESERVAS ATRASADAS
        update_res(data)

        # OCORRENCIAS
        n = distr[data]
        while n > 0:
            n -= 1
            ocurrence(data)
