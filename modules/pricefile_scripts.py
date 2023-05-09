from modules.pricefile_scripts_helpers import *



def ford_at_script(pricefile):
    data = open_pricefile(pricefile, delete_first_line=True)
    print(data)
    print("THIS IS THE FORD AT SCRIPT")


def tesla_at_script(pricefile):
    open_pricefile(pricefile)
    print("THIS IS THE TESLA AT SCRIPT")