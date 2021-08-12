fin = open('input.txt', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
nameResult = dict()
count = 0
countMax = 0
countSecond = 0
winner = ''
second = ''
for line in fin:
    name = line.strip()
    count += 1
    if name not in nameResult:
        nameResult[name] = 0
    nameResult[name] += 1
    if nameResult[name] > countMax:
        if countMax >= countSecond and len(nameResult) > 1 and name != winner:
            countSecond = countMax
            second = winner
        winner = name
        countMax = nameResult[name]
    if nameResult[name] > countSecond and name != winner:
        second = name
        countSecond = nameResult[name]
if countMax / count > 0.5:
    print(winner, file=fout)
else:
    print(winner, file=fout)
    print(second, file=fout)
