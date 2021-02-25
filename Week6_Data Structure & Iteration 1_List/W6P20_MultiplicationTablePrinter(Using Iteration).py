# 구구단(반복문 이용)

'''
Description

구구단의 한 단을 출력하는 함수 print_multiples(n)과 구구단을 출력하는 함수 print_multiplication_table()을 작성할 것

주의: 반복문(for loop statement)을 이용해서 작성할 것, 이 함수들을 다시 작성하면서 어떻게 간단히 줄일 수 있는지를 생각하면서 코드를 작성하시오.

print_multiples(n) 함수
함수의 동작
1 <= n <= 9: 구구단의 n단을 출력하고, 줄을 바꿈, 주의: 숫자와 숫자 사이는 빈칸 2개 이용(hint: print함수의 end이용)
otherwise: Don't torture me!!!를 출력
매개변수
n: (int) n단을 출력, n은 1과 9 사이의 정수
반환값: 없음(None)
print_multiplication_table() 함수
함수의 동작
구구단을 출력한다
반드시 print_multiples() 함수를 사용할 것
while문을 사용하지 말 것!!!
매개변수: 없음
반환값: 없음(None)
'''

'''
함수 사용예시

print_multiples(3)
print_multiples(5)
print_multiples(-1)
print_multiplication_table()
'''

'''
실행결과

3  6  9  12  15  18  21  24  27  
5  10  15  20  25  30  35  40  45  
Don't torture me!!!
1  2  3  4  5  6  7  8  9  
2  4  6  8  10  12  14  16  18  
3  6  9  12  15  18  21  24  27  
4  8  12  16  20  24  28  32  36  
5  10  15  20  25  30  35  40  45  
6  12  18  24  30  36  42  48  54  
7  14  21  28  35  42  49  56  63  
8  16  24  32  40  48  56  64  72  
9  18  27  36  45  54  63  72  81
'''

#Code

def print_multiples(n):
    if 0<=n<=9:
        for value in  range(1, 10):
            print(value*n, end='  ')
        print('')
    else:
        print("Don't torture me!!!")

def print_multiplication_table():
    for left_number in range(1, 10):
        for right_number in range(1, 10):
            print(left_number*right_number, end='  ')
        print('')

print_multiples(3)
print_multiples(5)
print_multiples(-1)
print_multiplication_table()