import pandas as pd

def strange_characters_replace(pricefile):
    strange_characters_dictionary = {
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
    if isinstance(pricefile, pd.DataFrame):
        pricefile['pn'] = pricefile['pn'].str.translate(str.maketrans(strange_characters_dictionary))
        pricefile['ss'] = pricefile['ss'].str.translate(str.maketrans(strange_characters_dictionary))

    return pricefile


def drop_pn_null_values(pricefile):
    if isinstance(pricefile, pd.DataFrame):
        pricefile = pricefile.dropna(subset=['pn'])
    return pricefile

def blank_ss_while_same_as_pn(pricefile):
    if isinstance(pricefile, pd.DataFrame):
        pricefile.loc[pricefile['ss'] == pricefile['pn'], 'ss'] = ''
    return pricefile

def delete_non_price_rows(pricefile, no_price_word):
    pricefile = pricefile.dropna(subset=['price', 'ss'], how='all').copy()
    pricefile = pricefile[~pricefile['price'].str.contains(no_price_word, case=False, na=False)]
    pricefile = pricefile[pricefile['price'] != 0]
    return pricefile

def generate_txt_file(pricefile, filename):
    with open(filename, 'w') as file:
        for _, row in pricefile.iterrows():
            pn = str(row['pn']).ljust(20)
            ss = str(row['ss']).ljust(20)
            price = float(row['price'])
            file.write(f"{pn}{ss}{price:>10.2f}\n")