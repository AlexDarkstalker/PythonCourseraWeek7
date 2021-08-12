fin = open('input.txt', encoding='utf8')
result = dict()
for line in fin:
    elem = line.split()
    name = elem[0]
    count = int(elem[1])
    if name not in result:
        result[name] = 0
    result[name] += count
for line in sorted(result):
    print(line, result[line])
