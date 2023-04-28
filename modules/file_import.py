from os import listdir
from os.path import isfile, join

TESTING_MODE_ON = True

testing_pricefiles = listdir('./testing_pricefiles/')

if TESTING_MODE_ON:
    for file in testing_pricefiles:
        print(file)
