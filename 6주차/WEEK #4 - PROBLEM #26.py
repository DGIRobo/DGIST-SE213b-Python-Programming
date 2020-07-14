# 벡터의 내적 구하기

'''
Description

다중 리스트에 있는 두 개의 벡터의 내적을 계산하는 inner_product(v1, v2)를 구현하시오.

함수동작	
두개의 벡터(v1:리스트, v2:리스트)의 길이 동일한 경우, 내적한 결과값을 반환하고 다른 경우 "can't calculate"를 반환
매개변수	
v1:(list) 연산을 원하는 벡터값이 리스트 형태로 저장
v2:(list) 연산을 원하는 벡터값이 리스트 형태로 저장
반환값	
내적한 결과값을 반환
두 벡터의 길이가 다르면 "can't calculate" 반환
'''

'''
함수 실행 예시

v1 = [1,0,1]
v2 = [1,1,1]
print(inner_product(v1, v2))
v1 = [2,1]
v2 = [-1,2]
print(inner_product(v1, v2))
v1 = [2,1]
v2 = [-1]
print(inner_product(v1, v2))
'''

'''
실행 결과 예시

2
0
can't calculate
'''

#Code

def inner_product(v1, v2):
    if len(v1) == len(v2):
        result=0
        for value in range(len(v1)):
            result+=v1[value]*v2[value]
        return result
    else:
        return "can't calculate"
    
v1 = [1,0,1]
v2 = [1,1,1]
print(inner_product(v1, v2))
v1 = [2,1]
v2 = [-1,2]
print(inner_product(v1, v2))
v1 = [2,1]
v2 = [-1]
print(inner_product(v1, v2))