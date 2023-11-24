import PySimpleGUI as sg
import func_acervo as fa
import func_cadastro as fc

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
    # Gera as janelas
    window_mat = window_mat()
    # Loop de leitura da tela
    while True:
        window, evento, valores = sg.read_all_windows()
        # Evento de fechamento de tela
        if evento == sg.WIN_CLOSED():
            window.close()
        # Evento de cadastro
        if evento == '-CADASTRO-':
            output = fc.registra_matricula(valores['-COD_MAT-'], valores['-NOME_MAT-'])
            sg.popup(output)
        # Evento de atualização

        # Evento de mostrar as matrículas
