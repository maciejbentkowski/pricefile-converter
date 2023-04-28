from os import listdir

TESTING_MODE_ON = True

testing_pricefiles = listdir('./testing_pricefiles/')

pricefiles_csv = []
pricefiles_txt = []

def pricefiles_listing():
    pricefiles = listdir('./testing_pricefiles/')
    pricefile_list = []
    for file in pricefiles:
        if file.endswith('.txt') or file.endswith('.csv'):
            pricefile_list.append(file)
    print(pricefile_list)
    return pricefile_list

def choose_pricefile():
    pricefile_list = pricefiles_listing()
    print('Choose a pricefile from the list above')
    choice = input('Enter the file name: ')
    if choice in pricefile_list:
        return choice
    else:
        print('The file you have entered is not in the list above. Please try again')
        choose_pricefile()

if TESTING_MODE_ON:
    pricefile_list = pricefiles_listing()
    for file in pricefile_list:
        if len(testing_pricefiles) > 1:
            print('There are more than one pricefile in the testing_pricefiles directory. Please choose one')
            choose_pricefile()
            
            exit()
        else:
            print(file)
