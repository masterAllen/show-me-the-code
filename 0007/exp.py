txt = open('sample.py', 'r').read().splitlines()

comments = 0
blank_lines = 0
code_lines = 0

for line in txt:
    if not len(line):
        blank_lines += 1
        continue

    line = line.lstrip()
    if line[0]=='#':
        comments += 1
    else:
        code_lines += 1

print('comments = %d' % comments)
print('blank_lines = %d' % blank_lines)
print('code_lines = %d' % code_lines)
