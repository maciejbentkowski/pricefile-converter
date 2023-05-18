from modules.pricefile_scripts_helpers import *



def ford_at_script(pricefile):
    cols = ['pn', 'ss', 'price', 'cuntry_tag']
    df = pd.read_fwf(pricefile, colspecs=([1,8], [46,53], [53,65], [30,31]),names=cols, skiprows=1)
    df = df.drop(df[df['cuntry_tag'] != 'A'].index)
    df = strange_characters_replace(df)
    df.loc[~df['ss'].isin(df['pn']), 'ss'] = ''
    df = drop_pn_null_values(df)
    #df = blank_ss_while_same_as_pn(df)
    df = delete_non_price_rows(df, no_price_word="KEIN PREIS")

    print(df)
    print("THIS IS THE FORD AT SCRIPT")
    generate_txt_file(df, 'output.txt')

def tesla_at_script(pricefile):
    print("THIS IS THE TESLA AT SCRIPT")