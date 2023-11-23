import psycopg2
import datetime

# Registro de Exemplar
'''
def nome_da_função (coluna1, coluna2, ..., colunaN):
    conecta no banco
        realiza o insert
    desconecta do banco
'''
# Registro de Matricula




# Registro de Livro
import psycopg2

def registro_livro():
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
                insert_livro = '''
                    INSERT INTO livros (isbn, titulo, subtitulo, dt_publ, editora, edicao, local_publ)
                    VALUES (({0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(isbn, titulo, subtitulo, dt_publ, editora, edicao, local_publ))'''

                cur.execute(insert_livro)

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
    registra_autor(30, 'Brandon Sanderson', 'Estados Unidos')
