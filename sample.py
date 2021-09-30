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


#tabula PDF⇒表を出力

!pip install tabula-py

import tabula
tabula.environment_info()

pdf_path = 'file:///Users/user/Desktop/09_%E5%A5%91%E7%B4%84%E6%B3%95%E5%8B%99%E3%83%8A%E3%83%AC%E3%83%83%E3%82%B7%E3%82%99%E3%83%9E%E3%83%8D%E3%82%B7%E3%82%99%E3%83%A1%E3%83%B3%E3%83%88%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%81%B2%E3%81%AA%E5%9E%8B%E4%BD%9C%E6%88%90%E3%82%AB%E3%82%99%E3%82%A4%E3%83%88%E3%82%99.pdf'
dfs = tabula.read_pdf(pdf_path, stream=True, pages= 'all')
print(len(dfs))
dfs（０）
