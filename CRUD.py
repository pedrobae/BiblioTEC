#alterar para o caso do pi e para o postgresql
import PySimpleGUI as sg
import psycopg2

def limpar():
    window['-ID-'].update('')
    window['-NOME-'].update('')
    window['-EMAIL-'].update('')
    window['-CEL-'].update('')

def atualiza():
    if len(lista) == 0:
        limpar()
    else:
        window['-ID-'].update( lista[indice][0] )
        window['-NOME-'].update( lista[indice][1] )
        window['-EMAIL-'].update( lista[indice][2] )
        window['-CEL-'].update( lista[indice][3] )

def todos():
    global indice
    global lista
    resposta = []
    with con:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM matricula;")
            resposta = cursor.fetchall()
    lista.clear()
    for i in range(len(resposta)):
        lista.append( list(resposta[i]) )

    sg.popup('Quantidade de registros: ' + str(len(resposta)))
    indice = 0
    atualiza()

# Inicialização BD
con = psycopg2.connect(host="localhost", database="BiblioTEC", user="postgres", password="123456")
with con:
    with con.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS matricula (
            
  	(cod_matricula 			INTEGER 		PRIMARY KEY, 
	cod_tipo_matricula 		SMALLSERIAL 	NOT NULL 	REFERENCES tipo_matricula(cod_tipo_matricula),  
	cod_instituicao 		SMALLSERIAL  	REFERENCES instituicao(cod_instituicao), 
	nome_matricula 			VARCHAR(100) 	NOT NULL, 
	dt_matricula 			DATE 			NOT NULL, 
	sexo 					CHAR(1) 		NOT NULL, 
	dt_nscm 				DATE,  
	email_matricula 		VARCHAR(150),  
	endereco_matricula 		VARCHAR(500),  
	CPF						NUMERIC(11),  
	dt_termino 				DATE );""")

lista=[]
indice = 0

layout = [
    [
        sg.Text("Código de matricula:", size=(8, 1)),
        sg.InputText(size=(6, 1), key="-cod_matricula-", focus=False)
    ],
  [
        sg.Text("Código tipo de matricula:", size=(8, 1)),
        sg.InputText(size=(6, 1), key="-cod_tipo_matricula-", focus=False)
    ],
  [
        sg.Text("Código instituição:", size=(8, 1)),
        sg.InputText(size=(6, 1), key="-cod_instituicao-", focus=False)
    ],
  
    [
        sg.Text("Nome Completo:", size=(8, 1)),
        sg.InputText(size=(40, 1), key="-nome_matricula-", focus=True)
    ],
   
  # colocar dt_matricula, sexo, dt_nascimento, email_matricula, endereco_matricula, CPF, dt_termino
  [
        sg.Text("E-mail:", size=(8, 1)),
        sg.InputText(size=(40, 1), key="-EMAIL-")
    ],
    
    [
        sg.Button('Limpar', size=(8, 1), key="-LIMPAR-"),
        sg.Button('Inserir', size=(8, 1), key="-INSERIR-"),
        sg.Button('Atualizar', size=(8, 1), key="-ATUALIZAR-"),
        sg.Button('Remover', size=(8, 1), key="-REMOVER-")
    ],
    [
        sg.Button('<<', size=(8, 1), key="-<<-"),
        sg.Button('Procurar', size=(8, 1), key="-PROCURAR-"),
        sg.Button('Todos', size=(8, 1), key="-TODOS-"),
        sg.Button('>>', size=(8, 1), key="->>-")
    ]
]

window = sg.Window("Cadastro dos Amigos", layout, use_default_focus=False)

# Run the Event Loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "-LIMPAR-":
        limpar()
    elif event == "-INSERIR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("INSERT INTO amigos (nome, email, celular) VALUES (%s, %s, %s);",
                    (values['-NOME-'], values['-EMAIL-'], values['-CEL-']))
        limpar()
    elif event == "-ATUALIZAR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("UPDATE matricula SET nome = %s, email = %s, celular = %s WHERE id = %s",
                    (values['-NOME-'], values['-EMAIL-'], values['-CEL-'], values['-ID-']))
        lista[indice] = [values['-ID-'], values['-NOME-'], values['-EMAIL-'], values['-CEL-']]        
    elif event == "-REMOVER-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("DELETE FROM matricula WHERE id = %s", (values['-ID-'],))
        lista.pop(indice)
        indice -= 1
        atualiza()
    elif event == "-PROCURAR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("SELECT * FROM matricula WHERE nome LIKE %s;",
                    ('%'+values['-NOME-']+'%',))
                resposta = cursor.fetchall()
                lista.clear()
                for i in range(len(resposta)):
                    lista.append( list(resposta[i]) )
                sg.popup('Quantidade de registros: ' + str(len(resposta)))
                indice = 0
                atualiza()
    elif event == "-TODOS-":
        todos()
    elif event == "->>-":
        indice += 1
        if indice >= len(lista): indice = len(lista)-1
        atualiza()
    elif event == "-<<-":
        indice -= 1
        if indice <= 0: indice = 0
        atualiza()

window.close()

# Fazer as mudanças para a base persistente
con.commit()

# Fechar a comunicação com o servidor
cursor.close()
con.close()
