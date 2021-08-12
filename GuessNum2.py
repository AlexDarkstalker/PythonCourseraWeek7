n = int(input())
possibleNums = set(range(1, n + 1))
line = input()
while line != 'HELP':
    curNums = set(map(int, line.split()))
    word = input().strip()
    if word == 'YES':
        possibleNums &= curNums
    else:
        possibleNums -= curNums
    line = input()
print(*sorted(list(possibleNums)))
