import PySimpleGUI      as sg
import window_acervo    as wa
import display_menu     as dm
import theme

from Funcoes import func_cadastro   as fc
from Funcoes import func_atualiza   as fa

def window_mat():
    layout = [
        [sg.Text("Código de Matricula: ", size = (20)), sg.Input(size=(25, 1), key = '-COD_MAT-')],
        [sg.Text("Tipo de Matrícula: ", size = (20)), sg.Input(size=(25, 1), key = '-TIPO_MAT-')],
        [sg.Text("Instituição: ", size = (20)), sg.Input(size=(25, 1), key = '-INST_MAT-')],
        [sg.Text("Nome: ", size = (20)), sg.Input(size=(25, 1), key = '-NOME_MAT-')],
        [sg.Text("Sexo: ", size = (20)), sg.Input(size=(25, 1), key = '-SEXO_MAT-')],
        [sg.Text("Data de Nascimento: ", size = (20)), sg.Input(size=(25, 1), key = '-NASC_MAT-')],
        [sg.Text("E-mail: ", size = (20)), sg.Input(size=(25, 1), key = '-EMAIL_MAT-')],
        [sg.Text("Endereço: ", size = (20)), sg.Input(size=(25, 1), key = '-ENDE_MAT-')],
        [sg.Text("CPF: ", size = (20)), sg.Input(size=(25, 1), key = '-CPF_MAT-')],
        [sg.Text("Data de Término: ", size = (20)), sg.Input(size=(25, 1), key = '-TERM_MAT-')],
        [sg.HorizontalSeparator(pad = ((0,0), (5,5)), color = "#b948b4")],
        [sg.Button('Cadastrar', size = (13, 2), key = '-CADASTRO-'), sg.Button('Atualizar', size = (13, 2), key = '-ATUALIZA-'), sg.Button('Lista de\nMatrículas', size = (13, 2), k= '-LISTA-')]
    ]
    # Gera a Janela e retorna
    return sg.Window(title= "Matrícula", layout = layout, size = (425, 375), font = 'Corbel', finalize = True)



# Cria a janela do exemplar (precisa colocar os botões do acervo)
def window_exemp():
    layout = [
        [   sg.Text('Código do Exemplar:',      size = (20)),       sg.Input(size=(23, 1),      key = '-COD_EXEMP-'     ) ],
        [   sg.Text('ISBN: ',                   size = (20)),       sg.Input(size=(23, 1),      key = '-ISBN_EXEMP-'    ) ],
        [   sg.Text('Código da Estante:',       size = (20)),       sg.Input(size=(23, 1),      key = '-COD_ESTANTE-'   ) ],
        [   sg.Text('Situação:',                size = (20)),       sg.Input(size=(23, 1),      key = '-SITUACAO-'      ) ],
        [   sg.Text('Estado de Conservação:',   size = (20)),       sg.Input(size=(23, 1),      key = '-ESTADO_CONS-'   ) ],
        [   sg.HorizontalSeparator(pad = ((0,0), (5,7)), color = "#b948b4"                                              ) ],
        [   sg.Button('Cadastrar',              size = (20),        key = '-CADASTRO-',         p=((5,0),(0,0))         ), 
            sg.Button('Atualizar',              size = (20),        key = '-ATUALIZA-',         p=((6,0),(0,0))         ) ],
        [   sg.HorizontalSeparator(pad = ((0,0), (5,0)), color = "#b948b4"                                              ) ],
        [   sg.Text(    'ACERVO',               size = (50),        justification='center'                              ) ],
        [   sg.Button(  'Disponível',           size = (9),         key = '-ACERVO_DISP-',      p=((5,0),(0,0))         ),
            sg.Button(  'Emprestado',           size = (9),         key = '-ACERVO_EMPR-',      p=((8,0),(0,0))         ),
            sg.Button(  'Perdido',              size = (9),         key = '-ACERVO_PERD-',      p=((8,0),(0,0))         ),
            sg.Button(  'Manutenção',           size = (9),         key = '-ACERVO_MANU-',      p=((8,0),(0,0))         ) ]
    ]

    return sg.Window("Exemplar", layout, font='Corbel', finalize=True, size=(410, 275))



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
        [sg.Button('Cadastrar', size = (13, 2), key = '-CADASTRO-'), sg.Button('Atualizar', size = (13, 2), key = '-ATUALIZA-'), sg.Button('Lista de\nLivros', size = (13, 2), k= '-LISTA-')]
    ]

    return sg.Window(title= "Livro", layout = layout, size = (425, 285), font = 'Corbel', finalize = True)



# Cria a janela do autor
def window_aut():
    layout = [
        [sg.Text("Código do Autor: ", size = (20)), sg.Input(size=(25, 1), key = '-COD_AUT-')],
        [sg.Text("Nome do Autor: ", size = (20)), sg.Input(size=(25, 1), key = '-NOME_AUT-')],
        [sg.Text("País de Origem: ", size = (20)), sg.Input(size=(25, 1), key = '-PAIS_AUT-')],
        [sg.HorizontalSeparator(pad = ((0,0), (5,5)), color = "#b948b4")],
        [sg.Button('Cadastrar', size = (13, 2), key = '-CADASTRO-'), sg.Button('Atualizar', size = (13, 2), key = '-ATUALIZA-'), sg.Button('Lista de\nAutores', size = (13, 2), k= '-LISTA-')]
    ]

    return sg.Window(title= "Autor", layout = layout, size = (425, 170), font = 'Corbel', finalize = True)



# Função que cria o display e realiza as operações (Matrícula)
def display_mat():
    open = None
    # Abro a janela
    window_m = window_mat()
    window_lista = None
    # Loop de leitura da tela
    while True:
        window, evento, valores = sg.read_all_windows()
        # Evento de fechamento de tela
        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_m:
                open = 'menu'
                break
            elif window == window_lista:
                window_lista = None
        # Evento de cadastro
        elif evento == '-CADASTRO-':
            if valores['-TIPO_MAT-'] == 'Estudante':
                cod_tipo_mat = 1
            elif valores['-TIPO_MAT-'] == 'Professor':
                cod_tipo_mat = 2
            elif valores['-TIPO_MAT-'] == 'Funcionário':
                cod_tipo_mat = 3
            elif valores['-TIPO_MAT-'] == 'Externo':
                cod_tipo_mat = 4

            output = fc.registra_matricula(valores['-COD_MAT-'], cod_tipo_mat, valores['-INST_MAT-'], valores['-NOME_MAT-'], valores['-SEXO_MAT-'], valores['-NASC_MAT-'], valores['-EMAIL_MAT-'], valores['-ENDE_MAT-'], valores['-CPF_MAT-'])
            sg.popup(output)
        # Evento de atualizar
        elif evento == '-ATUALIZA-':
            output = fa.atualiza_matricula(valores['-COD_MAT-'], valores['-NOME_MAT-'], valores['-SEXO_MAT-'], valores['-NASC_MAT-'], valores['-EMAIL_MAT-'], valores['-CPF_MAT-'], valores['-TERM_MAT-'])
            sg.popup(output)
        # Evento de Lista
        elif evento == '-LISTA-':
            window_lista = wa.wind_mat()
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

        elif evento == "-CADASTRO-":
            output = fc.registra_exemplar(valores['-COD_EXEMP-'], valores['-ISBN_EXEMP-'], valores['-COD_ESTANTE-'], valores['-ESTADO_CONS-'])
            sg.popup(output)

        elif evento == "-ATUALIZA-":
            if valores['-SITUACAO-'] == 'Disponível':
                cod_sit = 1
            elif valores['-SITUACAO-'] == 'Emprestado':
                cod_sit = 2
            elif valores['-SITUACAO-'] == 'Manutenção':
                cod_sit = 3
            elif valores['-SITUACAO-'] == 'Perdido':
                cod_sit = 4
            else:
                cod_sit = ''
            output = fa.atualiza_exemplar(valores['-COD_EXEMP-'], valores['-COD_ESTANTE-'], cod_sit, valores['-ESTADO_CONS-'])
            sg.popup(output)

    window.close()
    if open == 'menu':
        dm.display_menu()


# Função que cria o display e realiza as operações (Livro)
def display_liv():
    open = None
    # Abro a janela
    window_l = window_liv()
    window_lista = None
    # Loop de leitura da tela
    while True:
        window, evento, valores = sg.read_all_windows()
        # Evento de fechamento de tela
        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_l:
                open = 'menu'
                break
            elif window == window_lista:
                window_lista = None
        # Evento de cadastro
        elif evento == '-CADASTRO-':
            output = fc.registra_livro(valores['-ISBN_LIV-'], valores['-TITU_LIV-'], valores ['-DT_PUBL_LIV-'], valores ['-EDIT_LIV-'], valores ['-EDIC_LIV-'], valores ['-LOC_PUBL_LIV-'], valores ['-SUB_LIV-'])
            sg.popup(output)
        # Evento de atualizar
        elif evento == '-ATUALIZA-':
            output = fc.atualiza_livro(valores['-ISBN_LIV-'], valores['-TITU_LIV-'], valores ['-SUB_LIV-'], valores ['-DT_PUBL_LIV-'], valores ['-EDIT_LIV-'], valores ['-EDIC_LIV-'], valores ['-LOC_PUBL_LIV-'])
            sg.popup(output)
        # Evento de Lista
        elif evento == '-LISTA-':
            window_lista = wa.wind_liv()
    # Fechar janela
    window.close()
    if open == 'menu':
        dm.display_menu()



# Função que cria o display e realiza as operações (autor)
def display_aut():
    open = None

    window_a = window_aut()
    window_lista = None

    while True:
        window, evento, valores = sg.read_all_windows()

        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_a:
                open = 'menu'
                break
            elif window == window_lista:
                window_lista = None

        elif evento == '-CADASTRO-':
            output = fc.registra_autor(valores['-COD_AUT-'], valores['-NOME_AUT-'], valores ['-PAIS_AUT-'])
            sg.popup(output)

        elif evento == '-ATUALIZA-':
            output = fc.atualiza_autor(valores['-COD_AUT-'], valores['-NOME_AUT-'], valores ['-PAIS_AUT-'])
            sg.popup(output)

        elif evento == '-LISTA-':
            window_lista = wa.wind_aut()

    window.close()
    if open == 'menu':
        dm.display_menu()




#--------------------------------------------#
if __name__ == "__main__":
    theme.biblioTEC()
    dm.display_menu()
