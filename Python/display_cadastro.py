import PySimpleGUI as sg
from Funcoes import func_acervo as fa
from Funcoes import func_cadastro as fc
import display_menu as dm

def window_mat():
    
    # Layout
    layout = [
        [sg.Text("Código de Matricula: "), sg.Input(size=(10, 1), key = '-COD_MAT-')],
        [sg.Text("Tipo de Matrícula: "), sg.Input(size=(18, 1), key = '-TIPO_MAT-')],
        [sg.Text("Instituição: "), sg.Input(size=(18, 1), key = '-INST_MAT-')],
        [sg.Text("Sexo: "), sg.Input(size=(18, 1), key = '-SEXO_MAT-')],
        [sg.Text("Data de Nascimento: "), sg.Input(size=(10, 1), key = '-NASC_MAT-')],
        [sg.Text("E-mail: "), sg.Input(size=(25, 1), key = '-EMAIL_MAT-')],
        [sg.Text("Endereço: "), sg.Input(size=(50, 1), key = '-ENDE_MAT-')],
        [sg.Text("CPF: "), sg.Input(size=(12, 1), key = '-CPF_MAT-')],
        [sg.Button('Cadastrar', size = (40), key = '-CADASTRO-')],
        [sg.Button('Atualizar', size = (40), key = '-ATUALIZA-')]
    ]

    # Gera a Janela e retorna
    return sg.Window(title= "Matrícula", layout = layout, size = (600, 300))
    
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
            output = fc.registra_matricula(valores['-COD_MAT-'], valores['-TIPO_MAT-'], valores ['-INST_MAT-'], valores ['-SEXO_MAT-'], valores ['-NASC_MAT-'], valores ['-EMAIL_MAT-'], valores ['-ENDE_MAT-'], valores ['-CPF_MAT-'])
            sg.popup(output)

        # Evento de atualizar
        elif evento == '-ATUALIZA-':
            output2 = fc.atualiza_matricula(valores['-COD_MAT-'], valores['-TIPO_MAT-'], valores ['-INST_MAT-'], valores ['-SEXO_MAT-'], valores ['-NASC_MAT-'], valores ['-EMAIL_MAT-'], valores ['-ENDE_MAT-'], valores ['-CPF_MAT-'])
            sg.popup(output2)

    # Fechar janela
    window.close()

    if open == 'menu':
        dm.display_menu()

if __name__ == "__main__":
    display_mat()

