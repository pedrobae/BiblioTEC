import PySimpleGUI as sg
import display_cadastro as dc
import display_operacoes as do
import window_acervo as wa
import theme

def window_menu():
    
    coluna_cad = [
        [sg.Text('Cadastros', size = (20), justification='center')],
        [sg.Button('Autor', size = (20), key = '-CADASTRO_AUTOR-')],
        [sg.Button('Livro', size = (20), key = '-CADASTRO_LIVRO-')],
        [sg.Button('Exemplar', size = (20), key = '-CADASTRO_EXEMPLAR-')],
        [sg.Button('Matrícula', size = (20), key = '-CADASTRO_MATRICULA-')]
    ]

    coluna_oper = [
        [sg.Text('Operações', size = (20), justification='center')],
        [sg.Button('Operações', size = (20), key = '-OPERACOES-')]
    ]

    coluna_acrv = [
        [sg.Text('Acervo', size = (20), justification='center')],
        [sg.Button('Disponível', size = (20), key = '-ACERVO_DISP-')],
        [sg.Button('Emprestado', size = (20), key = '-ACERVO_EMPR-')],
        [sg.Button('Perdido', size = (20), key = '-ACERVO_PERD-')],
        [sg.Button('Manutenção', size = (20), key = '-ACERVO_MANU-')]
    ]

    layout = [
        [sg.Image('images/Logo.png', expand_x=True, expand_y=True)],
        [sg.HorizontalSeparator(color='#b948b4')],
        [sg.Column(coluna_cad, s=(200, 180)), sg.Column([], s=(2,180), background_color='#b948b4'), sg.Column(coluna_oper, s=(200, 180)), sg.Column([], s=(2,180), background_color='#b948b4'), sg.Column(coluna_acrv,s=(182, 180))]
    ]

    return sg.Window('Menu', layout, size= (665, 400), finalize=True, font='Corbel')


def display_menu():
    open = None
    window_mn = window_menu()
    window_disp, window_empr, window_manu, window_perd = None, None, None, None

    while True:
        window, evento, valores = sg.read_all_windows()
        
        if evento == sg.WIN_CLOSED:
            window.close()

            if window == window_mn:
                break

            elif window in (window_disp, window_empr, window_manu, window_perd):
                window_disp, window_empr, window_manu, window_perd = None, None, None, None
        
        elif evento == "-ACERVO_DISP-" and not window_disp:
            window_disp = wa.wind_disp()

        elif evento == "-ACERVO_EMPR-" and not window_empr:
            window_empr = wa.wind_empr()
            
        elif evento == "-ACERVO_MANU-" and not window_manu:
            window_manu = wa.wind_manu()

        elif evento == "-ACERVO_PERD-" and not window_perd:
            window_perd = wa.wind_perd()

        elif evento == "-CADASTRO_AUTOR-":
            open = 'CADASTRO_AUTOR'
            window.close()
            break

        elif evento == "-CADASTRO_LIVRO-":
            open = 'CADASTRO_LIVRO'
            window.close()
            break

        elif evento == "-CADASTRO_EXEMPLAR-":
            open = 'CADASTRO_EXEMPLAR'
            window.close()
            break

        elif evento == "-CADASTRO_MATRICULA-":
            open = 'CADASTRO_MATRICULA'
            window.close()
            break

        elif evento == "-CADASTRO_MATRICULA-":
            open = 'CADASTRO_MATRICULA'
            window.close()
            break

        elif evento == "-OPERACOES-":
            open = 'OPERACOES'
            window.close()
            break

    if open == 'CADASTRO_AUTOR':
        dc.display_aut()
    elif open == 'CADASTRO_LIVRO':
        dc.display_liv()
    elif open == 'CADASTRO_EXEMPLAR':
        dc.display_exemp()
    elif open == 'CADASTRO_MATRICULA':
        dc.display_mat()
    elif open == 'OPERACOES':
        do.display_operacoes()

            

if __name__ == "__main__":
    theme.biblioTEC()
    display_menu()