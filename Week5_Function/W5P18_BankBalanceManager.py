# 은행 잔고 관리

'''
Description

은행 잔고를 관리하는 함수 manage_account(balance, choice, money)를 구현하시오.

조건에 맞는 출력문과 입/출금 후 잔액을 리턴하시오.

함수 동작
현재 잔고(balance)와 입출력 여부(choice), 입출력 금액(money)를 인자로 받아서 입출력 이후 잔고를 반환함.
입출력이 정상적으로 이루어진 경우 잔고를 출력
잔고 보다 출금 금액이 큰경우에는 출금하지 않고 There is not enough money in your account를 출력
choice가 '+' 또는 '-'가 아닌 경우에는 ERROR를 출력
매개변수
balance: (int) 현재 잔고 입력
choice: (str) 입 출금 여부
'+', '-' 중에 하나 (입금, 출금)
money: (int) 입출금 하고자 하는 금액
반환값: (int) 현재 잔고를 반환
'''

'''
함수 사용 예시

balance = 10000    
balance = manage_account(balance, '-', 20000)
balance = manage_account(balance, '-', 5000)
balance = manage_account(balance, '=', 20000)
balance = manage_account(balance, '+', 1000)
'''

'''
실행결과

There is not enough money in your account
5000
ERROR
6000
'''

# Code
def manage_account(balance, choice, money):
    now = int(balance)
    if choice == '+':
        print(now+money)
        return now+money
    elif choice == '-':
        if now>money:
            print(now-money)
            return now-money
        elif now<money:
            print('There is not enough money in your account')
            return now
    else:
        print('ERROR')
        return now


balance = 10000
balance = manage_account(balance, '-', 20000)
balance = manage_account(balance, '-', 5000)
balance = manage_account(balance, '=', 20000)
balance = manage_account(balance, '+', 1000)
