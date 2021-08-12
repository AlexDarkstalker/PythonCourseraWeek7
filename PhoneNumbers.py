def toDigitNumber(number):
    digNum = list(''.join(filter(lambda x: x.isdigit(), number)))
    if len(digNum) == 7:
        digNum.insert(0, '7')
        digNum.insert(1, '4')
        digNum.insert(2, '9')
        digNum.insert(3, '5')
    if digNum[0] in ['7', '8']:
        digNum.pop(0)
    return ''.join(digNum)


number = input()
digNum = toDigitNumber(number)
for i in range(3):
    curNum = toDigitNumber(input())
    if digNum == curNum:
        print('YES')
    else:
        print('NO')
