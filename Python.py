import psycopg2
from datetime import datetime
from datetime import date
from datetime import timedelta


# Registro de Exemplar


# Registro de Matricula


# Realizar Emprestimo - TO DO -> checar reservas para atualizar datas previstas e preeencher data de emprestimo)
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


# Realizar Reserva - Definir a ordem para calcular o data de emprestimo prevista
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


# Devoluçao - Acusa uma reserva
    import psycopg2
    from datetime import datetime
    from datetime import date
    from datetime import timedelta
    
    def devolucao(cod_exemp):
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
            
            select_emp = ('SELECT * FROM emprestimo WHERE emprestimo.cod_exemplar = (%s) AND emprestimo.dt_devolucao IS NULL')
            select_emp_values = (str(cod_exemp))
            cur.execute(select_emp, select_emp_values)
            
            emprestimo = cur.fetchall()        
            if emprestimo != []:
                cod_emp = emprestimo[0][0]
            
                update_emp = ('UPDATE emprestimo SET dt_devolucao = %s WHERE cod_emprestimo = %s')
                update_emp_values = (str(now), cod_emp)
                cur.execute(update_emp, update_emp_values)
                
                select_res = ('SELECT * FROM reserva WHERE reserva.cod_exemplar = %s AND reserva.dt_emprestimo IS NULL')
                select_res_values = (str(cod_exemp))
                cur.execute(select_res, select_res_values)
                
                reservas = cur.fetchall()
                if reservas != []:
                    cod_mat = reservas[0][1]
                    
                    select_mat_values = (str(cod_mat))
                    select_mat = ('SELECT * FROM matricula WHERE matricula.cod_matricula = {0}'.format(select_mat_values))            
                    cur.execute(select_mat)
                    
                    matricula_reserva = cur.fetchall()
                    print('O livro esta reservado por', matricula_reserva[3], 'e-mail', matricula_reserva[7])
                else:
                    print('O livro não esta emprestado')
            else:
                print('O livro não esta emprestado')
                
            con.commit()
        except Exception as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
            if con is not None:
                con.close()

#Exemplo de Conexão
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
