import PySimpleGUI as sg
import func_operacoes as fo
import display_acervo as da

def display_operacoes():
    largura = 500
    altura = 180
    column_1 = [
        [
            sg.Text('Código de Matrícula:', size = (17)),
            sg.InputText(size = (25), key = 'cod_mat'),
        ],
        [
            sg.Text('Código de Exemplar:', size = (17)),
            sg.InputText(size = (25), key = 'cod_exemp'),
        ],
        [
            sg.Button('Reservar', size = (40), key = '-RESERVAR-'),
        ],
        [
            sg.Button('Emprestar', size = (40), key = '-EMPRESTAR-'),
        ],
        [
            sg.Button('Devolver', size = (40), key = '-DEVOLVER-'),
        ]
    ]

    column_2 = [
        
    ]

    column_3 = [
        [
            sg.Text('ACERVO', size = (20))
        ],
        [
            sg.Button('Disponível', size = (20), key = '-ACERVO_DISP-')
        ],
        [
            sg.Button('Emprestado', size = (20), key = '-ACERVO_EMPR-')
        ],
        [
            sg.Button('Perdido', size = (20), key = '-ACERVO_PERD-')
        ],
        [
            sg.Button('Manutenção', size = (20), key = '-ACERVO_MANU-')
        ]
    ]

    layout = [
        [sg.Column(column_1),sg.Column(column_2, s=(1,altura), background_color='black'),sg.Column(column_3)]
    ]

    window = sg.Window('Operações', layout, size = (largura,altura))

    while True:
        evento, valores = window.read()
        
        if evento == sg.WIN_CLOSED:
            break

        elif evento == "-RESERVAR-":
            retorno = fo.reserva(valores['cod_mat'], valores['cod_exemp'])
            if retorno == 1:
                resultado = "Reserva Efetuada"
            elif retorno == 2:
                resultado = "O exemplar está disponível."
            sg.popup(resultado)

        elif evento == "-EMPRESTAR-":
            retorno = fo.emprestimo(valores['cod_mat'], valores['cod_exemp'])
            if retorno == 1:
                resultado = "Empréstimo Efetuado"
            elif retorno == 2:
                resultado = "O exemplar está reservado."
            elif retorno == 3:
                resultado = "O exemplar está emprestado, realize a devolução primeiro."
            sg.popup(resultado)

        elif evento == "-DEVOLVER-":
            retorno = fo.devolucao(valores['cod_exemp'])
            if retorno == 1:
                resultado = "Devolução Efetuada"
            elif retorno == 2:
                resultado = "O exemplar está reservado"
            elif retorno == 3:
                resultado = "O exemplar não está reservado."
            elif retorno == 4:
                resultado = "O exemplar não está emprestado."
            print(resultado)
            sg.popup(resultado)

        elif evento == "-ACERVO_DISP-":
            da.display_disp()

        elif evento == "-ACERVO_EMPR-":
            da.display_empr()

        elif evento == "-ACERVO_PERD-":
            da.display_perd()

        elif evento == "-ACERVO_MANU-":
            da.display_manu()

    #fecho a janela
    window.close()

display_operacoes()
