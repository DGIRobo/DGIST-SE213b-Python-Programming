# hypotenuse of right angled triangle

'''
Description
직각 삼각형 빗변을 제외한 한 변의 길이와 그 끼인각을 알면, 빗변의 길이를 구할 수 있다. 사용자로 부터 한변의 길이와 각도를 입력 받아 빗변의 길이를 계산하는 프로그램을 작성하시오.

삼각형 ABC가 있고, 변AB의 길이가 c, 변BC의 길이가 a, 변 AC의 길이가 b이다.

* 주의: 삼각함수를 사용하기 위해서 math 모듈을 사용하시오.

https://docs.python.org/ko/3/library/math.html
math.cos( input_radian )
math.radians( input_degree ) # 입력받은 degree를 radian으로 변경하는 함수
한변의 길이가 0 또는 음수인 경우, Incorrect input. 을 출력하시오.
끼인 각이 0도 보다 크지 않거나 90도 보다 작지 않은 경우, Incorrect input. 을 출력하시오.
'''

'''
실행예시 1
Enter the length of a side(b) of the right triangle: 1
Enter the degree of the angle(BAC): 45
1.414213562373095
'''

'''
실행예시 2
Enter the length of a side(b) of the right triangle: 1
Enter the degree of the angle(BAC): 100
Incorrect input.
'''

'''
실행예시 3
Enter the length of a side(b) of the right triangle: -1
Enter the degree of the angle(BAC): 100
Incorrect input.
'''

# Code
import math
b = float(input('Enter the length of a side(b) of the right triangle: '))
BAC = float(input('Enter the degree of the angle(BAC): '))
if (b<=0) or (BAC<0) or (BAC>=90):
    print('Incorrect input.')
else:
    print(b/math.cos(BAC*(math.pi)/180))
