userid = input('아이디')

if userid =='admin':
  print('콘텐츠 이용이 가능합니다.')
else:
  level = int(input('회원 레벨은? '))
  if level >0 and level < 4:
    print('콘텐츠 이용이 가능합니다')
  else:
    print('콘텐츠 이용이 불가능합니다.')