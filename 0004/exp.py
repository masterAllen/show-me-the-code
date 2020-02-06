import re

dic = {}
lastflag = False

# 1. Python 文件读写
txt = open('sample.txt', 'r').read().splitlines()
for line in txt:
    if not len(line):
        continue

    if lastflag:
        line = lastword + line
        lastflag = False
        
    lastflag = (line[-1]=='-')

    line = re.sub(r'[.;?!,]',' ',line)
    line = re.sub(r'-',' ',line)

    wordlist = line.split()

    if lastflag:
        lastword = wordlist[-1]
        del wordlist[-1]

    for word in wordlist:
        dic.setdefault(word,0)
        dic[word] += 1

print(dic)
