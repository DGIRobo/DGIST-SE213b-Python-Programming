# 화씨, 섭씨 변환 함수 작성
'''
Description

함수 convert_temperature(degree, degree_type) 함수를 작성하시오.

함수 동작
온도(degree)와 degree_type을 인자로 받아서 degree_type이 'c' 또는 'C' 인 경우에 온도를 화씨로 변형하여 반환하고 'f' 또는 'F'인 경우에는 섭씨로 변환하여 반환하는 함수
매개변수
degree: (int or float) 온도를 입력받는다.
degree_type: (str - default값은 'c') 온도가 섭씨인지, 화씨인지를 구분한다
'c' or 'C': degree가 섭씨를 뜻함
'f' or 'F': degree가 화씨를 뜻함
반환값: (float) 온도를 변환된 값을 float으로 반환한다
degree_type이 'c' or 'C'인 경우: degree를 섭씨로 가정하고, 이것을 화씨로 변환하여 출력
degree_type이 'f' or 'F'인 경우: degree를 화씨로 가정하고, 이것을 섭씨로 변환하여 출력
degree_type이 위의 값들 중 하나가 아니면 None을 반환
참고: 아무 것도 return하지 않거나 return None이라고 하면 None이 반환값으로 사용된다.
'''

'''
함수 사용예시

print(convert_temperature(10, 'c'))
print(convert_temperature(10))
print(convert_temperature(50, 'F'))
print(convert_temperature(50, 't'))
'''

'''
실행결과

50.0
50.0
10.0
None
'''

#Code
def convert_temperature(degree, degree_type='c'):
    if (degree_type == 'C') or (degree_type == 'c'):
        Fahrenheit = float(degree)*9/5+32
        return Fahrenheit
    elif (degree_type == 'F') or (degree_type == 'f'):
        Celsius = (float(degree)-32)*5/9
        return Celsius
    else:
        return None

print(convert_temperature(10, 'c'))
print(convert_temperature(10))
print(convert_temperature(50, 'F'))
print(convert_temperature(50, 't'))
print(convert_temperature(100, 'c'))
