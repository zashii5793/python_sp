dictionary = {
    'A': 'あ',
    'B': 'い',
    'C': 'う',
    'D': 'え',
}
print(dictionary.get('D'))


lasts = ['A','B']
firsts = ['C','D']
for last, first in zip(lasts, firsts):
    print(last+first)   


lasts = ['A','B']

for i, last in enumerate(lasts) :
  print(f'{i}番目の{last}です')

num = 0
try :
  print(f' 計算結果: {10/num}')
except ZeroDivisionError  as e:
  print(e)

file = open('sample.txt')
text = file.read()
file.close()

with open('sample.txt', 'r') as f:
  txt = f.read()
print(x)


import os

for curDir, dirs, files in os.walk('.'):
  for file in files:
    print(f'{curDir}/{file}')


import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

data = np.random.randint(0, 50, size=(2, 100))    

import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

data = np.random.randint(0, 100, size=(50, 2))
plt.plot(data)
plt.savefig('sample.png')


import pandas as pd
from fbprophet import Prophet
_df = pd.read_csv('https://www.tepco.co.jp/forecast/html/images/juyo-2017.csv', encoding='shift-jis', skiprows=1)
_df.head()
_df.shape

years = [2017, 2018, 2019]
year = years[0]
df = pd.DataFrame()
for year in years:
    _df = pd.read_csv(f'https://www.tepco.co.jp/forecast/html/images/juyo-{year}.csv', encoding='shift-jis', skiprows=1)
    df = pd.concat([df, _df], axis=0)
