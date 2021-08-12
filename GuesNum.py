fin = open('input.txt', 'r', encoding='utf8')
n = int(fin.readline())
possibleNums = set(range(1, n + 1))
line = fin.readline()
while line != 'HELP':
    curNums = set(map(int, line.split()))
    word = fin.readline().strip()
    if word == 'YES':
        possibleNums &= curNums
    else:
        possibleNums -= curNums
    line = fin.readline()
print(*possibleNums)
