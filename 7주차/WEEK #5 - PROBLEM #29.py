# min-max 구하기

'''
Description

이중 리스트가 주어졌을 때,
이중 리스트 안쪽에 있는 리스트의 최대값들 중에 최소값을 구하는 함수 minmax()를 구현하시오.

함수동작
이중(2차) 리스트를 매개변수로 받아서
겉 리스트의 엘리먼트로 들어있는 리스트들의 최대값을 찾고
각 리스트의 최대값을 비교하여 가장 작은 값을 반환하는 함수
매개변수
nested_list: list를 원소로 포함하는 list
   - 한 가지 자료형만을 가진 list(안 쪽에 포함된 리스트)들을 포함하는 리스트.
즉, 자료형이 다른 것을 처리해줄 필요는 없음
반환값
안 쪽에 포함된 리스트들의 최대값 중 최소값을 반환
'''

'''
함수 사용 예시

example1 = [[1, 2], [3, 4], [5, 6]]
example2 = [[42, 1024, 23], [6, 28, 496], [2, 3, 5, 7, 11]]
example3 = [['programming', 'linear algebra'],
            ['operating systems', 'computer architecture']]
print(minmax(example1))
print(minmax(example2))
print(minmax(example3))
'''

'''
실행 결과 예시

2
11
operating systems
'''

# Code

def minmax(nested_list):
    """Return the minimum value of the maximum values of inner lists"""
    max_list=[]
    for val1 in nested_list:
        max=val1[0]
        for val2 in val1:
            if val2 > max:
                max = val2
        max_list.append(max)
    min = max_list[0]
    for val3 in max_list:
        if val3 < min:
            min = val3
    return min

example1 = [[1, 2], [3, 4], [5, 6]]
example2 = [[42, 1024, 23], [6, 28, 496], [2, 3, 5, 7, 11]]
example3 = [['programming', 'linear algebra'],
            ['operating systems', 'computer architecture']]
print(minmax(example1))
print(minmax(example2))
print(minmax(example3))
