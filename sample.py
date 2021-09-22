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