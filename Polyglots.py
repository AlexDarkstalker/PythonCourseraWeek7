n = int(input())
allSet = set()
oneSet = set()
curSet = set()
for i in range(n):
    curSet.clear()
    m = int(input())
    for _ in range(m):
        curSet.add(input())
    if i == 0:
        for elem in curSet:
            allSet.add(elem)
    allSet &= curSet
    oneSet |= curSet
print(len(allSet))
for elem in allSet:
    print(elem)
print(len(oneSet))
for elem in oneSet:
    print(elem)
