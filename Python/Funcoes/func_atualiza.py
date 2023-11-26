import psycopg2

# Atualizar Livro
def atualiza_livro(ISBN, titulo = None, subtitulo = None, dt_publ = None, editora = None, edicao = None, local_publ = None):
    retorno = None
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
            
            with con.cursor() as cur:
                
                select_ISBN = "SELECT ISBN FROM livro"
                cur.execute(select_ISBN)
                lista_ISBN = []
                for value in cur.fetchall():
                    lista_ISBN += value
                    
                if ISBN in lista_ISBN:
                    # Atualizo os valores passados
                    if titulo:
                        update_tit = "UPDATE livro SET titulo = '{0}' WHERE ISBN = {1}".format(titulo, ISBN)
                        cur.execute(update_tit)
                        retorno = "Título atualizado com sucesso."
                    if subtitulo:
                        update_subt = "UPDATE livro SET subtitulo = '{0}' WHERE ISBN = {1}".format(subtitulo, ISBN)
                        cur.execute(update_subt)
                        retorno = "Subtítulo atualizado com sucesso."
                    if dt_publ:
                        update_dtp = "UPDATE livro SET dt_publ = '{0}' WHERE ISBN = {1}".format(dt_publ, ISBN)
                        cur.execute(update_dtp)
                        retorno = "Data de publicação atualizada com sucesso."
                    if editora:
                        update_edit = "UPDATE livro SET editora = {0} WHERE ISBN = {1}".format(editora, ISBN)
                        cur.execute(update_edit)
                        retorno = "Editora atualizada com sucesso."
                    if edicao:
                        update_edic = "UPDATE livro SET edicao = {0} WHERE ISBN = {1}".format(edicao, ISBN)
                        cur.execute(update_edic)
                        retorno = "Edição atualizada com sucesso."
                    if local_publ:
                        update_local = "UPDATE livro SET local_publ = '{0}' WHERE ISBN = {1}".format(local_publ, ISBN)
                        cur.execute(update_local)
                        retorno = "Local de publicação atualizado com sucesso."
                    
                else:
                    retorno = "O ISBN não está cadastrado, por favor cadastre o livro."
                    
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            
    return retorno


# Atualizar Exemplar
def atualiza_exemplar(cod_exemplar, cod_estante = None, cod_situacao = None, estado_exemplar = None):
    retorno = None
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
            
            with con.cursor() as cur:
                
                select_cod_exemplar = "SELECT cod_exemplar FROM exemplar"
                cur.execute(select_cod_exemplar)
                lista_exemplar = []
                for value in cur.fetchall():
                    lista_exemplar += value
                    
                if cod_exemplar in lista_exemplar:
                    # Atualizo os valores passados
                    if cod_estante:
                        update_cod_estante = "UPDATE exemplar SET cod_estante = {0} WHERE cod_exemplar = {1}".format(cod_estante, cod_exemplar)
                        cur.execute(update_cod_estante)
                        retorno = "Estante atualizada com sucesso."
                    if cod_situacao:
                        update_cod_situacao = "UPDATE exemplar SET cod_situacao = {0} WHERE cod_exemplar = {1}".format(cod_situacao, cod_exemplar)
                        cur.execute(update_cod_situacao)
                        retorno = "Situação do exemplar atualizada com sucesso."
                    if estado_exemplar:
                        update_estado_exemplar = "UPDATE exemplar SET estado_exemplar = '{0}' WHERE cod_exemplar = {1}".format(estado_exemplar, cod_exemplar)
                        cur.execute(update_estado_exemplar)
                        retorno = "Estado do exemplar atualizado com sucesso."
                else:
                    retorno = "O código do exemplar não está cadastrado, por favor cadastre o exemplar."
        
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            
    return retorno



# Atualizar Matricula
def atualiza_matricula(cod_matricula, nome_matricula = None, sexo = None, dt_nscm = None, email_matricula = None, CPF = None, dt_termino = None):
    retorno = None
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
            
            with con.cursor() as cur:
                
                select_cod_matricula = "SELECT cod_matricula FROM matricula"
                cur.execute(select_cod_matricula)
                lista_cod_matricula = []
                for value in cur.fetchall():
                    lista_cod_matricula += value
                    
                    
                if cod_matricula in lista_cod_matricula:
                    # Atualizo os valores passados
                    if nome_matricula:
                        update_nome_matricula = "UPDATE matricula SET nome_matricula = '{0}' WHERE cod_matricula = {1}".format(nome_matricula, cod_matricula)
                        cur.execute(update_nome_matricula)
                        retorno = "Nome atualizado com sucesso."
                    if sexo:
                        update_sexo = "UPDATE matricula SET sexo = '{0}' WHERE cod_matricula = {1}".format(sexo, cod_matricula)
                        cur.execute(update_sexo)
                        retorno = "Gênero atualizado com sucesso."
                    if dt_nscm:
                        update_dtn = "UPDATE matricula SET dt_nscm = '{0}' WHERE cod_matricula = {1}".format(dt_nscm, cod_matricula)
                        cur.execute(update_dtn)
                        retorno = "Data de nascimento atualizada com sucesso."
                    if email_matricula:
                        update_email = "UPDATE matricula SET email_matricula = '{0}' WHERE cod_matricula = {1}".format(email_matricula, cod_matricula)
                        cur.execute(update_email)
                        retorno = "E-mail atualizado com sucesso."
                    if CPF:
                        update_cpf = "UPDATE matricula SET CPF = {0} WHERE cod_matricula = {1}".format(CPF, cod_matricula)
                        cur.execute(update_cpf)
                        retorno = "CPF atualizado com sucesso."
                    if dt_termino:
                        update_dtt = "UPDATE matricula SET dt_termino = '{0}' WHERE cod_matricula = {1}".format(dt_termino, cod_matricula)
                        cur.execute(update_dtt)
                        retorno = "Data de término atualizada com sucesso."
                    
                else:
                    retorno = "O código de metrícula não está cadastrado, por favor cadastre a matrícula."
                    
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            
    return retorno


# Atualizar Autor
def atualiza_autor(cod_autor, nome_autor = None, pais_autor = None):
    retorno = None
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
            
            with con.cursor() as cur:
                
                select_cod_autor = "SELECT cod_autor FROM autor"
                cur.execute(select_cod_autor)
                lista_autor = []
                for value in cur.fetchall():
                    lista_autor += value
                    
                if cod_autor in lista_autor:
                    # Atualizo os valores passados
                    if nome_autor:
                        update_nome_autor = "UPDATE autor SET nome_autor = '{0}' WHERE cod_autor = {1}".format(nome_autor, cod_autor)
                        cur.execute(update_nome_autor)
                        retorno = "Nome do autor atualizado com sucesso."
                    if pais_autor:
                        update_pais_autor = "UPDATE autor SET pais_autor = '{0}' WHERE cod_autor = {1}".format(nome_autor, cod_autor)
                        cur.execute(update_pais_autor)
                        retorno = "País de origem do autor atualizado com sucesso."

                    
                else:
                    retorno = "O código do autor não está cadastrado, por favor cadastre o autor."
        
    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            
    return retorno