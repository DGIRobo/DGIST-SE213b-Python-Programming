# 지역 변수, 클래스 변수, 객체 변수 구분해 보기

'''
Description
다음 예에서는 지역 변수, 클래스 변수, 객체 변수가 모두 사용되어 있다. Python Tutor를 사용하여, 한 줄씩 실행해보고, 각각의 변수가 언제/어떻게 변경되는지 확인해보시오.
어떤 변수가 지역 변수, 클래스 변수, 객체 변수인가?

class MyCounter():
    """Simple Counter class"""
    # Is n a class variable or an instance variable?
    n = 0

    def __init__(self, value=0):
        """Initialize counter with given value or default value (0)"""
        # What is the difference between 'self.counter' and 'counter'?
        self.counter = value
        counter = value
        MyCounter.n += 1

    def get(self):
        """Return the value of counter"""
        return self.counter

    def inc(self):
        """Increase counter by 1"""
        self.counter += 1
        # What is the scope of local_variable?
        local_variable = self.counter
        local_variable += 100

print(MyCounter.n)
c1 = MyCounter()
print(MyCounter.n, c1.get())
c2 = MyCounter(42)
print(MyCounter.n, c1.get())
print(MyCounter.n, c1.get())
c1.inc()
print(MyCounter.n, c1.get())
print(MyCounter.n, c1.get())
c1.inc()
print(MyCounter.n, c1.get())
print(MyCounter.n, c1.get())
c2.inc()
print(MyCounter.n, c1.get())
print(MyCounter.n, c1.get())
'''

#Code
class MyCounter():
    """Simple Counter class"""
    # Is n a class variable or an instance variable?
    n = 0

    def __init__(self, value=0):
        """Initialize counter with given value or default value (0)"""
        # What is the difference between 'self.counter' and 'counter'?
        self.counter = value
        counter = value
        MyCounter.n += 1

    def get(self):
        """Return the value of counter"""
        return self.counter

    def inc(self):
        """Increase counter by 1"""
        self.counter += 1
        # What is the scope of local_variable?
        local_variable = self.counter
        local_variable += 100


print(MyCounter.n)
c1 = MyCounter()
print(MyCounter.n, c1.get())
c2 = MyCounter(42)
print(MyCounter.n, c1.get())
print(MyCounter.n, c1.get())
c1.inc()
print(MyCounter.n, c1.get())
print(MyCounter.n, c1.get())
c1.inc()
print(MyCounter.n, c1.get())
print(MyCounter.n, c1.get())
c2.inc()
print(MyCounter.n, c1.get())
print(MyCounter.n, c1.get())
