import PySimpleGUI as sg
from biblioteca import reserva, emprestimo, devolucao

def operacoes():
    largura = 600
    altura = 400
    layout = [
        [
            sg.Text('Código de Matrícula:', size =(largura/4, altura/4)),
            sg.InputText(key = 'cod_mat')
        ],
        [
            sg.Text('Código de Exemplar:', size =(largura/4, altura/4)),
            sg.InputText(key = 'cod_exemp')
        ],
        [
            sg.Button('Reservar', size(largura/3, altura/2), key = '-RESERVAR-'),
            sg.Button('Emprestar', size(largura/3, altura/2), key = '-EMPRESTAR-'),
            sg.Button('Devolver', size(largura/3, altura/2), key = '-DEVOLVER-'),
        ]
    ]

    window = sg.Window('Operações', layout, size = (largura,altura))

    while True:
        evento, valores = window.read()
        
        if evento == sg.WIN_CLOSED:
            break

        elif evento == "-RESERVAR-":
            retorno = biblioteca.reserva(valores['cod_mat'], valores['cod_exemp'])

            if retorno == 1:
                resultado = "Reserva Efetuada"
            elif retorno == 2:
                resultado = "O exemplar está disponível."
            sg.popup(resultado)

        elif evento == "-EMPRESTAR-":
            retorno = biblioteca.emprestimo(valores['cod_mat'], valores['cod_exemp'])

            if retorno == 1:
                resultado =
            sg.popup()

        elif evento == "-DEVOLVER-":
            sg.popup()

    #fecho a janela
    window.close()