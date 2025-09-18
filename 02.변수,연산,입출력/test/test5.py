price = int(input('책 값: '))
discount = int(input('할인율: '))
delivery = int(input('배송비: '))

pay = price - (price * (discount/100)) + delivery

print('\n')
print('======결과======')
print('책값: %d원' %price)
print('할인율: %d' % discount)
print('배송비: %d원' %delivery)
print('결제금액: %d원' %pay)