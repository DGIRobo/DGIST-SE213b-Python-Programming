'''
Description
사용자에게 섭씨온도를 입력받아, 이것을 화씨온도로 출력하는 프로그램을 작성할 것. 섭씨 온도
(C)를 화씨온도(F)로 변경하는 수식은 아래와 같다.
F = C*(9/5)+32
'''

'''
실행예시
Enter a degree: 10
50.0
'''

Celsius = float(input('Enter a degree: '))
Fahrenheit = Celsius*9/5+32
print(Fahrenheit)