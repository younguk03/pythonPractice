#영어 소문자 또는 대문자의 자음/모음을 판별하는 프로그램

char1 = input('영어 대문자 또는 영어 소문자 하나를 입력하세요')
char2 = char1.upper()   #upper()은 소문자를 대문자로 변환해주는 함수다

if char2 == 'A' or char2 == 'E' or char2 == 'O' or char2 == 'U':
    print(f'{char2} -> 모음')
else :
    print(f'{char2} -> 자음')
