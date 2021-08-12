n = int(input())
possibleNums = set(range(1, n + 1))
line = input()
while line != 'HELP':
    curNums = set(map(int, line.split()))
    ySet = possibleNums & curNums
    # nSet = possibleNums - curNums
    if len(ySet) > len(possibleNums) - len(ySet):
        possibleNums = ySet
        print('YES')
    else:
        possibleNums -= curNums
        print('NO')
    line = input()
print(*sorted(list(possibleNums)))
