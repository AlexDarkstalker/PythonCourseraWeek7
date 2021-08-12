fin = open('input.txt', encoding='utf8')
result = []
words = dict()
for line in fin:
    for elem in line.split():
        word = elem.strip()
        if word not in words:
            words[word] = 0
        result.append(words[word])
        words[word] += 1
print(*result)
