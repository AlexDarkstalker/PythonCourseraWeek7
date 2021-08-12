a1, b1, a2, b2 = map(int, input().split())
fSet = set(range(min(a1, b1), max(a1, b1) + 1))
sSet = set(range(min(a2, b2), max(a2, b2) + 1))
print(len(fSet & sSet))
