import pandas as pd

def open_pricefile(pricefile, pn, ss, price):
    cols = ['pn', 'ss', 'price']
    df = pd.read_fwf(pricefile, widths=[8, 8, 12], names=cols, skiprows=1)
    return df


def strange_characters_replace(pricefile):
    strange_characters_dictionary= {
        ')': '',
        '(': '',
        'a': 'A',
        'А': 'A',
        'б': 'B',
        'b': 'B',
        'в': 'B',
        'с': 'C',
        'C': 'C',
        'д': 'D',
        'Д': 'D',
        'd': 'D',
        'E': 'E',
        'э': 'E',
        'е': 'E',
        'f': 'F',
        'ф': 'F',
        'H': 'H',
        'н': 'H',
        'к': 'K',
        'k': 'K',
        'К': 'K',
        'р': 'P',
        'Р': 'P',
        'п': 'P',
        'П': 'P',
        'т': 'T',
        'Т': 'T',
        't': 'T',
        '0': '0',
        'g': 'G',
        'и': 'I',
        'j': 'J',
        'l': 'L',
        'м': 'M',
        'М': 'M',
        'n': 'N',
        'о': 'O',
        'О': 'O',
        'q': 'Q',
        'л': 'L',
        'y': 'Y',
        'У': 'Y',
        'u': 'U',
        'Г': 'G',
        'Ч': 'C',
        'Ш': 'Z',
        'З': 'Z',
        'Ж': 'Z',
        'Ą': 'A',
        'Ć': 'C',
        'Ź': 'Z',
        'Ę': 'E',
        'Ń': 'N',
        ';': '.',
        "'": '.',
        '+': '-'

    }

