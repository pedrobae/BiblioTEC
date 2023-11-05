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
                res_trig = 0
        
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
                        res_trig = 1
                else:
                    print("O exemplar está emprestado, realize a devolução primeiro.")
        
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    return res_trig

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
                    emp_trig = 0
                    
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
                            emp_trig = matricula_reserva[0][0]
                               
                        else:
                            print("O exemplar não está reservado.")
                            
                    else:
                        print("O exemplar não está emprestado.")
                        
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    return emp_trig


# Popula emprestimos e reservas
def pop_bibliotec(dt_ini, dt_fim):
    # Data - Maior ocorrencias para datas mais recentes
    interv = dt_fim - dt_ini
    distr = {}
    # Dividir o intervalo em n intervalos menores, com uma formula baseada na data
    for i in range(interv.days + 1):
        data = dt_ini + timedelta(days = i)
        mes = data.month
        dia = data.weekday()
        # Não ter emprestimos em fim de semana e nos meses de janeiro, julho e dexembro
        if dia > 4:
            distr[data] = 0

        elif mes in [12, 1, 7]:
            distr[data] = 0
            
        else:
            prob = i/interv.days
            list_ocu = [0, 1]
            distr[data] = random.choices(list_ocu, weights = [1 - prob, prob])[0]
          
    # Distribuição aleatória com pesos para o numero de ocorrencias
    for data in distr:
        list_n_ocu = [1,2,3,4,5,6]
        distr[data] = distr[data] * (random.choices(list_n_ocu, weights = [0.03, 0.17, 0.38, 0.31, 0.09, 0.02])[0])

    # Gerar emprestimos
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:

            with con.cursor() as cur:
            
                for data in distr:
                    n = distr[data]
                # Após ciclos checar devoluções e reservas não efetuadas (7 dias)
                    # SELECIONAR os emprestimos ativos 
                    select_emp = "SELECT exemp.cod_exemplar, emp.dt_prevista_devolucao FROM emprestimo emp JOIN exemplar exemp ON (emp.cod_exemplar = exemp.cod_exemplar) WHERE dt_devolucao is NULL AND exemp.cod_situacao != 4"
                    cur.execute(select_emp)
                    emp_ativo = cur.fetchall()

                    # Gerar devoluções
                        # Devoluções atrasadas, perda de livros
                    for emp in emp_ativo:
                        delta = (data - emp[1]).days
                        if delta > 180:
                            # Talvez não funcione
                            update_loss = "UPDATE exemplar SET cod_situacao = 4 WHERE cod_exemplar = {0}".format(emp[0])
                            cur.execute(update_loss)
                        elif delta < 0:
                            prob = (delta + 14)/150
                        elif delta == 0:
                            prob = 0.4
                        else:
                            prob = 0.3/delta
                                                
                        flag = random.choices([0, 1], weights = [1 - prob, prob])
                        if flag == [1]:
                            emp_trig = devolucao(emp[0], data, data)
                            if emp_trig != 0:
                                prob = 0.5
                                flag = random.choices([0, 1], weights = [1 - prob, prob])
                                if flag == [1]:                                                           
                                    emprestimo(emp_trig, emp[0], data)
                                

                    # Cancelar reservas atrasadas
                    select_res = "SELECT cod_exemplar, dt_prevista_emprestimo, cod_reserva FROM reserva WHERE situacao_res = 'ATIVA'"
                    cur.execute(select_res)
                    res_ativa = cur.fetchall()
                    
                    for res in res_ativa:
                        emp_atrasado = False
                        for emp in emp_ativo:
                            if res[0] == emp[0]:
                                emp_atrasado = True
                                
                        atraso = (data - res[1]).days
                        if not emp_atrasado and atraso > 7:
                            cancel_res = "UPDATE reserva SET situacao_res = 'INATIVA' WHERE cod_reserva = {0}".format(res[2])
                        
                    while n > 0:
                        # Escolher uma matrícula
                        select_mat = "SELECT cod_matricula FROM matricula"
                        cur.execute(select_mat)
                        mat = random.choice(cur.fetchall())
                            # Perfís?
                            
                        # Escolher um exemplar no acervo
                            # Checar a data de aquisição do livro
                            # Exceto livros perdidos ou em manutenção
                        select_exemp = "SELECT cod_exemplar, cod_situacao FROM exemplar WHERE cod_situacao NOT IN (3, 4) AND dt_aquisicao < '{0}'".format(data)
                        cur.execute(select_exemp)
                        exemp = random.choice(cur.fetchall())
                        
                        # Livros emprestados viram reservas
                        if exemp[1] == 2:
                            reserva(mat[0], exemp[0], data, data)
                        # Efetuar emprestimo no banco
                        else:
                            res_trig = emprestimo(mat[0], exemp[0], data)
                            # Caso o livro esteja reservado -> tem a chance de efetuar o emprestimo correto
                            if res_trig == 1:
                                prob = 0.9
                                flag = random.choices([0, 1], weights = [1 - prob, prob])
                                if flag == [1]:
                                    select_res = "SELECT cod_matricula FROM reserva r WHERE r.cod_exemplar = {0} AND r.situacao_res = 'ATIVA' ORDER BY r.dt_reserva ASC".format(str(exemp[0]))
                                    cur.execute(select_res)
                                    mat_res = cur.fetchall()[0][0]
                                                                    
                                    emprestimo(mat_res, exemp[0], data)
                        n -= 1
       
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

'''
emprestimo(40101, 1)
emprestimo(40102, 1)
emprestimo(40102, 2)
reserva(40102, 1)
reserva(40103, 1)
reserva(40104, 1)
devolucao(1)
emprestimo(40103, 1)
emprestimo(40102, 1)
'''
