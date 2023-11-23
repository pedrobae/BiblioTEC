import psycopg2
import datetime

# Registro de Exemplar
def registra_exemplar (isbn, dt_aquisicao, cod_estante, cod_situacao, estado_exempl):
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
                select_exe = "SELECT isbn FROM exemplar"
                cur.execute(select_exe)
                lista_exe = []
                for value in cur.fetchall():
                    lista_exe += value

                # Checa se o cod_autor existe na lista
                if isbn in lista_exe:
                    retorno = 'O livro já está cadastrado'
                else:
                    # Realiza o cadastro
                    insert_exe = "INSERT INTO exemplar VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')".format(isbn, dt_aquisicao, cod_estante, cod_situacao, estado_exempl)
                    cur.execute(insert_exe)
                    retorno = 'Cadastro Efetuado'

    except Exception as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    if retorno:
        return retorno
    


# Registro de Matricula




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
                    if subtitulo:
                        subtitulo = "'{0}'".format(subtitulo)
                    if local_publ:
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

if __name__ == "__main__":
    registra_livro(6589132683, 'O Caminho dos Reis', '2010-8-31', 'Trama')
