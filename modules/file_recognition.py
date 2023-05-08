from modules.pricefile_scripts import *
import os


def script_choice(pricefiles_directory, filename):
    filedir = str(pricefiles_directory) + str(filename)
    if filename.endswith('.txt') and 'ford' in filename:
        print(filename)
        print(filedir)
        ford_at_script(filedir)
    elif filename.endswith('.csv') and 'tesla' in filename:
        tesla_at_script(filedir)
    else:
        print('Invalid file format or filename')
        exit()