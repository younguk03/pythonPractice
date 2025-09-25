start = int(input('시작수: '))
end = int(input('끝 수: '))
num = int(input('정수 입력: '))

result = '%d는 %d~%d 사이에 없다.' %(num, start,end)

if start <= num and end >= num:
  result = '%d는 %d~%d 사이에 있다.' %(num, start, end)

print(result)