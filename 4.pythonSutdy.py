print('身長(ｃｍ)は?')
height = 175
bmi = 22
weight = bmi * (height / 100) ** 2
print('身長が' + str(height) + 'cmの場合の標準体重は', end= '')
print('{:.2f}kgです。'.format(weight))
