# 사칙연산 계산기

'''
Description
사용자에게 두 숫자와 "+, -, *, /" 중 하나인 연산자를 입력받아 두 수의 연산을 수행하는 계산기를 만들 것.
'''

'''
실행예시
Enter a left operand: 12.34
Enter an operator: *
Enter a right operand: 5.6
69.104
'''

# Code
number1 = float(input('Enter a left operand: '))
operator = input('Enter an oprator: ')
number2 = float(input('Enter a right operand: '))

if operator=='+':
    print(number1+number2)
elif operator=='-':
    print(number1-number2)
elif operator=='*':
    print(number1*number2)
elif operator=='/':
    print(number1/number2)
