fin = open('input.txt', encoding='utf8')
wordsCount = dict()
maxCount = 0
maxCountWord = ''
for line in fin:
    for elem in line.split():
        word = elem.strip()
        if word not in wordsCount:
            wordsCount[word] = 0
        wordsCount[word] += 1
        if wordsCount[word] > maxCount or \
                (wordsCount[word] == maxCount and word < maxCountWord):
            maxCount = wordsCount[word]
            maxCountWord = word
print(maxCountWord)
