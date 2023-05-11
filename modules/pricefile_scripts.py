from modules.pricefile_scripts_helpers import *



def ford_at_script(pricefile):
    cols = ['pn', 'ss', 'price', 'cuntry_tag']
    df = pd.read_fwf(pricefile, colspecs=([1,8], [46,53], [53,65], [30,31]),names=cols, skiprows=1)
    df = df.drop(df[df['cuntry_tag'] != 'A'].index)
    #df[df['ss'].str.isdecimal().fillna(False)] = df['ss'] = 'Nope'
    df['ss'] = df['ss'].apply(lambda x: '' if pd.isna(pd.to_numeric(x, errors='coerce')) else x)
    #print(df.to_string())
    print(df)
    print("THIS IS THE FORD AT SCRIPT")


def tesla_at_script(pricefile):
    print("THIS IS THE TESLA AT SCRIPT")