import random
attacks = ['ストローク', 'ボレー', 'スマッシュ', 'ロブ']
for count in range(5):
    print(random.choice(attacks))

sound = {
    'A' : 'a',
    'B' : 'b',
    'C' : 'c',
    'D' : 'd',
    'E' : 'e',
    'F' : 'f',
}
for key, value in sound.items():
    print(key, value)
