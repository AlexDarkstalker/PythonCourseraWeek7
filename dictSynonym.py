n = int(input())
words = dict()
for _ in range(n):
    wrd1, wrd2 = input().split()
    words[wrd1] = wrd2
    words[wrd2] = wrd1
print(words[input()])
