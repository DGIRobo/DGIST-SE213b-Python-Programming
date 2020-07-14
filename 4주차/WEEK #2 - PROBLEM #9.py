#온도 변환 2
'''
Description
섭씨에서 화씨, 혹은 그 반대로 온도 변환을 하는 프로그램을 작성하시오.

먼저 온도(실수의 값을 처리할 수 있어야 함), 그리고 그 온도의 종류를 입력받고('c' 혹은 'C'를 입력하면 섭씨, 'f' 또는 'F'를 입력하면 화씨), 섭씨이면 화씨로 아니면 반대로 변경하는 프로그램을 작성하시오.

온도의 종류에 대한 입력값이 정확하지 않은 경우, 문자열 'Error in the kind of temperature scale!'을 출력하시오.

주의: 대소문자 모두 처리되도록 할 것. 그리고 입력받는 온도의 종류는 입력받은 온도가 섭씨 혹은 화씨임을 의미함.
'''

'''
실행예시 1
Enter a degree: 10
Enter the kind of temperature scale: c
50.0
'''

'''
실행예시 2
Enter a degree: 50
Enter the kind of temperature scale: F
10.0
'''

'''
실행예시 3
Enter a degree: 10
Enter the kind of temperature scale: cc
Error in the kind of temperature scale!
'''

# Code
degree = float(input('Enter a degree: '))
scale = input('Enter the kind of temperature scale: ')

if (scale == 'C') or (scale == 'c'):
    Fahrenheit = degree*9/5+32
    print(Fahrenheit)
elif (scale == 'F') or (scale == 'f'):
    Celsius = (degree-32)*5/9
    print(Celsius)
else:
    print('Error in the kind of temperature scale!')