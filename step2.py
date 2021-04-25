import os.path

with open('data/local/dict/phones.txt', 'w') as phones, open('data/local/dict/lexicon.txt', 'w') as lexicon:
    phones.write("Y\nN\n")
    lexicon.write("YES Y\nNO N\n")
