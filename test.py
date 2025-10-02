first_hour = int(input('첫번째 시간의 시를 입력하세요: '))
first_minite = int(input('첫번째 시간의 분을 입력하세요: '))
second_hour = int(input('두번째 시간의 시를 입력하세요: '))
second_minite = int(input('두번째 시간의 분을 입력하세요: '))

if first_hour>=1 and first_hour<=24 and second_hour>=1 and second_hour<=24:
  if first_minite>=0 and first_minite<60 and second_minite>=0 and second_minite<60:
    if first_hour > second_hour:
        print(f'-빠른 시간: {second_hour}:{second_minite}')
        print(f'-늦은 시간: {first_hour}:{first_minite}')
    elif first_hour == second_hour:
      if second_minite> first_minite:
        print(f'-빠른 시간: {first_hour}:{first_minite}')
        print(f'-늦은 시간: {second_hour}:{second_minite}')
      elif second_minite == first_minite:
        print('같음')
      else:
        print(f'-빠른 시간: {second_hour}:{second_minite}')
        print(f'-늦은 시간: {first_hour}:{first_minite}')
    else:
      print(f'-빠른 시간: {first_hour}:{first_minite}')
      print(f'-늦은 시간: {second_hour}:{second_minite}')
  else:
    print('분 범위를 초과했습니다.')
else:
  print('시 범위를 초과했습니다..')