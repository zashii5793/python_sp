import pandas as pd
from glob import glob

filepaths = glob('source/*.xlsx')
filepaths
filepath = filepaths[0]
filepath

_df = pd.read_excel(filepath)
_df

columns = _df.iloc[10, [1, 2, 4, 10, 11, 14]]
columns

_df.iloc[11:23, [1, 2, 4, 10, 11, 14]]

def extract(filepath):
    _df = pd.read_excel(filepath)
    columns = _df.iloc[10, [1, 2, 4, 10, 11, 14]]
    df = _df.iloc[11:23, [1, 2, 4, 10, 11, 14]]
    df.columns = columns
    df['企業コード'] = df.iloc[3, 4]
    return df
    
df = extract(filepath)