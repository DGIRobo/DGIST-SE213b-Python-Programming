# 평균과 분산 계산

'''
Description

함수 get_mean_var_list(numbers_list)를 아래와 같이 작성하시오.

함수동작
이중 리스트를 인자로 받아 내부 리스트마다 각각 평균과 분산을 구해서 튜플로 만들고 이를 리스트에 추가하여 반환
매개변수
nested_list: numbers: 임의의 길이의 실수 이중 리스트
반환값
(nested list) 이중 리스트 내부의 각 리스트 마다 구한 평균과 분산을 튜플로 갖는 리스트 반환
'''

'''
함수 사용 예시

get_mean_var_list([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
get_mean_var_list([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]])
'''

'''
실행 결과

[(2.0, 0.666666666666667), (3.0, 0.6666666666666661), (4.0, 0.6666666666666679)]
[(3.0, 2.0), (4.0, 2.0), (5.0, 2.0)]
'''

# Code

def get_mean_var_list(numbers_list):
    mean_var=[]
    for list in numbers_list:
        sum = 0
        sqaure_sum = 0
        for val in list:
            sum=sum+val
            sqaure_sum=sqaure_sum+val**2
        mean_var.append((sum/len(list), sqaure_sum/len(list)-(sum/len(list))**2))
    return mean_var

print(get_mean_var_list([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))
print(get_mean_var_list([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]))
