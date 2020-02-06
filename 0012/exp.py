import re

word_list = []
reword_list = []
with open('source/filtered_words.txt', 'r') as f:
    for line in f:
        word_list.append(line.strip())
        # 1. 查找字符串是否有中文
        if len(re.findall(u"[\u4e00-\u9fa5]+", line.strip())) > 0:
            reword_list.append('**')
        else:
            reword_list.append('*')

# 2. 基本输入输出
while True:
    txt = input('input: ')
    for word, reword in zip(word_list, reword_list):
        txt = txt.replace(word, reword)
    print('output: ' + txt)

