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
