number = int(input('정수 입력: '))

if number%3 == 0 and number % 4 == 0:
  print('3의 배수이면서 4의 배수이기도 하다.')
elif number%3 == 0:
  print('3의 배수다.')
elif number%4 == 0:
  print('4의 배수다.')
else:
  print('위의 모든 조건에 만족하지 않는다.')
