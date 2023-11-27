import PySimpleGUI as sg
from Funcoes import func_operacoes as fo
import window_acervo as wa
import display_menu as dm
import theme

def window_operacoes():
    culuna_ope = [
        [   sg.Text(    'Código de Matrícula:',     size = (17, 1),     p=((0,5),(3,4))),
            sg.InputText(size = (25, 1),            key = 'cod_mat',    p=((0,0),(3,4)))    ],
        [   sg.Text(    'Código de Exemplar:',      size = (17, 1),     p=((0,5),(3,5))), 
            sg.InputText(size = (25, 1),            key = 'cod_exemp',  p=((0,0),(3,5)))    ],
        [   sg.Button(  'Reservar',                 size = (40, 1),     key = '-RESERVAR-',     p=((0,0),(3,3)))    ],
        [   sg.Button(  'Emprestar',                size = (40, 1),     key = '-EMPRESTAR-',    p=((0,0),(3,3)))    ],
        [   sg.Button(  'Devolver',                 size = (40, 1),     key = '-DEVOLVER-',     p=((0,0),(3,3)))    ]
    ]

    coluna_acervo = [
        [   sg.Text(    'ACERVO',       size = (20, 1),     justification= 'center',    p=((0,0),(0,3)))    ],
        [   sg.Button(  'Disponível',   size = (20, 1),     key = '-ACERVO_DISP-',      p=((0,0),(3,3)))    ],
        [   sg.Button(  'Emprestado',   size = (20, 1),     key = '-ACERVO_EMPR-',      p=((0,0),(3,3)))    ],
        [   sg.Button(  'Perdido',      size = (20, 1),     key = '-ACERVO_PERD-',      p=((0,0),(3,3)))    ],
        [   sg.Button(  'Manutenção',   size = (20, 1),     key = '-ACERVO_MANU-',      p=((0,0),(3,3)))    ]
    ]

    layout = [
        [   sg.Column(culuna_ope,   s=(370, 200)                                ),
            sg.Column([],           s=(1,200),      background_color='#b948b4'  ),
            sg.Column(coluna_acervo                                             )   ]
    ]

    return sg.Window('Operações', layout, size = (600, 190), finalize=True, font='Corbel')

def display_operacoes():
    open = None
    window_ope = window_operacoes()
    window_disp, window_empr, window_manu, window_perd = None, None, None, None

    while True:
        window, evento, valores = sg.read_all_windows()
        
        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_ope:
                open = 'menu'
                break
            elif window == window_disp:
                window_disp = None
            elif window == window_empr:
                window_empr = None
            elif window == window_manu:
                window_manu = None
            elif window == window_perd:
                window_perd = None

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

    if open == 'menu':
        dm.display_menu()

if __name__ == "__main__":
    theme.biblioTEC()
    display_operacoes()