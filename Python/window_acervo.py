import PySimpleGUI as sg
import func_acervo as fa

def wind_disp():
    acervo = fa.acervo_disp()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Data de Aquisição'])]
        ]
    return sg.Window('Acervo Disponível', layout, finalize=True)



def wind_empr():
    acervo = fa.acervo_empr()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Matricula do Empréstimo', 'Data Prevista de Devolução'])]
        ]
    return sg.Window('Acervo Emprestado', layout, finalize=True)



def wind_manu():
    acervo = fa.acervo_manu()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo'])]
        ]
    return sg.Window('Acervo em Manutenção', layout, finalize=True)


def wind_perd():
    acervo = fa.acervo_perd()
    layout = [
        [sg.Table(acervo, ['Código do Exemplar','Titulo','Matricula do Último Empréstimo'])]
        ]
    return sg.Window('Acervo Perdido', layout, finalize=True)


def wind_liv():
    acervo = fa.acervo_liv()
    layout = [
        [sg.Table(acervo, ['ISBN','Titulo','Subtitulo','dt_publ','editora','local_publ'])]
        ]
    return sg.Window('Livros Registrados', layout, finalize=True)


def wind_mat():
    acervo = fa.acervo_mat()
    layout = [
        [sg.Table(acervo, ['cod_matricula', 'descr_matricula', 'nome_matricula', 'sexo', 'dt_nscm', 'dt_termino'])]
        ]
    return sg.Window('Matriculas Registradas', layout, finalize=True)


def wind_aut():
    acervo = fa.acervo_aut()
    layout = [
        [sg.Table(acervo, ['cod_autor', 'nome_autor', 'pais_autor'])]
        ]
    return sg.Window('Autores Registrados', layout, finalize=True)