import psycopg2

# Selecionar Acervo Disponível
def acervo_disp():
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
            
            with con.cursor() as cur:

                select_acerv =  ''' SELECT e.cod_exemplar, l.titulo, e.dt_aquisicao 
                                        FROM exemplar e 
                                            JOIN livro l ON (e.ISBN = l.ISBN) 
                                        WHERE e.cod_situacao = 1 
                                            ORDER BY l.titulo'''
                cur.execute(select_acerv)

                acervo = cur.fetchall()

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()

    return acervo



# Selecionar Acervo Emprestado
def acervo_empr():
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
        
            with con.cursor() as cur:

                select_acerv =  ''' SELECT e.cod_exemplar, l.titulo, m.nome_matricula AS "Matricula do Emprestimo", emp.dt_prevista_devolucao
                                        FROM exemplar e 
                                            JOIN livro l            ON (e.ISBN = l.ISBN)
                                            JOIN emprestimo emp     ON (e.cod_exemplar = emp.cod_exemplar)
                                            JOIN matricula m        ON (emp.cod_matricula = m.cod_matricula)
                                        WHERE e.cod_situacao = 2
                                            AND dt_devolucao IS NULL 
                                            ORDER BY l.titulo'''
                cur.execute(select_acerv)

                acervo = cur.fetchall()

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()

    return acervo



# Selecionar Acervo Perdido
def acervo_perd():
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
            
            with con.cursor() as cur:

                select_acerv =  ''' SELECT e.cod_exemplar, l.titulo, m.nome_matricula AS "Matricula do Ultimo Empréstimo"
                                        FROM exemplar e 
                                            JOIN livro l            ON (e.ISBN = l.ISBN)
                                            JOIN emprestimo emp     ON (e.cod_exemplar = emp.cod_exemplar)
                                            JOIN matricula m        ON (emp.cod_matricula = m.cod_matricula)
                                        WHERE e.cod_situacao = 4
                                            AND dt_devolucao IS NULL 
                                            ORDER BY l.titulo'''
                cur.execute(select_acerv)

                acervo = cur.fetchall()

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()

    return acervo



# Selecionar Acervo em Manutenção
def acervo_manu():
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
            
            with con.cursor() as cur:

                select_acerv =  ''' SELECT e.cod_exemplar, l.titulo
                                        FROM exemplar e 
                                            JOIN livro l    ON (e.ISBN = l.ISBN)
                                        WHERE e.cod_situacao = 3 
                                        ORDER BY l.titulo'''
                
                cur.execute(select_acerv)

                acervo = cur.fetchall()

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()

    return acervo
