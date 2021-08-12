n, k = map(int, input().split())
strikesSet = set()
for _ in range(k):
    first, interval = map(int, input().split())
    for day in range(first, n + 1, interval):
        if day % 7 not in [0, 6]:
            strikesSet.add(day)
print(len(strikesSet))
