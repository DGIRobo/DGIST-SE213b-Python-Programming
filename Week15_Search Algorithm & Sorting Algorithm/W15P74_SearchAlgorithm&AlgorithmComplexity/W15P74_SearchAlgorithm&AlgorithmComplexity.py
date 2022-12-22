# 검색 알고리즘, 알고리즘 복잡도

'''
Description

참고: sorted(), list.sort()

t = [4, 3, 8, 6, 7, 13, 10, 14, 9]
print(t)
t2 = sorted(t)
print(t2)
print(t)

[4, 3, 8, 6, 7, 13, 10, 14, 9]
[3, 4, 6, 7, 8, 9, 10, 13, 14]
[4, 3, 8, 6, 7, 13, 10, 14, 9]

t.sort() # list의 sort() 함수는 반환값이 없음
print(t)

[3, 4, 6, 7, 8, 9, 10, 13, 14]
'''

'''
검색 알고리즘

Sequential Search (순차 검색): 앞에서부터 하나씩 원하는 값이 리스트의 어디에(인덱스) 저장되어 있는지 찾는 알고리즘
Binary Search (이진 검색): 리스트가 정렬되어 있을 때, 찾는 범위는 반씩 줄이면서 원하는 값이 리스트의 어디에(인덱스) 저장되어 있는지 찾는 알고리즘
'''

'''
실행시간 측정 방법

python에서 제공하는 timeit 모듈에서 제공하는 timeit() 함수를 이용하여, 특정 코드의 실행시간을 측정할 수 있다.

timeit.timeit() 함수는 아래와 같이 정의되어 있다.

timeit.timeit(stmt='pass', setup='pass', timer=, number=1000000, globals=None)
매개변수
stmt: 실행시간을 측정하기 위한 코드
setup: stmt를 실행하기 전에 한 번만 실행하는 코드
timer: 시간을 측정하는 timer의 종류를 명시
number: 반복실행할 회수
globals: 글로벌변수/함수 등을 전달하기 위하여 사용

반환값
stmt로 전달된 명령문을 number번 실행해서 그 평균 실행시간을 반환 (초 단위)


주의 정렬 알고리즘의 경우에는, 입력데이터에 따라 실행속도가 매우 다르게 되는 경우가 많다. 예를 들어, 모든 데이터들이 이미 정렬되어 있는 경우에 실행이 바로 끝나는 알고리즘이 존재한다. 혹은 데이터가 역순으로 정렬되어 있을 때, 평균실행속도보다 실행시간이 훨씬 오래 걸리는 알고리즘도 존재한다.

따라서 정렬알고리즘을 테스트하기 위해서는 리스트에 난수를 발생시킨 후 (혹은 원하는 데이터를 저장한 후), timeit() 함수의 매개변수 number에 1를 전달하여, 한 번만 실행하도록 한다.

같은 데이터 크기 n에 대하여 여러 번 실행해서 그 평균을 구하고 싶은 경우에는, 매번 리스트에 원하는 데이터(난수 혹은 원하는 데이터값)을 넣고 timeit() 함수를 호출하여야 한다.
'''

'''
연습 1. sequential search & binary search

1) 동작의 이해
sequential_search(), binary_search() 함수의 verbose 매개변수에 True를 넘겨주어 실행하면서, 검색 알고리즘의 동작을 이해해볼 것.
인자로 전달하는 리스트의 크기, 저장된 값들을 바꾸면서 프로그램이 어떠한 단계로 실행되는지, 즉 알고리즘이 어떻게 작동하는지 이해해볼 것.
질문: 코드를 그대로 수행하면 우리가 찾고자 하는 값(5)가 리스트의 원소로 존재함에도 불구하고, binary_search()는 None을 반환한다. 이 이유는 무엇인가?

2) 테스트 케이스 작성
알고리즘이 제대로 작동하는 것을 확인하기 위해서 테스트 케이스를 잘 만들 필요가 있다. (참고: 채점 코드로 이와 유사한 방법어로 만들고 있습니다.)
검색의 경우에는 다음과 같이 테스트를 할 수 있을 것입니다.
우선 함수에 전달될 수 있는 가장 간단한 경우들에 대해서 테스트를 합니다. 즉 빈 리스트부터, 원소가 1개, 2개, ... 등의 간단한 경우를 테스트 합니다. 그리고 찾고자 하는 값이 리스트에 존재하는 경우, 그렇지 않은 경우 등에 대해서 나눠서 테스트를 할 필요가 있습니다.
또한 리스트의 원소의 순서에 따라 알고리즘이 작동하지 않을 수 있으니, 동일한 원소들이 포함되어도 그 리스트의 순서를 바꾼 입력을 주어보는 것도 필요하구요.
그리고 어느 정도 이상 규모가 큰 입력에 대해서도 제대로 작동을 하는지 확인을 할 필요도 있습니다. 아래의 예시에서는 n=100인 경우에 테스트를 한 경우입니다.

print(sequential_search([], 1))
print(sequential_search([1], 1))
print(sequential_search([2], 1))
print(sequential_search([1, 2], 1))
print(sequential_search([2, 1], 1))
print(sequential_search([1, 2], 2))
print(sequential_search([2, 1], 2))
print(sequential_search([1, 2], 3))
print(sequential_search([2, 1], 3))

n = 100
t = list(range(n))
random.shuffle(t)
print('t =', t)
for i in range(n):
    index = sequential_search(t, i)
    if index == None:
        # since the list contains 0..(n-1), None shouldn't be returned
        print(f'There is a problem when looking for {i} in t')

To do
이진 검색에 대해서도 위와 유사한 테스트 케이스를 만들어 볼 것. 테스트 케이스가 달라야 할텐데, 그 이유는 무엇일까?
이진 검색에서 일부러 오류를 만들어보고 (예: first = mid + 1 부분을 first = mid로 수정), 이 경우에 어떤 테스트 케이스에서 문제가 생기는지 확인해 볼 것
참고: 필요하면 함수를 부를 때 verbose에 True를 전달하면 도움이 된다

3) n에 따른 실행시간 측정
timeit_search() 함수를 호출하는 부분을 수정하여, 아래 표를 채워보고, 다음 질문에 답해볼 것.
표만을 보고, 알고리즘 복잡도를 추정할 수 있나?
참고: timeit_search()는 수정하지 않고, 그대로 사용해도 됨.
'''

#Code
import random
import timeit

def sequential_search(sequence, item, verbose=False):
    if verbose:
        print(f'sequential_search() invoked,',
              f'item={item}, sequence={sequence}')
    for index in range(len(sequence)):
        if verbose:
            print(f'index={index}, sequence[index]={sequence[index]}')
        if sequence[index] == item:
            return index
    return None

def binary_search(sequence, item, verbose=False):
    if verbose:
        print(f'binary_search() invoked,',
              f'item={item}, sequence={sequence}')
    first = 0
    last = len(sequence) - 1  # last is INCLUSIVE

    while first <= last:
        mid = (first + last) // 2
        if verbose:
            print(f'first={first}, mid={mid}, last={last},',
                  f'sequence[mid]={sequence[mid]}')
        if sequence[mid] == item:
            return mid
        if item < sequence[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return None

def timeit_search(func, n, repetition=None):
    """Return the execution time of func() for repetition times,
       for the problem size of n
    """
    if repetition == None:
        repetition = n

    t = list(range(n))
    duration = timeit.timeit('func(t, random.randrange(n))',
                             setup='import random',
                             globals=locals(),
                             number=repetition)
    return duration

if __name__ == '__main__':
    # 1)
    n = 10
    item = 5

    t = list(range(n))
    random.shuffle(t)  # make a random list
    print(f'Searching {item} in {t}...')
    print('sequential:',  sequential_search(t, item, True))
    print('binary :',  binary_search(t, item, True))

    # 2)
    print(sequential_search([], 1))
    print(sequential_search([1], 1))
    print(sequential_search([2], 1))
    print(sequential_search([1, 2], 1))
    print(sequential_search([2, 1], 1))
    print(sequential_search([1, 2], 2))
    print(sequential_search([2, 1], 2))
    print(sequential_search([1, 2], 3))
    print(sequential_search([2, 1], 3))

    n = 100
    t = list(range(n))
    random.shuffle(t)
    print('t =', t)
    for i in range(n):
        index = sequential_search(t, i)
        if index == None:
            # since the list contains 0..(n-1), None shouldn't be returned
            print(f'There is a problem when looking for {i} in t')
        else:
            print(f'The index of the value {i}: {index}')

    # 3)
    problem_sizes = [1, 10, 20, 50, 100]
    rep = 100
    print('Sequential search...')
    for n in problem_sizes:
        print(f'{n:5d}:', timeit_search(sequential_search, n, rep))

    print('Binary search...')
    for n in problem_sizes:
        print(f'{n:5d}:', timeit_search(binary_search, n, rep))
