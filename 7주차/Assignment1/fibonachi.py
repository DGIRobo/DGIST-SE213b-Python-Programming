# 피보나치 수열 만들기

'''
Description

함수 fibonacci_seq(num) 를 작성할 것.

함수동작
num을 매개변수로 받아서 num까지 피보나치 수열을 구하여 list에 넣고 반환함
매개변수
num: (int) 출력할 피보나치 수열의 개수
반환값
(list) 값의 크기가 작은 순서대로 정렬된 피보나치 수열 리스트
'''

'''
함수 사용예시

print(fibonacci_seq(1))
print(fibonacci_seq(3))
print(fibonacci_seq(5))
'''

'''
실행결과

[1]
[1, 1, 2]
[1, 1, 2, 3, 5]
'''

# Code

def fibonacci_seq(number):
    seq_list=[0, 1]
    while len(seq_list[1:]) < number:
        before_two = seq_list[-2]
        before_one = seq_list[-1]
        seq_list.append(before_two+before_one)
    return seq_list[1:]

print(fibonacci_seq(1))
print(fibonacci_seq(3))
print(fibonacci_seq(5))
print(fibonacci_seq(100))
