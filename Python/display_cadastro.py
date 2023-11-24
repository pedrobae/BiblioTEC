import PySimpleGUI as sg
import func_acervo as fa
import func_cadastro as fc
import display_menu as dm

# Função que gera a janela das matriculas
def window_mat():
    
    # Layout
    layout = [
        [sg.Text("Código de Matricula: "), sg.Input(size=(10, 1), key = '-COD_MAT-')],
        [sg.Text("")]
        [sg.Button()]
    ]

    # Gera a Janela e retorna
    return sg.Window(title= "Matrícula", layout = layout, size = ())
    
# Função que cria o display e realiza as operações
def display_mat():

    # Abro a janela
    window = window_mat()

    # Loop de leitura da tela
    while True:
        evento, valores = window.read()

        # Evento de fechamento de tela
        if evento == sg.WIN_CLOSED():
            open = 'menu'
            break

        # Evento de cadastro
        elif evento == '-CADASTRO-':
            output = fc.registra_matricula(valores['-COD_MAT-'], valores['-NOME_MAT-'])
            sg.popup(output)
        # Evento de atualização


        # Evento de mostrar as matrículas


    # Fecho a Janela
    window.close()

    # Abro o Menu
    if open == 'menu':
        dm.display_menu()

