file = open(
    'random.txt',
    'r',
    encoding= 'utf-8'
)
data = file.read()
file.close()
lines = data.split('¥n')
for line in lines:
    print(line)
