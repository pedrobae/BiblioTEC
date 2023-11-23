import psycopg2
import datetime

# Registro de Exemplar




# Registro de Matricula
def registro_matricula (cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, dt_matricula, sexo, dt_nscm, email_matricula, endereco_matricula, CPF, dt_termino):
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
                select_mat = "SELECT cod_matricula FROM exemplar"
                cur.execute(select_mat)
                lista_mat = []
                for value in cur.fetchall():
                    lista_mat += value

                # Checa se o cod_matricula existe na lista
                if cod_matricula in lista_mat:
                    retorno = 'O Código de Matrícula já está cadastrado'
                else:
                    # Realiza o cadastro
                    insert_mat = "INSERT INTO matricula VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}')".format(cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, dt_matricula, sexo, dt_nscm, email_matricula, endereco_matricula, CPF, dt_termino)
                    cur.execute(insert_mat)
                    retorno = 'Matrícula Efetuado'

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