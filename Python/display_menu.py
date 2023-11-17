import PySimpleGUI as sg
import display_acervo as acrv

menu_def = [
    ['&Cadastro', ['&Matricula::-cad_mat-', '&Exemplar:-cad_exe-', '!&Autor:-cad_aut-', '!&Livro:-cad_liv-']],
    ['&Acervo', ['&Disponível::-acrv_disp-', '&Emprestado::-acrv_empr-', '&Manutenção::-acrv_manu-', '&Perdido::-acrv_perd-']],
    ['&Operações', ['&Empréstimo::-ope_emp-', '&Devolução::-ope_dev-', '&Reserva::-ope_res-']]
]

layout = [
    [
        sg.MenubarCustom(menu_def, tearoff = True)
    ]
]

window = sg.Window('Operações', layout, size = (500, 100))

while True:
    evento, valores = window.read()
    
    if evento == sg.WIN_CLOSED:
        break

    if evento == '-acrv_disp-':
        acrv.acervo_disp()

window.close()