#할인율에 따라 지불 금액을 계산하라!
'''
10,000 ~ 50,000원 => 5%할인
50,001 ~ 300,000원 => 7.5%할인
300,001원 이상 : 10%할인
10,000원 미만 => 0%
'''

spend = int(input("구매 금액 : "))

if spend >= 10000 and spend <= 50000:
    rate = 5.0
elif spend > 10000 and spend <= 300000:
    rate = 7.5
elif spend > 300000:
    rate = 10.0
else :
    rate = 0

discount = spend / 100 * rate
pay = spend - discount

print(f"구매 금액 : {spend}")
print("할인율 : %.1f" %rate)
print("할인 금액 : %.0f원" %discount)
print("지불 금액 : %.0f원" %pay)