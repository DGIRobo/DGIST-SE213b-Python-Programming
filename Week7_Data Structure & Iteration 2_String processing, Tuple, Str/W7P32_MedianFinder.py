# Median 구하기

'''
Description

리스트 입력으로 받고 리스트의 중앙값을 리턴하는 함수 find_median(lst)를 만드시오.

함수동작
정수가 들어있는 리스트(lst)를 받아서 중앙값을 반환
매개변수
lst: (list) 정수를 원소로 같는 리스트
반환값
lst가 빈 리스트인 경우 None반환
lst의 원소의 수가 홀수 인 경우: (int) (n+1)/2 번째 원소 반환
lst의 원소의 수가 짝수 인 경우: (float) n/2, 1+n/2 번째 원소의 평균값 반환
'''

'''
함수 사용 예시

print(find_median([ ] ))
print(find_median([1, 4, 3, 2, 5] ))
print(find_median([1, 2, 3, 4] ))
'''

'''
실행결과

None
3
2.5
'''

# Code

def find_median(lst):
    if len(lst) == 0:
        return None
    elif len(lst)%2 == 0:
        num1 = int(len(lst)/2)-1
        num2 = int(1+len(lst)/2)-1
        mean = (lst[num1]+lst[num2])/2
        return mean
    else:
        return lst[int((len(lst)+1)/2)-1]

print(find_median([  ] ))
print(find_median([1, 4, 3, 2, 5] ))
print(find_median([1, 2, 3, 4] ))
