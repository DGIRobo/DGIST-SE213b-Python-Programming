# 오름차순 정렬하기

'''
Description

3개의 정수를 입력받아서, 오름차순 정렬하는 sorting(n1, n2, n3) 함수를 작성하세요. 단, 세 정수가 서로 같은 경우는 생각하지 않을 것. 즉, 세 정수는 모두 값이 다르다.

함수 동작
정수 3개(n1, n2, n3)를 인자로 넣어주면, 오름차순으로 숫자를 정렬한 뒤, 정렬된 순서대로 출력함
매개변수
n1: (int) 정렬하고자 하는 숫자
n2: (int) 정렬하고자 하는 숫자
n3: (int) 정렬하고자 하는 숫자
반환값: 없음(None)
'''

'''
실행예시

sorting(20, 10, 30)
10 20 30
'''

# Code
def sorting(n1, n2, n3):
    if n1>n2:
        if n1<n3:
            print(n2, n1, n3)
        if n1>n3:
            if n2>n3:
               print(n3, n2, n1)
            elif n3>n2:
               print(n2, n3, n1)
    if n1<n2:
        if n2<n3:
            print(n1, n2, n3)
        if n2>n3:
            if n3>n1:
               print(n1, n3, n2)
            elif n1>n3:
               print(n3, n1, n2)


sorting(20, 10, 30)