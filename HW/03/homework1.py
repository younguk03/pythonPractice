first_hour=int(input("첫번째 시간의 시를 입력하세요"))
first_minute=int(input("첫번째 시간의 분를 입력하세요"))
second_hour=int(input("두번째 시간의 시를 입력하세요"))
second_minute=int(input("두번째 시간의 분를 입력하세요"))

if second_hour > 23 or second_minute > 60 or second_minute < 0 or second_hour < 0 or second_hour > 23 or second_minute > 60 or second_minute < 0 or second_hour < 0:
  print("잘못입력하셨습니다.")
else:
  if first_hour < second_hour or (first_hour == second_hour and second_minute > first_minute):
    print(f"-빠른 시간: {first_hour}:{first_minute}")
    print(f"-늦은 시간: {second_hour}: {second_hour}")
  elif first_hour > second_hour or (first_hour == second_hour and second_minute < first_minute):
    print(f"-빠른 시간: {second_hour}: {second_minute}")
    print(f"-늦은 시간: {first_hour}: {first_minute}")
  else:
    print("시간이 같음")