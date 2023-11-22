import PySimpleGUI as sg
import window_acervo as wa
import display_operacoes as do
import display_cadastro as dc

menu_def = [
        ['&Cadastro', ['&Matricula', '&Exemplar', '!&Autor', '!&Livro']],
        ['&Acervo', ['&Disponível', '&Emprestado', '&Manutenção', '&Perdido']],
        ['&Operações', ['&Empréstimo', '&Devolução', '&Reserva']]
    ]

layout = [
    [sg.MenubarCustom(menu_def)]
]

window = sg.Window('Operações', layout, size = (500, 100))

while True:
    evento, valores = window.read()
    
    if evento == sg.WIN_CLOSED:
        break

    if evento == 'Disponível':
        wa.display_disp()

    if evento == 'Emprestado':
        wa.display_empr()

    if evento == 'Manutenção':
        wa.display_manu()
    
    if evento == 'Perdido':
        wa.display_perd()

    if evento in ('Empréstimo', 'Devolução', 'Reserva'):
        open = 'oper'
        break

window.close()

if open == 'oper':
    do.display_operacoes()

elif open == 'cad_mat':
    dc.cad_mat()