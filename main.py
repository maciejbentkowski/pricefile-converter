from modules.file_import import *

TESTING_MODE_ON = True


pricefiles_directory = './'

if TESTING_MODE_ON:
    pricefiles_directory = './testing_pricefiles/'
    pricefiles_list = pricefiles_listing(pricefiles_directory)
    for file in pricefiles_list:
        if len(pricefiles_list) > 1:
            print(pricefiles_list)
            print("There are more than one pricefile in the testing_pricefiles directory. Please choose one or type 'exit' to quit")
            choose_pricefile(pricefiles_list)
            exit()
        else:
            print(file)