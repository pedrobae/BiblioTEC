import PySimpleGUI as sg

def biblioTEC():
    # Purple = #1f122f
    # Lilas = #b948b4
    sg.LOOK_AND_FEEL_TABLE['BiblioTEC'] = {
        'BACKGROUND': '#1f122f',
        'TEXT': 'White',
        'INPUT': 'White',
        'TEXT_INPUT': 'Black',
        'SCROLL': '#99CC99',
        'BUTTON': ('Black', 'White'),
        'PROGRESS': ('#D1826B', '#CC8019'),
        'BORDER': 1, 'SLIDER_DEPTH': 0, 
        'PROGRESS_DEPTH': 0, }

    sg.theme('BiblioTEC')