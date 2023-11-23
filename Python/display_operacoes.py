import PySimpleGUI as sg
import func_operacoes as fo
import window_acervo as wa

def window_operacoes():
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
        [sg.Column(column_1),sg.Column(column_2, s=(1,180), background_color='black'),sg.Column(column_3)]
    ]

    return sg.Window('Operações', layout, size = (500, 180), finalize=True)

def display_operacoes():
    window_ope = window_operacoes()
    window_disp, window_empr, window_manu, window_perd = None, None, None, None

    while True:
        window, evento, valores = sg.read_all_windows()
        
        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_ope:
                open = 'menu'
                break
            elif window in (window_disp, window_empr, window_manu, window_perd):
                window_disp, window_empr, window_manu, window_perd = None, None, None, None

        elif evento == "-RESERVAR-":
            retorno = fo.reserva(valores['cod_mat'], valores['cod_exemp'])
            sg.popup(retorno)

        elif evento == "-EMPRESTAR-":
            retorno = fo.emprestimo(valores['cod_mat'], valores['cod_exemp'])
            sg.popup(retorno)

        elif evento == "-DEVOLVER-":
            retorno = fo.devolucao(valores['cod_exemp'])
            sg.popup(retorno)

        elif evento == "-ACERVO_DISP-" and not window_disp:
            window_disp = wa.wind_disp()

        elif evento == "-ACERVO_EMPR-" and not window_empr:
            window_empr = wa.wind_empr()
            
        elif evento == "-ACERVO_MANU-" and not window_manu:
            window_manu = wa.wind_manu()

        elif evento == "-ACERVO_PERD-" and not window_perd:
            window_perd = wa.wind_perd()

    #fecho a janela
    window.close()

#    if open == 'menu':
#        display_menu

if __name__ == "__main__":
    display_operacoes()