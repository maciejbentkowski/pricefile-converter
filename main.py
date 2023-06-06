from modules.file_import import *
from modules.file_recognition import *

#TURN ON TESTING MODE TO USE THE TESTING_PRICEFILES DIRECTORY
TESTING_MODE_ON = False

if TESTING_MODE_ON:
    pricefiles_directory = './testing_pricefiles/'
else:
    pricefiles_directory = './pricefiles/'

pricefiles_list = pricefiles_listing(pricefiles_directory)
for file in pricefiles_list:
    if len(pricefiles_list) > 1:
        print(pricefiles_list)
        print("There are more than one pricefile in the testing_pricefiles directory. Please choose one or type 'exit' to quit")
        choice = choose_pricefile(pricefiles_list)
        print(choice)
        script_choice(pricefiles_directory, choice)
        exit()
    else:
        print(file)
