n1 = int(input())
n2 = int(input())
max_num = {}

for i in range(n1, n2+1):
    a = 0
    if i %2 == 0:
        continue
    while True:
        a += 1
        if i%2 == 0:
            i = i//2
        else:
            i = i*3 + 1
        if i == 1:
            max_num[a] = i
            break

# 10, 5, 16, 8, 4, 2, 1