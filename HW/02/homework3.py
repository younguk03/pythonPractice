grade = input('등급을 입력해 주세요(A+,A,B+...F) : ')

if grade == 'A+':
    print(f'등급 : {grade}, 평점 : 4.5')
elif grade == 'A':
    print(f'등급 : {grade}, 평점 : 4.0')
elif grade == 'B+':
    print(f'등급 : {grade}, 평점 : 3.5')
elif grade == 'B':
    print(f'등급 : {grade}, 평점 : 3.0')
elif grade == 'C+':
    print(f'등급 : {grade}, 평점 : 2.5')
elif grade == 'C':
    print(f'등급 : {grade}, 평점 : 2.0')
elif grade == 'D+':
    print(f'등급 : {grade}, 평점 : 1.5')
elif grade == 'D':
    print(f'등급 : {grade}, 평점 : 1.0')
elif grade == 'F':
    print(f'등급 : {grade}, 평점 : 0')
else:
    print('잘못입력하셨습니다.')