num = input('수 입력: ')

if len(num) == 1:
  print(f'{num}은 한자리 숫자다.')
elif len(num) == 2:
  print(f'{num}은 두자리 숫자다.')
elif len(num) == 3:
  print(f'{num}은 세자리 숫자다.')
else:
  print(f'오류! {num}은 범위(0~999) 이외의 숫자다.')