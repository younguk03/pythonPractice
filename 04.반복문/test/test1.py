#while문으로 홀수의 누적 합계를 구하는 프로그램
n = 1
sum = 0
count = 0

while n <= 100:
    if n%2 == 1:
        sum = sum + n
        print("%6d" %sum , end=' ')
        count +=1
    if count % 10 == 0:
        print()
    n += 1