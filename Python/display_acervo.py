import PySimpleGUI as sg
from func_acervo import acervo_disp, acervo_empr, acervo_manu, acervo_perd

def display_disp():
    acervo = acervo_disp()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Data de Aquisição'])]
        ]
    window = sg.Window('Acervo Disponível', layout)
    while True:
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            break



def display_empr():
    acervo = acervo_empr()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Matricula do Empréstimo', 'Data Prevista de Devolução'])]
        ]
    window = sg.Window('Acervo Emprestado', layout)
    while True:
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            break



def display_manu():
    acervo = acervo_manu()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo'])]
        ]
    window = sg.Window('Acervo em Manutenção', layout)
    while True:
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            break



def display_perd():
    acervo = acervo_perd()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Matricula do Último Empréstimo'])]
        ]
    window = sg.Window('Acervo Perdido', layout)
    while True:
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            break
