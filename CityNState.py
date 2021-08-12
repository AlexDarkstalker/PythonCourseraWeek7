n = int(input())
cityState = dict()
for _ in range(n):
    line = input().split()
    for k in range(1, len(line)):
        cityState[line[k]] = line[0]
m = int(input())
for _ in range(m):
    print(cityState[input()])
