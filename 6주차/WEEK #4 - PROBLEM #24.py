# 리스트 두 개의 각각의 원소의 합을 구하는 함수

'''
Description
함수 add(t1, t2)를 아래와 같이 작성하시오.

함수동작	t1과 t2의 같은 인덱스의 데이터를 더해서 만든 리스트를 반환함
매개변수	
t1: (list) 원수의 합을 구하고자 하는 리스트
t2: (list) 원수의 합을 구하고자 하는 리스트
반환값	
t1와 t2의 원소의 개수가 같은 경우:
    -  새로운 리스트를 만들고, 각각 원소의 합을 저장하고 리스트를 반환
    -  t1과 t2의 원소는 변화하지 않음
t1와 t2의 원소의 개수가 다른 경우: None을 반환
'''

'''
함수 사용 예시

t1 = [42, 1024, 23]
t2 = [6, 28, 496]
t3 = add(t1, t2)
print(t1)
print(t2)
print(t3)
t4 = add(t2, t2)
print(t2)
print(t4)
t5 = add(t1, [1])
print(t5)
print(add([], []))
'''

'''
실행 결과

[42, 1024, 23]
[6, 28, 496]
[48, 1052, 519]
[6, 28, 496]
[12, 56, 992]
None
[]
'''

# Code

def add(t1, t2):
    """Return a new list with element-wise sum of t1 and t2"""
    if len(t1) == len(t2):
        new_list=[]
        for value in range(len(t1)):
                new_list.append(t1[value]+t2[value])
        return new_list
    else:
        return None


t1=[42, 1024, 23]
t2 = [6, 28, 496]
t3 = add(t1, t2)
print(t1)
print(t2)
print(t3)
t4 = add(t2, t2)
print(t2)
print(t4)
t5 = add(t1, [1])
print(t5)
print(add([], []))
