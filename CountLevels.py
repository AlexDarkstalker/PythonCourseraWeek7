n = int(input())
relativesTree = dict()
parentLevel = dict()
result = []
for _ in range(n - 1):
    child, parent = input().split()
    relativesTree[child] = parent
for elem in relativesTree:
    curParent = relativesTree[elem]
    if curParent in parentLevel:
        parentLevel[elem] = parentLevel[curParent] + 1
    else:
        level = 0
        while curParent in relativesTree:
            curParent = relativesTree[curParent]
            level += 1
        parentLevel[relativesTree[elem]] = level
        parentLevel[elem] = level + 1
for elem in sorted(parentLevel):
    print(elem, parentLevel[elem])
