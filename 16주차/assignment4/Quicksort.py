#Quick sort 구현

'''
Description

Quicksort에서는 파티션하는 과정을 통해서 정렬을 진행한다. 다양한 파티션 방법이 존재하나, 본 과제에서는 이론수업시간에 배운 파티션 방법을 이용하여 아래 코드를 완성하시오.
참고: 인터넷에서 아래 방식과 같은 코드를 찾아서 사용해도 괜찮음
아래 작성되어 있는 코드를 확인하고 파티션 함수partition(lst, left, right)를 작성하시오.
'''

'''
partition(lst, left, right) 함수

함수동작
전체 lst를 인자로 받고, lst에서 index left(포함)에서 right(포함)까지 에서 파티션을 함.
왼쪽 첫 원소(lst[left])를 pivot으로 설정하고 left에서 right까지 파티션한결과가 그래도 lst에 반영됨

매개변수
lst: (list) 정렬하고자 하는 정수가 들어있는 전체 리스트
left: (int) 파티션을 진행할 구간의 첫번째 인덱스
right: (int) 파티션을 진행할 구간의 마지막 인덱스

반환값
(int) 파티션 결과, 변경된 pivot의 위치(index)를 반환
'''

'''
함수 사용예시

a = [1, 4, 2, 7, 0]
quick_sort(a)
print(a)
b = [1, 4, 2, 7, 0]
print(partition(b, 2,4))
print(b)
'''

'''
실행결과

[0, 1, 2, 4, 7]
3
[1, 4, 0, 2, 7]
'''

#Code
# partition 함수를 작성하시오.
def partition(lst, left, right):
    pivot = left
    lm = left + 1
    rm = right
    while True:
        while lm < right and lst[lm] < lst[pivot]:
            lm = lm + 1
        while rm > pivot and lst[rm] > lst[pivot]:
            rm = rm - 1
        if rm <= lm:
            break
        lst[lm], lst[rm] = lst[rm], lst[lm]
        lm = lm + 1
        rm = rm - 1

    lst[pivot], lst[rm] = lst[rm], lst[pivot]
    return rm

def quick_sort(lst, left=None, right=None):
    if left == None: left = 0
    if right == None: right = len(lst)-1

    # base case
    if left >= right:
        return
    # recursive case
    # p: location(index) of pivot value
    p = partition(lst, left, right)
    quick_sort(lst, left, p - 1)
    quick_sort(lst, p + 1, right)

if __name__ == "__main__":
    a = [1, 4, 2, 7, 0]
    quick_sort(a)
    print(a)

    b = [1, 4, 2, 7, 0]
    print(partition(b, 2, 4))
    print(b)

    c = [10, 11, 111, 98, 24, 25, 22, 43, 96, 76, 88, 88, 21, 1, 4, 2, 7, 0]
    quick_sort(c)
    print(c)
