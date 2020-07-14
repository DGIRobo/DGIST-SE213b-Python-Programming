# Bank Account

'''
Description

실습된 사용한 클래스 BankAccount(아래 코드 참조)에 withdraw(amount)와 deposit(amount)함수를 만드시오.

withdraw(amount) : 매개변수로 출금액을 받아서 instance variable balance에서 amount만큼 빼고 반환값은 없음

deposit(amount) : 매개변수로 입금액을 받아서 instance variable balance에서 amount만큼 더하고 반환값은 없음
'''

'''
참고 아래 클래스를 확장하여 사용할 것

class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance
    def balance(self):
        return self.balance
'''

'''
함수 사용 예시

b1 = BankAccount(500)
b2 = BankAccount(2000)
b1.withdraw(400)
print(b1.balance())
b2.deposit(1000)
print(b2.balance())
b2.withdraw(5000)
print(b2.balance())
'''

'''
실행 예시

100
3000
-2000
'''

# Codes
class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        self.balance-=amount
        return self.balance

    def deposit(self, amount):
        self.balance+=amount
        return self.balance

    def getBalance(self):
        return self.balance

if __name__ == '__main__':
    b1 = BankAccount(500)
    b2 = BankAccount(2000)
    b1.withdraw(400)
    print(b1.getBalance())
    b2.deposit(1000)
    print(b2.getBalance())
    b2.withdraw(5000)
    print(b2.getBalance())
