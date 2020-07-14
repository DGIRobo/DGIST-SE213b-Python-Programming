# MyCounter 확장 (연산자 사용)

'''
Description

앞에서 사용한 클래스 MyCounter(아래 코드 참조)에 더하기 연산 +와 비교연산 == 함수를 만들 것.

__add__(self, obj) : instance method add를 작성하시오. 매개변수로 자기자신과 다른 값을 받아서, obj가 숫자면 self의 counter과 obj를 더한 값을 반환하고 obj가 MyCouter의 instance라면 obj의 counter값과 self의 counter값의 합을 반환

__eq__(self, other_counter) : instance method eq를 작성하시오. 매개변수로 자기자신과 다른 MyCounter instance를 받아서, 두 카운터의 값이 같으면 True를 반환하고 아니면 False를 반환
'''

'''
** hint : if type(변수) == int : #를 활용
참고 아래 클래스를 확장하여 사용할 것

class MyCounter():
    def __init__(self, value=0):
        self.counter = value

    def inc(self):
        self.counter += 1

    def get(self):
        return self.counter
'''

'''
함수 사용 예시

c1 = MyCounter()
c2 = MyCounter(42)
if c1 + c2 >= 20 :
    print (c1+c2)
else:
    print ("less than 20")
if c1 == c2:
    print ("c1 is equal to c2")
else :
    print ("c1 is not equal to c2")
c3 = MyCounter(42)
if c2 == c3:
    print ("c2 is equal to c3")
else :
    print ("c2 is not equal to c3")
print(c1+2)
'''

'''
실행 예시

42
c1 is not equal to c2
c2 is not equal to c3
2
'''

# Codes
class MyCounter():

    def __init__(self, value=0):
        self.counter = value

    def inc(self):
        self.counter += 1

    def get(self):
        return self.counter

    def __add__(self, obj):
        if type(obj) == int:
            return self.counter + obj
        else:
            return self.counter + obj.counter

    def __eq__(self, other_counter):
        if self.counter == other_counter.counter:
            return True
        else:
            return False

if __name__ == '__main__':
    c1 = MyCounter()
    c2 = MyCounter(42)
    if c1 + c2 >= 20 :
        print (c1+c2)
    else:
        print ("less than 20")
    if c1 == c2:
        print ("c1 is equal to c2")
    else :
        print ("c1 is not equal to c2")
    c3 = MyCounter(42)
    if c2 == c3:
        print ("c2 is equal to c3")
    else :
        print ("c2 is not equal to c3")
    print(c1+2)
