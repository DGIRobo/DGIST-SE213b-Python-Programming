# 소수 구하기

'''
Description

함수 prime_number(number) 를 작성할 것.

함수의 동작
2부터 number 사이의 소수를 출력하시오. (소수는 1과 자기 자신만으로 나누어 떨어지는 1보다 큰 양의 정수)
매개변수
number: (int) 소수를 출력하기 위한 최대 범위 설정 값
반환값: 없음(None)
'''

'''
함수 사용예시

prime_number(2)
prime_number(20)
'''

'''
실행 결과

2
235711131719
'''

# Code

def prime_number(number):
    for numbering in range(2, number+1):
        counting = []
        for checking in range(2, number+1):
            if numbering%checking == 0:
                counting.append(checking)
        if len(counting)==1:
            print(numbering, end='')
    print('')

prime_number(2)
prime_number(20)
