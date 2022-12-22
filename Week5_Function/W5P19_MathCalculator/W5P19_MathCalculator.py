# 사칙연산 계산기

'''
Description

함수 calculate_digits(left_operand, right_operand, operator) 를 작성하시오.

함수 동작
2개의 숫자(left_operand, right_operand)와 1개의 연산자(operator)를 인자로 넘겨주면, 연산자에 따라서 사칙연산을 수행하고 결과를 반환함
매개변수
left_operand: (float) 사칙연산의 왼쪽 피연산자
right_operand: (float) 사칙연산의 오른쪽 피연산자
operator: (str) 연산자
'+', '-', '*', '/' 중에 하나
반환값:
1. (float) 연산자에 의해 계산된 연산결과
2. None ('+', '-', '*', '/' 중에 하나가 아닌경우)
'''

'''
함수 사용예시

print(calculate_digits(1, 2, '+'))
print(calculate_digits(3, 4, '-'))
print(calculate_digits(5, 6, '*'))
print(calculate_digits(7, 14, '/'))
print(calculate_digits(9, 10, '%'))
'''

'''
실행결과

3
-1
30
0.5
None
'''

# Code
def calculate_digits(left_operand, right_operand, operator):
    val1 = left_operand
    val2 = right_operand
    if operator == '+':
        result = float(val1+val2)
        return result
    elif operator == '-':
        result = float(val1-val2)
        return result
    elif operator == '*':
        result = float(val1*val2)
        return result
    elif operator == '/':
        result = float(val1/val2)
        return result
    else: 
        None
'''
operand_left = float(input('Enter a left operand: '))
operator = input('Enter an operator: ')
operand_right = float(input('Enter a right operand: '))

print(calculate_digits(operand_left, operand_right, operator))
'''