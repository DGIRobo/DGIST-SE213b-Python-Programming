#정렬 알고리즘 (selectin sort, merge sort, and quick sort)

'''
Description

정렬 알고리즘의 소개

선택 정렬 (Selection Sort)
기본 아이디어
가장 작은 숫자를 찾아서 맨 앞에,
나머지 숫자 중 작은 숫자를 찾아서 두 번째에,
이 과정을 (n-1)번 반복

정렬의 진행
한 단계가 지날 때마다, 작은 순서대로 정렬이 된 숫자가 하나씩 들어난다. 즉 k 단계를 거친 후, 리스트 앞의 k개의 원소는 정렬이 된 상태로 존재한다.


병합 정렬 (Merge Sort)
기본 아이디어
두 개의 정렬된 리스트가 있으면, 두 리스트에 있는 원소들을 포함하는 정렬된 큰 리스트를 만드는 것은 쉽다. 새로운 리스트를 만들어서, 두 리스트의 가장 앞쪽의 숫자들을 비교하면서 그 중 작은 수를 새로운 리스트에 차례로 넣어주면 된다. 이 과정을 병합(merge) 이라 한다.
위에서 설명한 병합 을 이용하여 정렬을 쉽게 구현할 수 있다. 리스트를 둘로 나누고, 각각은 정렬한 후, 병합과정을 거치면 전체 리스트가 정렬이 된다.
둘로 나뉘어진 리스트는 재귀적으로 정렬을 하고, 즉, 다시 리스트를 둘로 나눠서 각각을 정렬하고, 병합을 하는 과정을 수행한다. 이 때 base case는 원소가 하나가 있는 리스트다.

정렬의 진행
가장 작은 단위, 즉 원소가 하나 있는 리스트로 나뉘어진 후, 병합이 일어나게 된다.
즉, 리스트에서 정렬된 작은 부분들이 증가하게 되고, 이러한 범위가 점점 커져서 전체 리스트가 정렬된다.


퀵 정렬 (Quick Sort)
기본 아이디어
리스트 안에 있는 임의의 수를 정해서, 그 수보다 작은 숫자는 리스트의 앞으로 큰 숫자를 리스트의 뒤로 보낸다.
특정한 숫자보다 큰 숫자와 작은 숫자로 나뉘어진 두 영역을 각각 재귀적으로 정렬한다. 이렇게 재귀적으로 호출을 할 때, base case는 원소가 하나있는 리스트가 된다.

정렬의 진행
재귀적으로 호출이 될 때마다 리스트가 전체적으로 조금씩 정렬되는 것을 볼 수 있다.
3개의 정렬 알고리즘을 작성해 보고, 리스트의 크기에 따라 실행시간을 비교해보시오.

다음 각각의 경우에 대해서 표를 완성해볼 것
리스트의 크기(=원소의 개수)가 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000때 실행시간
리스트의 원소가 1) 정렬이 되어 있을 때, 2) 역순으로 정렬이 되어 있을 때, 3) 임의의 배열로 되어 있을 때
각각의 경우에 대해서 실행시간을 보고, 알고리즘 복잡도를 추청해볼 것. 특히 quick sort의 경우에, 리스터의 정렬 상태에 따라서 실행시간이 어떻게 되는지를 측정해볼 것.
'''

#Code
import timeit
import random


def selection_sort(t):
    pass


def merge_sort(t, l=None, r=None):
    if l==None: l = 0
    if r==None: r = len(t)-1
    pass


def quick_sort(t, l=None, r=None):
    if l==None: l = 0
    if r==None: r = len(t)-1
    pass

def timeit_sort(func, n, data='random', repetition=100):
    # generate n random numbers
    t = list(range(n))
    duration = 0
    for i in range(repetition):
        if data == 'random':
            t1 = t.copy()
            random.shuffle(t)
        elif data == 'reverse':
            t1 = t[::-1]
        else:
            t1 = t.copy()
        duration += timeit.timeit('func(t1)', globals=locals(), number=1)
    return duration

if __name__ == '__main__':
    # 1) Understand how sorting algorithms work in detail
    n = 10

    t = list(range(n))
    random.shuffle(t)  # make a random list
    print('* Selection Sort')
    t1 = t.copy()
    selection_sort(t1)
    print('* Merge Sort')
    t2 = t.copy()
    merge_sort(t2, 0, len(t2) - 1)
    print('* Quick Sort')
    t3 = t.copy()
    quick_sort(t3, 0, len(t3) - 1)

    # 2) Set up test cases for sorting algorithms
    t = []
    selection_sort(t)
    t = [1]
    selection_sort(t)
    t = [1, 2]
    selection_sort(t)
    t = [1, 1]
    selection_sort(t)
    t = [2, 1]
    selection_sort(t)
    t = [1, 2, 3]
    selection_sort(t)
    t = [1, 3, 2]
    selection_sort(t)
    t = [1, 2, 3, 4]
    selection_sort(t)
    t = [4, 3, 2, 1]
    selection_sort(t)
    t = [2, 4, 1, 3]
    selection_sort(t)

    # 3) Measure execution time of sorting algoritms with varying n
    problem_sizes = [1, 10, 20, 50, 100]
    rep = 100
    data = 'random'
    print('Selection sort...')
    for n in problem_sizes:
        print(f'{n:5d}:', timeit_sort(selection_sort, n, data, rep))

    print('Merge sort...')
    for n in problem_sizes:
        print(f'{n:5d}:', timeit_sort(merge_sort, n, data, rep))

    print('Quick sort...')
    for n in problem_sizes:
        print(f'{n:5d}:', timeit_sort(quick_sort, n, data, rep))
