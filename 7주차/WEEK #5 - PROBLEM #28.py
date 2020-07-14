# Accumulator

'''
Description

함수에 전달되는 list의 elements를 더하는 함수 acc_list(lst, elm)를 구현하시오.

함수동작
정수가 들어있는 list(lst)를 매개변수로 받아서 list안에 있는 값을 모두 더하는 함수
두 번째 매개변수인 elm이 None인 경우
   - lst의 첫 원소부터 마지막 원소까지 누산을 한 결과 반환
elm이 None가 아닌 경우
   - lst의 첫 원소부터 elm 전 까지의 원소를 누산하여 결과를 반환함
매개변수
lst:(list) 모든 원소가 정수인 리스트
elm:(int|None) lst리스트에서 찾고자 하는 element
반환값
누산한 결과값을 반환
   - elm이 None인 경우: lst의 모든 원소를 합한 결과를 반환
   - elm이 None가 아닌 경우: lst에서 elm이 처음 나오기 전까지의 원소의 합을 반환
'''

'''
함수 실행 예시

v1 = [1,4,1,5]
print(acc_list(v1, None))
print(acc_list(v1, 5))
'''

'''
실행 결과 예시

11
6
'''

# Code

def acc_list(lst, elm) :
    ''' acc_list returns accumulation of elements of list before elm appears.'''
    result=0
    if elm == None:
        for val1 in lst:
            result=result+val1
        return result
    else:
        for val2 in lst:
            if val2 == elm:
                break
            else:
                result=result+val2
        return result

v1 = [1,4,1,5]
print(acc_list(v1, None))
print(acc_list(v1, 5))
