txt = open('sample.py', 'r').read().splitlines()

# 强行注释
comments = 0
blank_lines = 0
code_lines = 0

for line in txt:
    if not len(line):
        blank_lines += 1
        continue

            #line = line.lstrip()
    line.lstrip()
    print(line)
