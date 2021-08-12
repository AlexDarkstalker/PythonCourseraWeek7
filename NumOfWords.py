fin = open('input.txt', 'r', encoding='utf8')
words = fin.readlines()
wSet = set()
for elem in words:
    for word in elem.split():
        wSet.add(word)
print(len(wSet))
