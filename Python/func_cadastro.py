import psycopg2
import datetime

# Registro de Exemplar
def registra_exemplar(cod_exemplar, isbn, cod_estante, estado_exempl):
    retorno = None
    # Conecta com o banco
    con = None
    try:
        with psycopg2.connect(
                        database="BiblioTEC",
                        user="postgres",
                        password="123456",
                        host="localhost",
                        port="5432") as con:

            with con.cursor() as cur:
                # Seleciona os ISBNs existentes e coloca em uma lista
                select_isbn = "SELECT isbn FROM livro"
                cur.execute(select_isbn)
                lista_isbn = []
                for value in cur.fetchall():
                    lista_isbn += value

                # Checa se o ISBN está cadastrado
                if isbn in lista_isbn:
                    # Seleciona os exemplares
                    select_exemp = "SELECT cod_exemplar FROM exemplar"
                    cur.execute(select_exemp)
                    lista_exemp = []
                    for value in cur.fetchall():
                        lista_exemp += value

                    # Checa se o exemplar esta cadastrados
                    if cod_exemplar in lista_exemp:
                        retorno = "O código de matricula já está cadastrado"
                    else:
                        dt_aquisicao = datetime.date.today()
                        insert_exe = '''INSERT INTO exemplar VALUES (DEFAULT, {0}, '{1}', '{2}', 1, '{3}')'''.format(isbn, str(dt_aquisicao), cod_estante, estado_exempl)
                        cur.execute(insert_exe)
                        retorno = 'Cadastro do exemplar efetuado.'
                else:
                    retorno = 'Necessário cadastrar o livro'

    except Exception as error:
        print(error)
        retorno = 'Erro ao cadastrar exemplar.'
    finally:
        if con is not None:
            con.close()
    return retorno



# Registro de Matricula
def registra_matricula (cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, sexo, dt_nscm = 'NULL', email_matricula = 'NULL', endereco_matricula = 'NULL', CPF = 'NULL'):
    retorno = None
    # Conecta com o banco
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
        
            with con.cursor() as cur:
                # Seleciona os codigos de matrícula existentes e coloca em uma lista
                select_mat = "SELECT cod_matricula FROM matricula"
                cur.execute(select_mat)
                lista_mat = []
                for value in cur.fetchall():
                    lista_mat += value

                # Checa se o cod_matricula existe na lista
                if cod_matricula in lista_mat:
                    retorno = 'O Código de Matrícula já está cadastrado'
                else:
                    # Realiza o cadastro
                    dt_matricula = str(datetime.date.today())

                    if dt_nscm != 'NULL':
                        dt_nscm = "'{0}'".format(dt_nscm)

                    if email_matricula != 'NULL':
                        email_matricula = "'{0}'".format(email_matricula)

                    if endereco_matricula != 'NULL':
                        endereco_matricula = "'{0}'".format(endereco_matricula)

                    insert_mat = '''INSERT INTO matricula (cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, dt_matricula, sexo, dt_nscm, email_matricula, endereco_matricula, CPF) 
                                    VALUES ({0}, {1}, {2}, '{3}', '{4}', '{5}', {6}, {7}, {8}, {9})'''.format(cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, dt_matricula, sexo, dt_nscm, email_matricula, endereco_matricula, CPF)
                    cur.execute(insert_mat)
                    retorno = 'Matrícula Efetuada'

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    if retorno:
        return retorno



# Registro de Livro
def registra_livro(isbn, titulo, dt_publ, editora, edicao = 'NULL', local_publ = 'NULL', subtitulo = 'NULL'):
    con = None
    retorne = None
    try:
        with psycopg2.connect(
            database="BiblioTEC",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        ) as con:
            with con.cursor() as cur:

                select_livro = "SELECT isbn FROM livro"
                cur.execute(select_livro)
                lista_livro = []
                for value in cur.fetchall():
                    lista_livro += value

                if isbn in lista_livro:
                    retorne = 'O Código ISBN já está cadastrado'
                else:
                    if subtitulo != 'NULL':
                        subtitulo = "'{0}'".format(subtitulo)

                    if local_publ != 'NULL':
                        local_publ = "'{0}'".format(local_publ)
                    
                    insert_livro = '''
                        INSERT INTO livro (isbn, titulo, subtitulo, dt_publ, editora, edicao, local_publ)
                        VALUES ({0}, '{1}', {2}, '{3}', '{4}', {5}, {6})'''.format(isbn, titulo, subtitulo, dt_publ, editora, edicao, local_publ)

                    cur.execute(insert_livro)
                    retorne = 'Cadastro Efetuado'

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()

    if retorne:
        return retorne



# Registro de Autor
def registra_autor (cod_autor, nome_autor, pais_autor):
    retorno = None
    # Conecta com o banco
    con = None
    try:
        with psycopg2.connect(
                        database = "BiblioTEC", 
                        user = "postgres", 
                        password = "123456", 
                        host = "localhost",
                        port = "5432") as con:
        
            with con.cursor() as cur:
                # Seleciona os codigos de autor existentes e coloca em uma lista
                select_aut = "SELECT cod_autor FROM autor"
                cur.execute(select_aut)
                lista_aut = []
                for value in cur.fetchall():
                    lista_aut += value

                # Checa se o cod_autor existe na lista
                if cod_autor in lista_aut:
                    retorno = 'O Código de Autor ja está cadastrado'
                else:
                    # Realiza o cadastro
                    insert_aut = "INSERT INTO autor VALUES ({0}, '{1}', '{2}')".format(cod_autor, nome_autor, pais_autor)
                    cur.execute(insert_aut)
                    retorno = 'Cadastro Efetuado'

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    if retorno:
        return retorno



'''
EXEMPLO DE CONEXÃO
con = None
try:
    with psycopg2.connect(
                    database = "BiblioTEC", 
                    user = "postgres", 
                    password = "123456", 
                    host = "localhost",
                    port = "5432") as con:
    
        with con.cursor() as cur:

            # Código aqui            

except Exception as error:
    print(error)
finally:
    if con is not None:
        con.close()
'''