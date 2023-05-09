

def open_pricefile(pricefile):
    with open(pricefile, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
