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

class Person:
  __nationality = 'Japan'

  def __init__(self, name):
      self.name = name

  def say_hello(self):
    print(f'あああ {self.nationality}です。')
  def sya_nema(self):
    print(f'あああ {self.name}っす。')

person = Person('aa')
person.sya_nema()
person.


import pandas as pd
from glob import glob
filepaths_order = glob('sources/order_new/order*.xlsx')
filepaths_order
filepath = filepaths_order[0]

df_order = pd.read_excel(filepath)
df_order.to_dict().items()
from collections import defaultdict
order = defaultdict(int)

for key, value in df_order.to_dict().items():
    order[key] += value[0]
#    print(key, value[0])
order


#tabula PDF⇒表を出力

!pip install tabula-py

import tabula

pdf_path = 'pdfのurlを記入'
dfs = tabula.read_pdf(pdf_path, stream=True, pages= 'all')
dfs（０）
