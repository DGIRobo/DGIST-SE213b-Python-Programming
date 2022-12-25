# 리스트에서 짝수 홀수 구분하기

'''
Description

리스트 하나를 입력으로 받고 리스트의 원소 값을 비교하여 다음을 리턴하는 함수 list_even_odd(original_list)를 만드시오.

함수동작
original_list를 받아서 다음을 계산하여 반환하는 함수
   - 리스트의 원소 중 짝수인 원소의 개수
   - 리스트의 원소 중 홀수인 원소의 개수
   - 원래 리스트에서 짝수인 원소만 가지는 정렬된 리스트
   - 원래 리스트에서 홀수인 원소만 가지는 정렬된 리스트
매개변수
original_list:(list) 숫자가 들어있는 리스트
반환값
튜플의 첫번째 요소: (int) 주어진 리스트에서 짝수의 개수
튜플의 두번째 요소: (int) 주어진 리스트에서 홀수의 개수
튜플의 세번째 요소: (list) 주어진 리스트에서 짝수만 추출하여 만든 정렬된 리스트
튜플의 네번째 요소: (list) 주어진 리스트에서 홀수만 추출하여 만든 정렬된 리스트
'''

'''
함수 사용예제

list = [20, 5, 31, 94, 61, 39]
even_count, odd_count, even_list, odd_list = list_even_odd(list)
print(even_count, odd_count, even_list, odd_list)
'''

'''
실행결과

2 4 [20, 94] [5, 31, 39, 61]
'''

# Code

def list_even_odd(original_list):
    sort_list=sorted(original_list)
    odd_list=[]
    even_list=[]
    for val in sort_list:
        if val%2 == 0:
            even_list.append(val)
        else: odd_list.append(val)
    odd_count = len(odd_list)
    even_count = len(even_list)
    return even_count, odd_count, even_list, odd_list

list = [20, 5, 31, 94, 61, 39]
even_count, odd_count, even_list, odd_list = list_even_odd(list)
print(even_count, odd_count, even_list, odd_list)
