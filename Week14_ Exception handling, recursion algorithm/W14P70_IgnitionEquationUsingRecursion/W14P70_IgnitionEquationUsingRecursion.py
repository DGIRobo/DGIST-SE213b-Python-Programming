# 점화식 (재귀호출 이용)

'''
Description

다음가 같은 점화식으로 주어지는 수열(sequence)를 계산하는 함수 sequence_a(n)을 구현하시오.

a0=1,  an=2⋅an−1+1
'''

'''
함수 sequence_a(n)

함수동작
n을 매개변수로 받아서 n에 해당하는 함수 값을 반환함

매개변수
n: 0 이상의 정수. 음수 혹은 실수가 입력되는 경우는 생각하지 않아도 됨

반환값
(int) $a_n$의 값 반환
'''

'''
함수 실행 예시

print(sequence_a(0))
print(sequence_a(1))
print(sequence_a(5))
'''

'''
결과 예시

1
3
63
'''

#Code
def sequence_a(n):
    """Retuan a_n for the given sequence"""
    #Base case
    if n==0:
        return 1

    #Recursive case
    return 2*sequence_a(n-1)+1

if __name__ == '__main__':
    print(sequence_a(0))
    print(sequence_a(1))
    print(sequence_a(5))
