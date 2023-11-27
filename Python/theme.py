import PySimpleGUI as sg

def biblioTEC():
    # Purple    = #1f122f
    # Lilas     = #b948b4
    # Font      = 'Corbel'
    sg.LOOK_AND_FEEL_TABLE['BiblioTEC'] = {
        'BACKGROUND': '#1f122f',
        'TEXT': 'White',
        'INPUT': 'White',
        'TEXT_INPUT': 'Black',
        'SCROLL': '#b948b4',
        'BUTTON': ('Black', 'White'),
        'PROGRESS': ('#D1826B', '#CC8019'),
        'BORDER': 1, 'SLIDER_DEPTH': 0, 
        'PROGRESS_DEPTH': 0, }

    sg.theme('BiblioTEC')