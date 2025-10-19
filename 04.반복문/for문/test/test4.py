#for문으로 홀수의 개수를 카운트하라
number = input('숫자를 입력하세요 : ')

total = 0

for a in range(len(number)):
    a = int(a)
    if a%2 == 1:
        total += 1
print('홀수의 개수 : %d' %total)