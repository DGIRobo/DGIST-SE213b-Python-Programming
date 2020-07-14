# Reverse list

'''
Description

매개변수 리스트에 대해, 리스트 요소의 배열 순서를 뒤집는 함수 reverse(lst) 를 만드시오.

함수동작	
예를들어, lst=['a','b','c'] 를 매개변수로 입력하면, lst의 순서가 반전된 리스트인 ['c','b','a']를 lst에 다시 할당하고 lst를 반환하는 함수를 작성할 것.
매개변수	
lst: (list) 문자열 리스트
반환값	
(list) 매개변수 lst의 모든 elements순서가 뒤집어진 리스트
'''

'''
함수 사용예시

lst=['a','b','c']
print(reverse(lst))
print(lst)
'''

'''
실행 결과

['c', 'b', 'a']
['c', 'b', 'a']
'''

#Code

def reverse(lst): #2. 이렇게 함수가 리스트 자료형을 파라미터로 받아오면, 함수의 로컬 네임스페이스에는 그 파라미터가 리스트자료형인 것과 그것이 저장된 메모리의 주소가 어디인지 기록된다.
    copied = []
    for value in range(len(lst)):
        copied.append(lst[value])
    for value in range(len(lst)):
        lst[value]=copied[-1-value] #3. 그래서 이렇게 리스트를 새로 만들지 않고 이미 만들어진 리스트에다 장난질을 하면, 리스트 자체가 바뀌기 때문에, 이 문장이 실행된 이후의 이 리스트에 관련된 연산이나 명령들은 이 장난질에 의해 '바뀐' 리스트에 맞춰서 작성해주어야 한다.
    return lst

lst=['a', 'b', 'c'] #1. 여기서 list를 생성하면, global namespace에는 lst는 리스트자료형인 것과 그것이 저장된 메모리의 주소가 어디인지 기록되고, 다른 메모리 공간에서 lst는 인덱스 0번 자리에 문자 a, 인덱스 1번 자리에 b, 인덱스 2번 자리에 c를 가진 리스트 자료형이라는 것이 저장된다.
print(reverse(lst))
print(lst) #4. 따라서 lst=reverse(lst)를 해주지 않아도 lst는 Global에서 접속하든 Local에서 접속하든 한곳 lst이 저장된 메모리 주소로 접속하기 때문에 장난질 한 것이 그대로 반영되어 있다.