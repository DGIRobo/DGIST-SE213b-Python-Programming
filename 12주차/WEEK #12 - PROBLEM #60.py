# 원둘레, 원넓이를 계산하는 클래스

'''
Description

사용자로부터 반지름을 입력받으면 원둘레와 원넓이를 계산하는 클래스 Circle()을 작성하시오.

단, 반지름을 입력하지 않은 경우 반지름의 기본값으로 3을 이용하도록 만드시오.

※ 원주율(PI)값은 3.14로 통일한다. (클래스 변수 사용)

set(radius) : 정수 매개변수를 받아서 현재 instance의 반지름을 radius로 설정하고 반환값은 없음

Circumference() : 매개변수는 없고 현재 instance의 반지름을 가지고 원둘레를 계산하여 반환

Circlewidth() : 매개변수는 없고 현재 instance의 반지름을 가지고 원넓이를 계산하여 반환
'''

'''
실행예시

c1 = Circle()
c2 = Circle(5)
print(c1.Circumference())
print(c1.Circlewidth())
print(c2.Circumference())
print(c2.Circlewidth())
c1.set(10)
print(c1.Circumference())
print(c1.Circlewidth())
'''

'''
실행결과

18.84
28.26
31.400000000000002
78.5
62.800000000000004
314.0
'''

# Codes
class Circle:

    PI = 3.14

    def __init__(self, radius=3): # 파라메터 수정 필요
        self._radius = radius

    def set(self, radius): # 파라메터 수정 필요
        self._radius = radius

    def Circumference(self):
        return 2*self.PI*self._radius

    def Circlewidth(self):
        return self.PI*(self._radius**2)

if __name__ == '__main__':
    c1 = Circle()
    c2 = Circle(5)
    print(c1.Circumference())
    print(c1.Circlewidth())
    print(c2.Circumference())
    print(c2.Circlewidth())
    c1.set(10)
    print(c1.Circumference())
    print(c1.Circlewidth())
