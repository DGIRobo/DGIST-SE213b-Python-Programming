# 구구단 함수작성(중첩 반복문)

'''
Description

구구단을 출력하는 함수 print_multiplication_table()을 작성하시오.

주의: 중첩 반복문(nested for loop statement)을 이용해서 작성할 것print_multiplication_table외 다른 함수는 만든지 말 것.

함수동작
구구단을 출력
   - 각 단의 숫자 사이에는 빈칸이 1개 있어야하며, 마지막 숫자 뒤에는 빈칸이 없음.
   - 각 단은 for loop를 이용해서 작성해야 하며, 각 단이 출력된 뒤에는 줄바꿈 함.
매개변수
없음
반환값
없음(None)
'''

'''
함수 사용예시

print_multiplication_table()
'''

'''
실행결과

1 2 3 4 5 6 7 8 9
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81
'''

#Code

def print_multiplication_table():
      for left_number in range(1, 10):
        for right_number in range(1, 10):
            print(left_number*right_number, end='')
            if right_number == 9:
                print('')
            else:
                print(' ', end='')

print_multiplication_table()
