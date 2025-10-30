#영어 문장을 역순으로 출력(while)
sentence = input('문장을 입력해주세요 : ')

i = len(sentence) -1

while i >= 0:
    if sentence[i] == " ":
        print("-", end ='')
    else:
        print('%s' %sentence[i], end = '')
    
    i -= 1