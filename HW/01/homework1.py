#원의 둘레와 면적을 구하여라
'''
원의 둘레 : 2 x 반지름 x 3.14
원의 면적 : 반지름 x 반지름 x 3.14
'''

r = float(input('반지름은? '))    #반지름 입렵받아 실수 변환

length = 2 * r * 3.14            #원의 둘레
area = (r**2) * 3.14             #원의 면적

print('반지름 : %.2f cm' %r)
print("원의 둘레 : %.2f cm" %length)
print("원의 면적 : %.2f cm2" %area)