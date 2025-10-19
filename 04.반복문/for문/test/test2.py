#for문으로 길이 환산표를 만드는 프로그램
print("-" * 40)
print(" cm  mm   m   inch")
print("-" * 40)

for cm in range(1,101):
    mm = cm * 10.0
    m = cm * 0.01
    inch = cm * 0.3937
    print('%3d  %2d  %3.2f  %2.1f' %(cm, mm, m, inch))

print("-" * 40)