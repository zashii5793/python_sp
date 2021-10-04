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
