# 리스트의 원소에 상수배를 하는 함수 작성

'''
Description

함수 multiple_by_a_constant(t, a)를 아래와 같이 정의할 것

동작
t에 전달된 리스트에 있는 각 원소에 a를 곱해줌. 즉 t의 원소가 변화함.
인자
t : (list)임의의 값을 원소로 포함하는 리스트
a : (int)리스트의 원소를 곱하기 혹은 반복할 회수
반환값
(list) 전달받은 리스트, 즉 함수 내부에서 값이 변경한 리스트를 반환
'''

'''
함수 사용 예시

t = [42, 1024, 23]
multiply_by_a_constant(t, 2)
print(t)
multiply_by_a_constant(t, 10)
print(t)
multiply_by_a_constant(t, 0.5)
print(t)
s = ['i', 'love', 'python']
multiply_by_a_constant(s, 2)
print(s)
'''

'''
실행 결과

[84, 2048, 46]
[840, 20480, 460]
[420.0, 10240.0, 230.0]
['ii', 'lovelove', 'pythonpython']
'''

# Code

def multiply_by_a_constant(t, a):
    for value in range(len(t)):
        t[value]=t[value]*a
    return t

t = [42, 1024, 23]
multiply_by_a_constant(t, 2)
print(t)
multiply_by_a_constant(t, 10)
print(t)
multiply_by_a_constant(t, 0.5)
print(t)
s = ['i', 'love', 'python']
multiply_by_a_constant(s, 2)
print(s)