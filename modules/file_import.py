from os import listdir

def pricefiles_listing(pricefiles_directory):
    print(pricefiles_directory)
    pricefile_list = []
    for file in listdir(pricefiles_directory):
        if file.endswith('.txt') or file.endswith('.csv'):
            pricefile_list.append(file)
    return pricefile_list

def choose_pricefile(pricefile_list):
    choice = input('Enter the file name: ')
    if choice in pricefile_list:
        return choice
    elif choice == 'exit':
        exit()
    else:
        print(pricefile_list)
        print('The file you have entered is not in the list above. Please try again or type "exit" to exit the program')
        choose_pricefile(pricefile_list)
