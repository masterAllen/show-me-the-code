words = []
with open('source/filtered_words.txt', 'r', encoding='utf-8', newline='') as f:
    for line in f:
        words.append(line.strip())

while True:
    # 这个strip很细节
    txt = input('input: ').strip()
    if txt in words:
        print('output: Freedom')
    else:
        print('output: HumanRights ')

