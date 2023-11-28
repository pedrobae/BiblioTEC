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

                isbn = int(isbn)
                # Checa se o ISBN está cadastrado
                if isbn in lista_isbn:
                    # Seleciona os exemplares
                    select_exemp = "SELECT cod_exemplar FROM exemplar"
                    cur.execute(select_exemp)
                    lista_exemp = []
                    for value in cur.fetchall():
                        lista_exemp += value

                    # Checa se o exemplar esta cadastrados
                    cod_exemplar = int(cod_exemplar)
                    if cod_exemplar in lista_exemp:
                        retorno = "O código de exemplar já está cadastrado"
                    else:
                        if cod_estante != '':
                            cod_estante = int(cod_estante)

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
def registra_matricula (cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, sexo, dt_nscm = '', email_matricula = '', endereco_matricula = '', CPF = ''):
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

                cod_matricula = int(cod_matricula)
                # Checa se o cod_matricula existe na lista
                if cod_matricula in lista_mat:
                    retorno = 'O Código de Matrícula já está cadastrado'
                else:
                    # Realiza o cadastro
                    dt_matricula = str(datetime.date.today())

                    if dt_nscm != '':
                        dt_nscm = "'{0}'".format(dt_nscm)
                    else:
                        dt_nscm = 'NULL'

                    if email_matricula != '':
                        email_matricula = "'{0}'".format(email_matricula)
                    else:
                        email_matricula = 'NULL'

                    if endereco_matricula != '':
                        endereco_matricula = "'{0}'".format(endereco_matricula)
                    else:
                        endereco_matricula = 'NULL'

                    if cod_tipo_matricula != '':
                        cod_tipo_matricula = int(cod_tipo_matricula)
                    if cod_instituicao != '':
                        cod_instituicao = int(cod_instituicao)
                    if CPF != '':
                        CPF = int(CPF)

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
def registra_livro(isbn, titulo, dt_publ, editora, edicao = '', local_publ = '', subtitulo = ''):
    con = None
    retorno = None
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

                isbn = int(isbn)
                if isbn in lista_livro:
                    retorno = 'O Código ISBN já está cadastrado'
                else:
                    if subtitulo != '':
                        subtitulo = "'{0}'".format(subtitulo)
                    else:
                        subtitulo = 'NULL'

                    if local_publ != '':
                        local_publ = "'{0}'".format(local_publ)
                    else:
                        local_publ = 'NULL'

                    if edicao != '':
                        edicao = int(edicao)
                    
                    insert_livro = '''
                        INSERT INTO livro (isbn, titulo, subtitulo, dt_publ, editora, edicao, local_publ)
                        VALUES ({0}, '{1}', {2}, '{3}', '{4}', {5}, {6})'''.format(isbn, titulo, subtitulo, dt_publ, editora, edicao, local_publ)

                    cur.execute(insert_livro)
                    retorno = 'Cadastro Efetuado'

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()

    if retorno:
        return retorno



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
                cod_autor = int(cod_autor)
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