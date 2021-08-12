numList = list(map(int, input().split()))
numSet = set()
for elem in numList:
    if elem in numSet:
        print('YES')
    else:
        print('NO')
    numSet.add(elem)
