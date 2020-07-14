# 순환하는 소수 찾기

'''
Description

어떤 수가 있을 때, 그 숫자와 그 순자를 회전시켜 나오는 모든 수가 소수인 경우, 그 수를 순환하는 소수라 한다. 예를 들어, 1193의 경우, 이 숫자를 (왼쪽 혹은 오른쪽으로) 순환하여 얻을 수 있는 숫자 1931, 9311, 3119 모두 소수이다. 따라서 이 수를 순환하는 소수라고 한다.
어떤 수가 순환하는 소수인지를 확인하기 위하여, 다음과 같은 함수를 작성하시오.

circular(n)
함수동작
매개변수인 자연수 n를 왼쪽으로 회전하여 만들 수 있는 모든 수를 원소로 포함하는 리스트를 반환하는 함수이다.
반드시 prime()과 circular()를 사용할 것
제한 조건 (아래의 입력은 항상 만족된다. 즉 아래 조건을 어기는 함수 입력값은 신경쓰지 않아도 된다)
n는 항상 자연수가 전달된다고 가정한다.

매개변수
n: 자연수

반환값	(리스트)
n과 n를 순환하여 얻을 수 있는 모든 수를 포함하는 리스트
n을 먼저포함하고, 왼쪽으로 회전시킨 순서대로 숫자를 포함할 것 (아래 함수 사용 예시와 실행 결과를 참고할 것)


prime(n)
함수동작
매개변수인 자연수 n이 소수인지를 확인하는 함수이다.
제한 조건 (아래의 입력은 항상 만족된다. 즉 아래 조건을 어기는 함수 입력값은 신경쓰지 않아도 된다)
n는 항상 자연수가 전달된다고 가정한다.

매개변수
n: 자연수

반환값
True: n이 소수일 때
False: n이 소수가 아닐 때


circular_prime(n)
함수동작
매개변수인 자연수 n이 순환하는 소수인지를 확인하는 함수이다.
반드시 prime()과 circular()를 사용할 것
제한 조건 (아래의 입력은 항상 만족된다. 즉 아래 조건을 어기는 함수 입력값은 신경쓰지 않아도 된다)
n는 항상 자연수가 전달된다고 가정한다.

매개변수
n: 자연수

반환값
True: n이 순환하는 소수일 때
False: n이 순환하는 소수가 아닐 때
'''

'''
함수 사용 예시

print(circular(123))
print(circular(1123))
print(prime(2))
print(prime(3))
print(prime(4))
print(circular_prime(197))
print(circular_prime(13))
print(circular_prime(19))
'''

'''
실행 결과

[123, 231, 312]
[1123, 1231, 2311, 3112]
True
True
False
True
True
False
'''

#Code
def circular(n):
    circularNumbers = []
    circularNumbers.append(n)
    strForm = str(n)
    for counting in range(1, len(strForm)):
        strForm = strForm[1:] + strForm[0]
        circularNumbers.append(int(strForm))
    return circularNumbers

def prime(n):
    counting = []
    for checking in range(2, n+1):
        if n%checking == 0:
            counting.append(checking)
    if len(counting)==1: return True
    else: return False

def circular_prime(n):
    circularNums = circular(n)
    for Num in circularNums:
        if prime(Num): continue
        return False
    return True

print(circular(123))
print(circular(1123))
print(prime(2))
print(prime(3))
print(prime(4))
print(circular_prime(197))
print(circular_prime(13))
print(circular_prime(19))
