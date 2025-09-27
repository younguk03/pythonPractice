print('기능 선택')
print('1. 더하기')
print('2. 빼기')
print('3. 곱하기')
print('4. 나누기 \n')

s = input('계산기 기능을 선택하세요(1/2/3/4): ')

num1 = int(input('첫번째 숫자 입력:'))
num2 = int(input('두번째 숫자 입력:'))

if s == '1':
  print(f'{num1} + {num2} = {num1 + num2}')
elif s == '2':
  print(f'{num1} - {num2} = {num1 - num2}')
elif s == '3':
  print(f'{num1} x {num2} = {num1 * num2}')
elif s == '4':
  print('%d / %d = %.1f' %(num1, num2, num1/num2))
else:
  print('잘못 선택하셨습니다.')