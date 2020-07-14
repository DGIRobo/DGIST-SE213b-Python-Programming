#카운팅 (이론시간 예제)

'''
Description

카운팅 (이론시간 예제)
사전을 활용하는 예제를 다룰때, 카운팅 하는 예제를 사용했었다. 리스트를 인자로 받아서 리스트에 있는 요소 별로 몇번 사용되고 있는지 확인하는 코드를 작성하였다. 사전의 key값으로 요소를 넣고 value로 빈도수를 기입하는 코드를 아래와 같이 작성하였지만, 실행시, 뜻하지 않게 Key error 오류가 발생하였다.

수업시간에 이를 해결하는 방법으로 사전의 get함수를 활용하거나 in 연산자를 이용하는 방법을 다뤘다. 본 연습에서는 발생하는 에러를 확인해 보고 해당 에러를 처리할 수 있는 try구문을 구현하시오. (다양한 exception을 활용하여 동작시켜본다.)

def count_items(sequence):
    count = {}
    for item in sequence:
        count[item] += 1
    return count

t = ['python', 'c++', 'python', 'go', 'java', 'java']
print(count_items(t))
'''

'''
원하는 답

{'python': 2, 'c++': 1, 'go': 1, 'java': 2}
'''

'''
실행결과

Traceback (most recent call last):
  File "main.py", line 8, in <module>
    print(count_items(t))
  File "main.py", line 4, in count_items
    count[item] += 1
KeyError: 'python'
'''

#Code
def count_items(sequence):
    count = {}
    for item in sequence:
        try:
            count[item] += 1
        except KeyError:
            count[item] = 1
    return count

t = ['python', 'c++', 'python', 'go', 'java', 'java']
print(count_items(t))
