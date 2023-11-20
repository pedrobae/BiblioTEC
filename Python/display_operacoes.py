import PySimpleGUI as sg
import func_operacoes as fo
import window_acervo as wa

def window_operacoes():
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

    return sg.Window('Operações', layout, size = (largura,altura))

def display_operacoes():
    wind_opera = window_operacoes
    wind_disp, wind_empr, wind_manu, wind_perd = None, None, None, None

    while True:
        window, evento, valores = sg.read_all_windows()
        
        if evento == sg.WIN_CLOSED:
            window.close()
            if window == wind_opera:
                open = 'menu'
                break
            elif window in (wind_disp, wind_empr, wind_manu, wind_perd):
                wind_disp, wind_empr, wind_manu, wind_perd = None, None, None, None

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

        elif evento == "-ACERVO_DISP-" and not wind_disp:
            wind_disp = wa.display_disp()

        elif evento == "-ACERVO_EMPR-" and not wind_empr:
            wind_empr = wa.display_empr()
            
        elif evento == "-ACERVO_MANU-" and not wind_manu:
            wind_manu = wa.display_manu()

        elif evento == "-ACERVO_PERD-" and not wind_perd:
            wind_perd = wa.display_perd()

    #fecho a janela
    window.close()

#    if open == 'menu':
#        display_menu

if __name__ == "__main__":
    display_operacoes()