fin = open('input.txt', encoding='utf8')
words = dict()
result = []
for line in fin:
    for elem in line.split():
        word = elem.strip()
        if word not in words:
            words[word] = 0
        words[word] += 1
for elem in words:
    result.append((words[elem], elem))
result.sort(key=lambda x: (-x[0], x[1]))
for elem in result:
    print(elem[1])
