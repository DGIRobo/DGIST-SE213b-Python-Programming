# 리스트 두 개의 공통된 원소의 리스트를 반환하기

'''
Description

두 개의 시퀀스를 인자로 받아 두 리스트의 공통된 원소를 정렬된 순서대로 반환하는 함수 common_items(sequence1, sequence2, reverse=False) 를 만드시오.

함수동작
sequnce1과 sequence2를 받아서 공통 요소를 찾아서 정렬된리스트로 반환함

매개변수
sequence1: 임의의 시퀀스 (list, tuple, str)
sequence2: 임의의 시퀀스 (list, tuple, str)
reverse: bool. 정렬 순서를 역순으로 할 지를 지정.
   - True: 정렬을 역순으로(큰 순서에서 작은 순, 혹은 알파벳을 거꾸로) 함
   - False: 정렬을 순서대로 함

반환값
(리스트) 공통된 원소를 포함하는 리스트
공통된 원소가 없는 경우에는 빈 리스트를 반환
'''

'''
함수 사용예시

print(common_items('abracadabra', 'surisurimasuri'))
print(common_items('abracadabra', 'surisurimasuri', True))
print(common_items([42, 1024, 23], [6, 28, 496]))
print(common_items([2, 3, 5, 7], [1, 1, 2, 3, 5, 8]))
print(common_items([2, 3, 5, 7], [1, 1, 2, 3, 5, 8], False))
print(common_items([2, 3, 5, 7], (1, 1, 2, 3, 5, 8)))
'''

'''
실행결과

['a', 'r']
['r', 'a']
[]
[2, 3, 5]
[2, 3, 5]
[2, 3, 5]
'''

# Code

def common_items(sequence1, sequence2, reverse=False):
    """Return sorted list of the common items of sequence1 and sequence2"""
    new_set = set(sequence1) & set(sequence2)
    new_list = list(new_set)
    if reverse == True:    new_list.sort(key = None, reverse = True)
    else:    new_list.sort(key = None, reverse = False)
    return new_list

print(common_items('abracadabra', 'surisurimasuri'))
print(common_items('abracadabra', 'surisurimasuri', True))
print(common_items([42, 1024, 23], [6, 28, 496]))
print(common_items([2, 3, 5, 7], [1, 1, 2, 3, 5, 8]))
print(common_items([2, 3, 5, 7], [1, 1, 2, 3, 5, 8], False))
print(common_items([2, 3, 5, 7], (1, 1, 2, 3, 5, 8)))
