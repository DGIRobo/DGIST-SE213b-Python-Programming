# 문자열 삼각형

'''
Description

문자열 삼각형을 출력하는 print_pyramid(n)을 만드시오.

함수의 동작
문자열 삼각형은 n줄만큼 출력하면서, 각 줄에 '*' 를 1, 2, ..., n개씩 출력할 것
매개변수
n: (int) 출력할 줄 수
반환값: 없음(None)
'''

'''
함수사용예시

print('First pyramid')
print_pyramid(5)
print('Second pyramid')
print_pyramid(3)
'''

'''
실행 결과

First pyramid
*
**
***
****
*****
Second pyramid
*
**
***
'''

#Code

def print_pyramid(n):
    for row in range(n):
        for column in range(row+1):
            print('*', end='')
        print('')

print('First pyramid')
print_pyramid(5)
print('Second pyramid')
print_pyramid(3)