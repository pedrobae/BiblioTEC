import PySimpleGUI as sg
from func_operacoes import reserva, emprestimo, devolucao
from display_acervo import display_disp, display_empr, display_manu, display_perd

def display_operacoes():
    largura = 500
    altura = 180
    layout = [
        [
            sg.Text('Código de Matrícula:', size = (17)),
            sg.InputText(size = (25), key = 'cod_mat'),
            sg.Text('ACERVO', size = (20))
        ],
        [
            sg.Text('Código de Exemplar:', size = (17)),
            sg.InputText(size = (25), key = 'cod_exemp'),
            sg.Button('Disponível', size = (20), key = '-ACERVO_DISP-')
        ],
        [
            sg.Button('Reservar', size = (40), key = '-RESERVAR-'),
            sg.Button('Emprestado', size = (20), key = '-ACERVO_EMPR-')
        ],
        [
            sg.Button('Emprestar', size = (40), key = '-EMPRESTAR-'),
            sg.Button('Perdido', size = (20), key = '-ACERVO_PERD-')
        ],
        [
            sg.Button('Devolver', size = (40), key = '-DEVOLVER-'),
            sg.Button('Manutenção', size = (20), key = '-ACERVO_MANU-')
        ]
    ]

    window = sg.Window('Operações', layout, size = (largura,altura))

    while True:
        evento, valores = window.read()
        
        if evento == sg.WIN_CLOSED:
            break

        elif evento == "-RESERVAR-":
            retorno = reserva(valores['cod_mat'], valores['cod_exemp'])
            if retorno == 1:
                resultado = "Reserva Efetuada"
            elif retorno == 2:
                resultado = "O exemplar está disponível."
            sg.popup(resultado)

        elif evento == "-EMPRESTAR-":
            retorno = emprestimo(valores['cod_mat'], valores['cod_exemp'])
            if retorno == 1:
                resultado = "Empréstimo Efetuado"
            elif retorno == 2:
                resultado = "O exemplar está reservado."
            elif retorno == 3:
                resultado = "O exemplar está emprestado, realize a devolução primeiro."
            sg.popup(resultado)

        elif evento == "-DEVOLVER-":
            retorno = devolucao(valores['cod_exemp'])
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
            display_disp()

        elif evento == "-ACERVO_EMPR-":
            display_empr()

        elif evento == "-ACERVO_PERD-":
            display_perd()

        elif evento == "-ACERVO_MANU-":
            display_manu()

    #fecho a janela
    window.close()
