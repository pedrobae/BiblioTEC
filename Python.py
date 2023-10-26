import psycopg2

con = psycopg2.connect(
    database = "BiblioTEC", 
    user = "postgres", 
    password = "123456", 
    host = "localhost",
    port = "5432"
    )


# Registro de Exemplar

# Registro de Matricula

# Realizar Emprestimo

# Realizar Reserva (definir a ordem para calcular o data de emprestimo prevista)

# Transformar Reserva em Emprestimo


con.close()
