import PySimpleGUI as sg
import window_acervo as wa
# import display_cadastro as dc
import func_operacoes as fo

def menu_bar():
    menu_def = [
            ['&Cadastro', ['&Matricula', '&Exemplar', '!&Autor', '!&Livro']],
            ['&Acervo', ['&Disponível', '&Emprestado', '&Manutenção', '&Perdido']],
            ['&Operações', ['&Empréstimo', '&Devolução', '&Reserva']]
        ]
    return sg.MenubarCustom(menu_def)

def window_operacoes_bar():
    layout = [
        [   
            menu_bar()
        ],
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

    return sg.Window('Operações', layout, size = (300, 180), finalize=True)

def display_operacoes_bar():
    window_ope_bar = window_operacoes_bar()
    window_disp, window_empr, window_manu, window_perd = None, None, None, None
    while True:
        
        window, evento, valores = sg.read_all_windows()
        
        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_ope_bar:
                break

            elif window in (window_disp, window_empr, window_manu, window_perd):
                window_disp, window_empr, window_manu, window_perd = None, None, None, None

        elif evento == 'Disponível':
            wa.wind_disp()

        elif evento == 'Emprestado':
            wa.wind_empr()

        elif evento == 'Manutenção':
            wa.wind_manu()
        
        elif evento == 'Perdido':
            wa.wind_perd()

        elif evento == "-RESERVAR-":
            retorno = fo.reserva(valores['cod_mat'], valores['cod_exemp'])
            if retorno == 1:
                resultado = "Reserva Efetuada."
            elif retorno == 2:
                resultado = "O exemplar está disponível."
            sg.popup(resultado)

        elif evento == "-EMPRESTAR-":
            retorno = fo.emprestimo(valores['cod_mat'], valores['cod_exemp'])
            if retorno == 1:
                resultado = "Empréstimo Efetuado."
            elif retorno == 2:
                resultado = "O exemplar está reservado."
            elif retorno == 3:
                resultado = "O exemplar está emprestado."
            sg.popup(resultado)

        elif evento == "-DEVOLVER-":
            retorno = fo.devolucao(valores['cod_exemp'])
            if retorno == 1:
                resultado = "Devolução Efetuada."
            elif retorno == 2:
                resultado = "O exemplar está reservado."
            elif retorno == 3:
                resultado = "Devolução Efetuada.\nO exemplar não está reservado."
            elif retorno == 4:
                resultado = "Devolução Efetuada.\nO exemplar não está emprestado."
            print(resultado)
            sg.popup(resultado)
        elif evento in ('Empréstimo', 'Devolução', 'Reserva'):
            sg.popup("Já está aberto")

    window.close()

#    if open == 'cad_mat':
#        dc.cad_mat()

if __name__ == "__main__":
    display_operacoes_bar()