from os import listdir
def ford_at_script(pricefile):
    with open(pricefile, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
    print("THIS IS THE FORD AT SCRIPT")


def tesla_at_script(pricefile):
    for line in listdir(pricefile):
        print(line)
    print("THIS IS THE TESLA AT SCRIPT")