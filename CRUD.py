#alterar para o caso do pi
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys

arquivo = 'agenda.sqlite'
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName(arquivo)
if not con.open():
  print("Erro na base de dados: %s" % con.lastError().databaseText())
  sys.exit()
else:
  createTableQuery = QSqlQuery()
  createTableQuery.exec('CREATE TABLE IF NOT EXISTS agenda (\
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,\
            nome VARCHAR(40) NOT NULL,\
            email VARCHAR(40) NOT NULL,\
            celular VARCHAR(20) NOT NULL)')
  createTableQuery.finish()


def exibir_menu():
  print('''

  Escolha uma opção:

  1. Cadastrar uma pessoa
  2. Listar pessoas cadastradas
  3. Procurar dados de uma pessoa
  4. Remover
  5. Alterar
  6. Sair

  ''')


def matricula():
  cod_matricula = int(input ('código de matrícula: '))#int
  cod_tipo_matricula = int(input ('código tipo de matrícula: '))#int
  cod_instituicao = int(input ('código da instituição: '))#int
  nome_matricula = input('Nome Completo: ')  # string
  dt_matricula #current date
  sexo= input ('Sexo: ')
  dt_nascimento = ('Data de Nascimento: ')
  email_matricula = input('E-mail: ')  # string
  endereco_matricula = input('Endereço: ')  # string
  CPF = input ('CPF: ')#string
  dt_termino #não é necessário
  
  insertDataQuery = QSqlQuery()
  insertDataQuery.prepare('INSERT INTO agenda (nome, email, celular) VALUES (?, ?, ?)')
  insertDataQuery.addBindValue(nome) # dado relativo ao primeiro espaço reservado
  insertDataQuery.addBindValue(email) # dado relativo ao segundo espaço reservado
  insertDataQuery.addBindValue(celular) # dado relativo ao terceiro espaço reservado
  insertDataQuery.exec() # execute a query
  insertDataQuery.finish() # inative a query


def listar():
  query = QSqlQuery()
  query.exec("SELECT  cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, sexo, dt_nascimento, email_matricula, endereco_matricula, CPF FROM matricula")
  # Índices com nomes para melhorar a legibilidade
  cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, sexo, dt_nascimento, email_matricula, endereco_matricula, CPF = range(3)  # 0, 1 e 2
  cont = 0

  print(' NOME          | E-MAIL                        | CELULAR')
  print('-'*74)
  while query.next():
    print(f'{query.value(nome):15}| {query.value(email):30}| {query.value(celular):25}')
    cont += 1  # isso aqui é uma abreviação de cont = cont + 1
  query.finish()
  print('\nQuantidade de registros: ', cont, '\n')


def buscar():
  procurado = input('Entre com o nome a procurar: ')
  query = QSqlQuery()
  query.prepare("SELECT nome, email, celular FROM agenda WHERE nome LIKE ?")
  query.addBindValue('%'+procurado+'%')
  query.exec()
  # Índices com nomes para melhorar a legibilidade
  nome, email, celular = range(3)  # 0, 1 e 2
  cont = 0

  print(' NOME          | E-MAIL                        | CELULAR')
  print('-'*74)
  while query.next():
    print(f'{query.value(nome):15}| {query.value(email):30}| {query.value(celular):25}')
    cont += 1  # isso aqui é uma abreviação de cont = cont + 1
  query.finish()
  print('\nQuantidade de registros: ', cont, '\n')


def remover():  # aqui você completa.... :-)
  pass


def alterar():  # aqui você completa.... :-)
  pass


def main():
  opcao = '0'
  while opcao!='6':
    exibir_menu()
    opcao = input('Entre com a opção desejada: ')
    print()
    if opcao == '1': cadastrar()
    elif opcao == '2': listar()
    elif opcao == '3': buscar()
    elif opcao == '4': remover()
    elif opcao == '5': alterar()
    elif opcao == '6':
      con.close()
      QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
    else:
      print('Opção inválida')


main()