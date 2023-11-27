import PySimpleGUI      as sg
import window_acervo    as wa
import display_menu     as dm
import theme

from Funcoes import func_cadastro   as fc

def window_mat():
    layout = [
        [sg.Text("Código de Matricula: ", size = (20)), sg.Input(size=(25, 1), key = '-COD_MAT-')],
        [sg.Text("Tipo de Matrícula: ", size = (20)), sg.Input(size=(25, 1), key = '-TIPO_MAT-')],
        [sg.Text("Instituição: ", size = (20)), sg.Input(size=(25, 1), key = '-INST_MAT-')],
        [sg.Text("Sexo: ", size = (20)), sg.Input(size=(25, 1), key = '-SEXO_MAT-')],
        [sg.Text("Data de Nascimento: ", size = (20)), sg.Input(size=(25, 1), key = '-NASC_MAT-')],
        [sg.Text("E-mail: ", size = (20)), sg.Input(size=(25, 1), key = '-EMAIL_MAT-')],
        [sg.Text("Endereço: ", size = (20)), sg.Input(size=(25, 1), key = '-ENDE_MAT-')],
        [sg.Text("CPF: ", size = (20)), sg.Input(size=(25, 1), key = '-CPF_MAT-')],
        [sg.HorizontalSeparator(pad = ((0,0), (5,5)), color = "#b948b4")],
        [sg.Button('Cadastrar', size = (20), key = '-CADASTRO-'), sg.Button('Atualizar', size = (20), key = '-ATUALIZA-')]
    ]
    # Gera a Janela e retorna
    return sg.Window(title= "Matrícula", layout = layout, size = (425, 300), font = 'Corbel')



# Cria a janela do exemplar (precisa colocar os botões do acervo)
def window_exemp():
    layout = [
        []
    ]

    return sg.Window(title= "Exemplar", layout = layout, font = 'Corbel')



# Cria a janela do livro
def window_liv():
    layout = [
        [sg.Text("ISBN do Livro: ", size = (20)), sg.Input(size=(25, 1), key = '-ISBN_LIV-')],
        [sg.Text("Título: ", size = (20)), sg.Input(size=(25, 1), key = '-TITU_LIV-')],
        [sg.Text("Subtítulo: ", size = (20)), sg.Input(size=(25, 1), key = '-SUB_LIV-')],
        [sg.Text("Data de publicação: ", size = (20)), sg.Input(size=(25, 1), key = '-DT_PUBL_LIV-')],
        [sg.Text("Editora: ", size = (20)), sg.Input(size=(25, 1), key = '-EDIT_LIV-')],
        [sg.Text("Edição: ", size = (20)), sg.Input(size=(25, 1), key = '-EDIC_LIV-')],
        [sg.Text("Local de publicação: ", size = (20)), sg.Input(size=(25, 1), key = '-LOC_PUBL_LIV-')],
        [sg.HorizontalSeparator(pad = ((0,0), (5,5)), color = "#b948b4")],
        [sg.Button('Cadastrar', size = (20), key = '-CADASTRO-'), sg.Button('Atualizar', size = (20), key = '-ATUALIZA-')]
    ]

    return sg.Window(title= "Livro", layout = layout, font = 'Corbel')



# Cria a janela do autor
def window_aut():
    layout = [
        [sg.Text("ISBN do Livro: ", size = (20)), sg.Input(size=(25, 1), key = '-ISBN_LIV-')],
        [sg.Text("Título: ", size = (20)), sg.Input(size=(25, 1), key = '-TITU_LIV-')],
        [sg.Text("Subtítulo: ", size = (20)), sg.Input(size=(25, 1), key = '-SUB_LIV-')],
        [sg.Text("Data de publicação: ", size = (20)), sg.Input(size=(25, 1), key = '-DT_PUBL_LIV-')],
        [sg.Text("Editora: ", size = (20)), sg.Input(size=(25, 1), key = '-EDIT_LIV-')],
        [sg.Text("Edição: ", size = (20)), sg.Input(size=(25, 1), key = '-EDIC_LIV-')],
        [sg.Text("Local de publicação: ", size = (20)), sg.Input(size=(25, 1), key = '-LOC_PUBL_LIV-')],
        [sg.HorizontalSeparator(pad = ((0,0), (5,5)), color = "#b948b4")],
        [sg.Button('Cadastrar', size = (20), key = '-CADASTRO-'), sg.Button('Atualizar', size = (20), key = '-ATUALIZA-')]
    ]

    return sg.Window(title= "Livro", layout = layout, font = 'Corbel')

    return sg.Window(title= "Autor", layout = layout, font = 'Corbel')



# Função que cria o display e realiza as operações (mat)
def display_mat():
    open = None
    # Abro a janela
    window = window_mat()
    # Loop de leitura da tela
    while True:
        evento, valores = window.read()
        # Evento de fechamento de tela
        if evento == sg.WIN_CLOSED:
            open = 'menu'
            break
        # Evento de cadastro
        elif evento == '-CADASTRO-':
            output = fc.registra_matricula(valores['-COD_MAT-'], valores['-TIPO_MAT-'], valores ['-INST_MAT-'], valores ['-SEXO_MAT-'], valores ['-NASC_MAT-'], valores ['-EMAIL_MAT-'], valores ['-ENDE_MAT-'], valores ['-CPF_MAT-'])
            sg.popup(output)
        # Evento de atualizar
        elif evento == '-ATUALIZA-':
            output = fc.atualiza_matricula(valores['-COD_MAT-'], valores['-TIPO_MAT-'], valores ['-INST_MAT-'], valores ['-SEXO_MAT-'], valores ['-NASC_MAT-'], valores ['-EMAIL_MAT-'], valores ['-ENDE_MAT-'], valores ['-CPF_MAT-'])
            sg.popup(output)
    # Fechar janela
    window.close()
    if open == 'menu':
        dm.display_menu()



# Função que cria o display e realiza as operações (exemplar)
def display_exemp():
    open = None
    window_ex = window_exemp()
    window_disp, window_empr, window_manu, window_perd = None, None, None, None

    while True:
        window, evento, valores = sg.read_all_windows()

        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_ex:
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

        elif evento == "-ACERVO_DISP-" and not window_disp:
            window_disp = wa.wind_disp()
        elif evento == "-ACERVO_EMPR-" and not window_empr:
            window_empr = wa.wind_empr()
        elif evento == "-ACERVO_MANU-" and not window_manu:
            window_manu = wa.wind_manu()
        elif evento == "-ACERVO_PERD-" and not window_perd:
            window_perd = wa.wind_perd()

    window.close()
    if open == 'menu':
        dm.display_menu()


# Função que cria o display e realiza as operações (livro)
def display_liv():
    open = None
    window = window_liv()
    while True:
        evento, valores = window.read()
        # Evento de fechamento de tela
        if evento == sg.WIN_CLOSED:
            open = 'menu'
            break
        # Evento de cadastro
        elif evento == '-CADASTRO-':
            output = fc.registra_livro(valores['-ISBN_LIV-'], valores['-TITU_LIV-'], valores ['-SUB_LIV-'], valores ['-DT_PUBL_LIV-'], valores ['-EDIT_LIV-'], valores ['-EDIC_LIV-'], valores ['-LOC_PUBL_LIV-'])
            sg.popup(output)
        # Evento de atualizar
        elif evento == '-ATUALIZA-':
            output = fc.atualiza_livro(valores['-ISBN_LIV-'], valores['-TITU_LIV-'], valores ['-SUB_LIV-'], valores ['-DT_PUBL_LIV-'], valores ['-EDIT_LIV-'], valores ['-EDIC_LIV-'], valores ['-LOC_PUBL_LIV-'])
            sg.popup(output)
    # Fechar janela
    window.close()
    if open == 'menu':
        dm.display_menu()



# Função que cria o display e realiza as operações (autor)
def display_aut():

    window = window_aut()

    while True:

    window.close()
    if open == 'menu':
        dm.display_menu()



#--------------------------------------------#
if __name__ == "__main__":
    theme.biblioTEC()
    display_mat()
