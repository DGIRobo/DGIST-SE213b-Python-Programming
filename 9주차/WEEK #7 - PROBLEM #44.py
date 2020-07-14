# 동명이인 학생 찾기 (사전 사용)

'''
Description

학생들의 이름을 원소로 갖는 list인 'name_list'를 인자로 받아 해당 list 내에 동명이인이 있는지 확인하고, 동명이인이 있는 경우 해당 학생들의 이름을 리스트 형태로 만들어 반환하는 함수 same_name(name_list)를 작성할 것. 가능한 한 수업시간에 배운 dictionary를 사용할 것을 권장함.

함수동작
name_list에서 동명인 사람을 찾아서 리스트로 반환함

매개변수
name_list : 학생들의 이름을 원소로 가지는 리스트

반환값
동명이인이 있는 경우: 해당 학생들의 이름을 list형태로 반환
동명이인이 없는 경우: "There is no student having the same name." 문자를 반환
'''

'''
함수 사용 예시

python
list1=['Alice','Bob','Jane']
list2=['Alice','Bob','Jane','Tom','Bob','Tom']
print(same_name(list1))
print(same_name(list2))
'''

'''
실행결과

There is no student having the same name.
['Bob', 'Tom']
'''

# Code
def same_name(name_list):
    name_count = {}
    same_name = []
    for name in name_list:
        name_count[name] = name_count.get(name, 0) + 1
    for item in name_count:
        if name_count.get(item) >= 2:
            same_name.append(item)
    if len(same_name) != 0:
        return same_name
    else: return 'There is no student having the same name.'


list1=['Alice','Bob','Jane']
list2=['Alice','Bob','Jane','Tom','Bob','Tom']

print(same_name(list1))
print(same_name(list2))
