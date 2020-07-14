# MyCounter (이론수업 예제)

'''
Description

주의: 인스턴스 함수의 첫 번째 인자인 self는 파이썬이 자동으로 그 값을 전달해주기 때문에, 즉 이 함수를 사용할 때 인자를 넘겨줄 필요가 없기 때문에, 함수 사용법에 별도로 표시하지 않는 경우가 많다. (파이썬 공식 문서 등에서도 self는 생략하고 설명하는 경우가 대부분이다.) 함수를 구현할 때는, 첫 번째 인자인 self를 추가해주어야 한다. (아래 코드를 참고할 것)

dec() : 매개변수는 없고 intance variable counter를 1 감소시키고 반환값은 없음

set(value) : 매개변수(value)를 받아서 intance variable counter에 value의 값을 대입하고 반환값은 없음
'''

'''
참고 아래 클래스를 확장하여 사용할 것

class MyCounter():
    n=0
    def __init__(self, value=0):
        self.counter = value
        MyCounter.n += 1

    def inc(self):
        self.counter += 1

    def get(self):
        return self.counter
'''

'''
함수 사용 예시

c1 = MyCounter()
c2 = MyCounter(42)
print(MyCounter.n)
print(c1.get(), c2.get())
c1.inc()
c1.inc()
c2.dec()
print(c1.get(), c2.get())
c1.set(23)
c2.set(1024)
print(c1.get(), c2.get())
'''

'''
실행예시

2
0 42
2 41
23 1024
'''
# Codes
class MyCounter():
    """Simple Counter class"""
    n = 0

    def __init__(self, value=0):
        """Initialize counter with given value or default value (0)"""
        self.counter = value
        MyCounter.n += 1

    def get(self):
        """Return the value of counter"""
        return self.counter

    def set(self, value):
        """Set the counter with the given value"""
        self.counter = value

    def inc(self):
        """Increase counter by 1"""
        self.counter += 1

    def dec(self):
        """Decrease counter by 1"""
        self.counter -= 1

if __name__ == '__main__':
    c1 = MyCounter()
    c2 = MyCounter(42)
    print(MyCounter.n)
    print(c1.get(), c2.get())
    c1.inc()
    c1.inc()
    c2.dec()
    print(c1.get(), c2.get())
    c1.set(23)
    c2.set(1024)
    print(c1.get(), c2.get())
