# ------------------------ ABANDONADO ------------------------ #
import PySimpleGUI as sg
import window_acervo as wa
from Funcoes import func_operacoes as fo
import theme

def menu_bar():
    menu_def = [
            ['&Cadastro',   ['&Matricula',  '&Exemplar',    '!&Autor',      '!&Livro'   ]   ],
            ['&Acervo',     ['&Disponível', '&Emprestado',  '&Manutenção',  '&Perdido'  ]   ],
            ['&Operações',  ['&Empréstimo', '&Devolução',   '&Reserva'                  ]   ]
        ]
    return sg.MenubarCustom(menu_def)


def window_operacoes_bar():
    layout = [
        [ menu_bar() ],
        [ sg.Text ('Código de Matrícula:',  size = (17)),   sg.InputText(size = (25), key = 'cod_mat')      ],
        [ sg.Text ('Código de Exemplar:',   size = (17)),   sg.InputText(size = (25), key = 'cod_exemp')    ],
        [ sg.Button ('Reservar',            size = (40),    key = '-RESERVAR-')     ],
        [ sg.Button ('Emprestar',           size = (40),    key = '-EMPRESTAR-')    ],
        [ sg.Button ('Devolver',            size = (40),    key = '-DEVOLVER-')     ]
    ]

    return sg.Window('Operações', layout, size = (300, 180), finalize=True)


def window_matricula_bar():
    layout = [
        [ menu_bar() ],
        [ sg.Text ('Código de Matrícula:',  size = (17)),   sg.InputText(size = (25), key = 'cod_mat')      ],
        [ sg.Text ('Tipo Matrícula:',       size = (17)),   sg.InputText(size = (25), key = 'tipo_mat')     ],
        [ sg.Text ('Instituicao: ',         size = (17)),   sg.InputText(size = (25), key = 'intituicao')   ],
        [ sg.Text ('Nome: ',                size = (17)),   sg.InputText(size = (25), key = 'nome')         ],
        [ sg.Text ('Gênero: ',              size = (17)),   sg.InputText(size = (25), key = 'genero')       ],
        [ sg.Text ('Data de Nascimento: ',  size = (17)),   sg.InputText(size = (25), key = 'dt_nscm')      ],
        [ sg.Text ('E-mail: ',              size = (17)),   sg.InputText(size = (25), key = 'e-mail')       ],
        [ sg.Text ('Endereço: ',            size = (17)),   sg.InputText(size = (25), key = 'endereco')     ],
        [ sg.Text ('CPF: ',                 size = (17)),   sg.InputText(size = (25), key = 'cpf')          ],
        [ sg.Text ('Data de Término: ',     size = (17)),   sg.InputText(size = (25), key = 'dt_termino')   ],
        [ sg.Button ('Cadastrar', s= (17), key= '-CAD-'),   sg.Button('Atualizar', size=(17), key= '-ATT-') ]
    ]

    return sg.Window('Matrícula', layout, size = (500, 330), finalize=True)


def display_operacoes_bar():
    open = None
    window_ope_bar = window_operacoes_bar()
    window_disp, window_empr, window_manu, window_perd = None, None, None, None
    while True:
        
        window, evento, valores = sg.read_all_windows()
        
        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_ope_bar:
                break

            elif window in (window_disp, window_empr, window_manu, window_perd):
                window_disp, window_empr, window_manu, window_perd = None, None, None, None

        elif evento == 'Disponível':
            wa.wind_disp()

        elif evento == 'Emprestado':
            wa.wind_empr()

        elif evento == 'Manutenção':
            wa.wind_manu()
        
        elif evento == 'Perdido':
            wa.wind_perd()

        elif evento == 'Matricula':
            open = 'cad_mat'
            break

        elif evento == 'Exemplar':
            open = 'cad_exemp'
            break
        
        elif evento == 'Autor':
            open = 'cad_aut'
            break

        elif evento == 'Livro':
            open = 'cad_liv'
            break

        elif evento == "-RESERVAR-":
            retorno = fo.reserva(valores['cod_mat'], valores['cod_exemp'])
            sg.popup(retorno)

        elif evento == "-EMPRESTAR-":
            retorno = fo.emprestimo(valores['cod_mat'], valores['cod_exemp'])
            sg.popup(retorno)

        elif evento == "-DEVOLVER-":
            retorno = fo.devolucao(valores['cod_exemp'])
            sg.popup(retorno)

        elif evento in ('Empréstimo', 'Devolução', 'Reserva'):
            sg.popup("Já está aberto")

    window.close()

    if open == 'cad_mat':
        display_matricula_bar()

    elif open == 'cad_exemp':
        display_exemplar_bar()
    
    elif open == 'cad_liv':
        display_livro_bar()
    
    elif open == 'cad_aut':
        display_autor_bar()


def display_matricula_bar():
    open = None
    window_mat = window_matricula_bar()
    window_acervo_mat = None
    while True:
        
        window, evento, valores = sg.read_all_windows()
        
        if evento == sg.WIN_CLOSED:
            window.close()
            if window == window_mat:
                break

            elif window == window_acervo_mat:
                window_acervo_mat = None
        
        elif evento == 'Disponível':
            wa.wind_disp()

        elif evento == 'Emprestado':
            wa.wind_empr()

        elif evento == 'Manutenção':
            wa.wind_manu()
        
        elif evento == 'Perdido':
            wa.wind_perd()

        elif evento == 'Matricula':
            sg.popup("Já está aberto")
            break

        elif evento == 'Exemplar':
            open = 'cad_exemp'
            break
        
        elif evento == 'Autor':
            open = 'cad_aut'
            break

        elif evento == 'Livro':
            open = 'cad_liv'
            break

        elif evento in ('Empréstimo', 'Devolução', 'Reserva'):
            open = 'opera'
            break

    window.close()

    if open == 'opera':
        display_operacoes_bar()

    elif open == 'cad_exemp':
        display_exemplar_bar()
    
    elif open == 'cad_liv':
        display_livro_bar()
    
    elif open == 'cad_aut':
        display_autor_bar()


if __name__ == "__main__":
    theme.biblioTEC()
    display_matricula_bar()