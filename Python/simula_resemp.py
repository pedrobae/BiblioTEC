import psycopg2
import random
from datetime import timedelta, date, datetime
from biblioteca import reserva, emprestimo, devolucao

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
                    retorno = reserva(mat[0], exemp[0], data, data)
                    if retorno == 1:
                        resultado = "Reserva Efetuada"
                    elif retorno == 2:
                        resultado = "O exemplar está disponível."
                    print(resultado)
                    
                    
                else:
                    # Checar reservas do exemplar 
                    select_res = "SELECT cod_matricula FROM reserva WHERE cod_exemplar = {0} AND situacao_res = 'ATIVA' ORDER BY dt_reserva ASC".format(exemp[0])
                    cur.execute(select_res)
                    reservas = cur.fetchall()
                    
                    if reservas == []:
                        retorno = emprestimo(mat[0], exemp[0], data)
                        if retorno == 1:
                            resultado = "Empréstimo Efetuado"
                        elif retorno == 2:
                            resultado = "O exemplar está reservado."
                        elif retorno == 3:
                            resultado = "O exemplar está emprestado, realize a devolução primeiro."
                        print(resultado)
                    
                    else:
                        mat_res = reservas[0]
                        retorno = emprestimo(mat_res[0], exemp[0], data)
                        if retorno == 1:
                            resultado = "Empréstimo Efetuado"
                        elif retorno == 2:
                            resultado = "O exemplar está reservado."
                        elif retorno == 3:
                            resultado = "O exemplar está emprestado, realize a devolução primeiro."
                        print(resultado)
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
                        prob_dev = 1/delta
                    else:
                        update_loss = "UPDATE exemplar SET cod_situacao = 4 WHERE cod_exemplar = {0}".format(emp[0])
                        cur.execute(update_loss)
                        
                    flag_dev = random.choices([0, 1], weights = [1 - prob_dev, prob_dev])
                    if flag_dev == [1]:
                        retorno = devolucao(emp[0], data, data)
                        if retorno == 1:
                            resultado = "Devolução Efetuada"
                        elif retorno == 2:
                            resultado = "O livro está reservado"
                        elif retorno == 3:
                            resultado = "O exemplar não está reservado."
                        elif retorno == 4:
                            resultado = "O exemplar não está emprestado."
                        print(resultado)

                        # Checar as reservas do exemplar
                        select_res = "SELECT cod_matricula FROM reserva WHERE cod_exemplar = {0} AND situacao_res = 'ATIVA' ORDER BY dt_reserva ASC".format(emp[0])
                        cur.execute(select_res)
                        res = cur.fetchall()
                        
                        if res != []:
                            prob_emp = 0.8
                            flag_emp = random.choices([0, 1], weights = [1 - prob_emp, prob_emp])
                            if flag_emp == [1]:                                                           
                                emprestimo(res[0], emp[0], data)
                                if retorno == 1:
                                    resultado = "Empréstimo Efetuado"
                                elif retorno == 2:
                                    resultado = "O exemplar está reservado."
                                elif retorno == 3:
                                    resultado = "O exemplar está emprestado, realize a devolução primeiro."
                                print(resultado)
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
