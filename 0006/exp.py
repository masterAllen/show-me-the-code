from pathlib import Path, PosixPath
import re

srcpath = Path('sample')
file_list = list(srcpath.glob('*'))

dic = {}

for filename in file_list:
    txt = open(filename, 'r').read().splitlines()
    lastflag = False

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
