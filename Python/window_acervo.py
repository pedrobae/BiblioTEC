import PySimpleGUI as sg
from func_acervo import acervo_disp, acervo_empr, acervo_manu, acervo_perd

def wind_disp():
    acervo = acervo_disp()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Data de Aquisição'])]
        ]
    return sg.Window('Acervo Disponível', layout, finalize=True)



def wind_empr():
    acervo = acervo_empr()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Matricula do Empréstimo', 'Data Prevista de Devolução'])]
        ]
    return sg.Window('Acervo Emprestado', layout, finalize=True)



def wind_manu():
    acervo = acervo_manu()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo'])]
        ]
    return sg.Window('Acervo em Manutenção', layout, finalize=True)


def wind_perd():
    acervo = acervo_perd()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Matricula do Último Empréstimo'])]
        ]
    return sg.Window('Acervo Perdido', layout, finalize=True)