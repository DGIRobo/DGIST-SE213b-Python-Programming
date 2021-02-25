# 직사각형의 둘레 및 넓이(클래스)

'''
Description

직사각형의 가로와 세로 길이를 인스턴스 변수로 가지고, 이 직사각형의 둘레와 넓이를 구하는 인스턴스 메서드를 가지는 클래스 Rectangle()을 작성하시오.

Rectangle()
__init__(self, width, height) : width와 height를 인자로 받아 초기화 해준다. 반환값 없음.

set(self, new_width, new_height) : new_width와 new_height를 인자로 받아 기존의 width와 height 값을 갱신한다. 반환값 없음.

calcPerimeter(self) : 인스턴스 변수인 width와 height를 바탕으로 직사각형의 둘레를 계산 및 반환한다. 인자 없음. 반환값 : 직사각형의 둘레

calcArea(self) : 인스턴스 변수인 width와 height를 바탕으로 직사각형의 넓이를 계산 및 반환한다. 인자 없음. 반환값 : 직사각형의 넓이
'''

'''
함수 사용 예시

s=Rectangle(5,2)
print(s.calcPerimeter())
print(s.calcArea())
s.set(3,4)
print(s.calcPerimeter())
print(s.calcArea())
'''

'''
실행예시

14
10
14
12
'''

'''
실행결과가 예시와 동일하게 나오는 것을 확인할 것.
'''

# Codes
class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set(self, new_width, new_height):
        self._width = new_width
        self._height = new_height

    def calcPerimeter(self):
        return 2*self._width + 2*self._height

    def calcArea(self):
        return self._width*self._height

if __name__ == '__main__':
    s=Rectangle(5,2)
    print(s.calcPerimeter())
    print(s.calcArea())
    s.set(3,4)
    print(s.calcPerimeter())
    print(s.calcArea())
