# 리스트의 최댓값 (재귀호출 이용)

'''
Description

max() 함수를 사용하지 말 것.

주어진 리스트에서 최댓값을 찾는 find_max(t, l, r)라는 함수를 재귀호출을 이용하여 구현할 것.
'''

'''
함수 find_max(t, l, r)

함수동작
t라는 리스트에서 index l과 r사이에서의 최댓값을 반환함

매개변수
t: 1개 이상의 원소를 포함하고 있는 리스트 (이 조건에 맞지 않는 경우는 신경쓰지 않아도 됨)
l: (int) 최댓값을 찾기 위한 범위의 최소 인덱스 (소문자 L)
r: (int) 최댓값을 찾기 위한 범위의 최대 인덱스

반환값
t[l], t[l+1], t[l+2], ..., t[r]에서 최대값을 찾아서 반환
'''

'''
참고 t라는 리스트가 있을 때, 아래와 같이 find_max() 함수를 호출하면 전체 범위에서 최대값을 찾아 반환하게 된다. (인덱스는 0부터 len(t)-1까지임)

find_max(t, 0, len(t)-1)

힌트 전체 범위를 어떻게 나눌 것인가를 고민해 볼 것
'''

'''
함수 실행 예시

t = [1, 2]
print(find_max(t, 0, len(t) - 1))
t = [36, 43, 70, 76, 32, 7, 8, 21, 69, 78]
print(find_max(t, 0, len(t) - 1))
'''

'''
실행결과

2
78
'''
#Code
def find_max(t, l, r):
    """Retuan the max number in t[l:r-1]"""
    #Base case
    if l == r:
        return t[l]
    #Recursive case
    else:
        candidate = find_max(t, l+1, r)
        if candidate < t[l]:
            return t[l]
        else:
            return candidate

if __name__ == '__main__':
    t = [1, 2]
    print(find_max(t, 0, len(t) - 1))
    t = [36, 43, 70, 76, 32, 7, 8, 21, 69, 78]
    print(find_max(t, 0, len(t) - 1))
