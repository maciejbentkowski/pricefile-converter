import pandas as pd
import numpy as np
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

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
        pricefile = pricefile.dropna(subset=['pn']).reset_index(drop=True)
    return pricefile

def blank_ss_while_same_as_pn(pricefile):
    if isinstance(pricefile, pd.DataFrame):
        pricefile.loc[pricefile['ss'] == pricefile['pn'], 'ss'] = ''
    return pricefile

def clear_ss_while_there_is_no_equivalent_pn(pricefile):
    pricefile.loc[~pricefile['ss'].isin(pricefile['pn']), 'ss'] = ''
    return pricefile

def delete_empty_price_rows(pricefile):
    pricefile['ss'] = pricefile['ss'].replace('', np.nan)
    pricefile = pricefile.dropna(subset=['price', 'ss'], how='all').copy()
    pricefile['ss'] = pricefile['ss'].replace(np.nan, '')
    return pricefile

def delete_string_price_rows(pricefile, no_price_word):
    pricefile = pricefile[~pricefile['price'].astype(str).str.contains(no_price_word, case=False, na=False)].reset_index(drop=True)
    return pricefile

def delete_zero_price_rows(pricefile):
    pricefile['price'] = pricefile['price'].astype(float)
    pricefile = pricefile[(pricefile['price'] != 0.0) | (pricefile['ss'] != '')].reset_index(drop=True)
    return pricefile


def remove_chain_without_price(pricefile):
    valid_pn_set = set(pricefile[pricefile['price'].notna()]['pn'])
    valid_ss_set = set(pricefile[pricefile['price'].notna()]['ss'])
    valid_pn_ss_set = valid_pn_set.union(valid_ss_set)
    pricefile = pricefile[(pricefile['pn'].isin(valid_pn_ss_set)) | (pricefile['ss'].isin(valid_pn_ss_set)) | (pricefile['price'].notna())]
    pricefile = pricefile.reset_index(drop=True)
    return pricefile

def generate_txt_file(pricefile, filename):
    pricefile['price'].fillna('', inplace=True)
    with open(filename, 'w') as file:
        write_todays_date(file)
        for _, row in pricefile.iterrows():
            pn = str(row['pn']).ljust(20)
            ss = str(row['ss']).ljust(20)
            price = str(row['price']).ljust(10)
            file.write(f"{pn}{ss}{price:>10}\n")

def write_todays_date(file):
    today = date.today()
    today = today.strftime("%d.%m.%Y")
    file.write(f'PriceL{today}'+ (" "*30) +"9,99\n")

def replace_comma_with_dot(pricefile):
    pricefile['price'] = pricefile['price'].apply(lambda x: str(x).replace(',', '.')).apply(Decimal)
    pricefile['price'] = pricefile['price'].apply(lambda x: x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    pricefile['price'] = pricefile['price'].astype(float)
    print (pricefile.head(30))
    return pricefile


