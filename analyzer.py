from janome.tokenizer import Tokenizer
t = Tokenizer()
tokens = t.tokenize('わたしはPythonのプログラムです')
print(tokens[0].surface)
