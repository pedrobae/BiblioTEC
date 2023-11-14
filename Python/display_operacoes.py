import PySimpleGUI as sg
from func_operacoes import reserva, emprestimo, devolucao
from func_acervo import acervo_disp, acervo_empr, acervo_manu, acervo_perd

def operacoes():
    largura = 700
    altura = 150
    layout = [
        [
            sg.Text('Código de Matrícula:', size = (21)),
            sg.InputText(size = (48), key = 'cod_mat'),
            sg.Text('ACERVO', size = (21))
        ],
        [
            sg.Text('Código de Exemplar:', size = (21)),
            sg.InputText(size = (48), key = 'cod_exemp'),
            sg.Button('Disponível', size = (21), key = '-ACERVO_DISP-')
        ],
        [
            sg.Button('Reservar', size = (21), key = '-RESERVAR-'),
            sg.Button('Emprestado', size = (21), key = '-ACERVO_EMPR-')
        ],
        [
            sg.Button('Emprestar', size = (21), key = '-EMPRESTAR-'),
            sg.Button('Perdido', size = (21), key = '-ACERVO_PERD-')
        ],
        [
            sg.Button('Devolver', size = (21), key = '-DEVOLVER-'),
            sg.Button('Manutenção', size = (21), key = '-ACERVO_MANU-')
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
            sg.popup(acervo_disp())

        elif evento == "-ACERVO_EMPR-":
            sg.popup(acervo_disp())

        elif evento == "-ACERVO_PERD-":
            sg.popup(acervo_disp())

        elif evento == "-ACERVO_MANU-":
            sg.popup(acervo_disp())

    #fecho a janela
    window.close()