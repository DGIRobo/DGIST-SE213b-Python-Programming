# 원의 둘레와 넓이를 구하는 함수

'''
Description

원의 둘레와 넓이를 구하는 함수 1. circumference(radius)와 2. area(radius)를 각각 구현하시오.

주의: 원주율의 값으로 math.pi 값을 사용할 것. 즉 math 패키지를 import하여 사용할 것

그리고 반지름 1-3개를 입력받아, 그 반지름을 가지는 원의 넓이의 합을 반환하는 함수 3. sum_of_areas(radius1, radius2, radius3)를 구현할 것. radius2와 radius3는 생략가능함. 인자가 생략된 경우, 그 인자에 대한 원의 넓이를 구할 필요는 없음.

주의

원의 넓이를 구하기 위한 표현식을 따로 만들지 말고 area() 함수를 이용할 것.
힌트: 기본값을 사용할 것. 그리고 기본값을 어떻게 지정하면 함수의 구현이 가장 간단한지 생각해볼 것.
1. circumference(radius) 함수
함수 동작
반지름(radius)를 인자로 받아서 원의 둘레를 반환함.
매개변수
radius: (float) 원의 반지름
반환값: (float) radius로 계산한 원의 둘레
2. area(radius) 함수
함수 동작
반지름(radius)를 인자로 받아서 원의 넓이를 반환함.
매개변수
radius: (float) 원의 반지름
반환값: (float) radius로 계산한 원의 넓이
3. sum_of_areas(radius1, radius2, radius3) 함수
함수 동작
반지름을 3개(radius1, radius2, radius3)를 입력 받아서 각각의 넒이를 구한뒤 이를 더한 값을 반환함.
주의: 반지름 중 radius2, radius3은 생략이 가능하다.
매개변수
radius1: (float) 첫번째 원의 반지름
radius2: (float) 두번째 원의 반지름
radius3: (float) 세번째 원의 반지름
반환값: (float) 3개 또는 2개 또는 1개의 반지름이 들어온 경우, 각각 원의 넒이를 계산하여 더한 값을 반환
'''

'''
함수 사용 예시

r = 1.0
print(circumference(r), area(r))
r = 3.0
print(circumference(r), area(r))
print(sum_of_areas(1, 2, 3))
print(sum_of_areas(1))
'''

'''
실행결과

6.283185307179586 3.141592653589793
18.84955592153876 28.274333882308138
43.982297150257104
3.141592653589793
'''

# Code
import math

def circumference(radius):
    length = float(2*math.pi*radius)
    return length

def area(radius):
    surface = float(math.pi*radius**2)
    return surface

def sum_of_areas(radius1, radius2=0, radius3=0):
    surface1 = float(math.pi*radius1**2)
    surface2 = float(math.pi*radius2**2)
    surface3 = float(math.pi*radius3**2)
    return surface1+surface2+surface3

r = 1.0
print(circumference(r), area(r))
r = 3.0
print(circumference(r), area(r))
print(sum_of_areas(1, 2, 3))
print(sum_of_areas(1))
