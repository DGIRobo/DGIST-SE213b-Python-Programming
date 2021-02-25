# 사전 수정하기

'''
Description
주어진 사전에 추가할 key와 value를 인자로 받아 add_to_dict(dictionary,key,value,act)함수를 실행시키면 주어진 사전의 key에 해당하는 카테고리에 value를 추가해서 그 카테고리를 리턴함

add_to_dict(dictionary,key,value,act)

함수동작
Act값에 따라서 사전에 추가/삭제하는 함수를 작성
추가시 : key가 사전에 없는 경우, 사전에 key를 생성하여 value를 추가 - 리스트가 아닌 스트링으로 그냥 추가하면됨 key:value
해당하는 key에 존재하는 경우에는 value에 들어있는 리스트에 새로운 value를 append
이미 value가 리스트에 존재하는 경우, 'This word already exists.' 리턴

매개변수
dictionary: 수정할 사전
key: value를 추가(삭제)할 항목
value: 추가(삭제)할 항목
act: 동작 구분 (아무것도 적지 않은 경우는 0: default 값 0으로 설정)
act = 0: 추가
act = 1: 항목 key에 존재하는 value 제거
act = 2: 항목 key를 삭제

반환값
act = 0, value가 이미 존재하는 경우: 'This word already exists.' 반환
act = 0, value가 없는 경우: 해당 key의 모든 value 반환
act = 1: value를 삭제한 후의 해당 key의 모든 value 반환
act = 2: key를 삭제한 후 dict의 모든 key를 반환
'''

'''
함수사용예시

dictionary = {'fruit': ['apple', 'banana', 'pineapple', 'melon', 'kiwi'],
  'animal':['dog','cat'],
  'snack': ['cookie','biscuit','sable'],
  'beverage':['juice','coffee','wine'],
  'city':['Daegu','Seoul','Busan']}
print(add_to_dict(dictionary,'animal','panda'))
print(add_to_dict(dictionary,'vehicle','car',0))
print(add_to_dict(dictionary,'fruit','apple'))
print(add_to_dict(dictionary,'fruit','kiwi',2))
print(add_to_dict(dictionary,'fruit','apple'))
print(add_to_dict(dictionary,'snack','sable',1))
'''

'''
실행 결과

['dog', 'cat', 'panda']
car
This word already exists.
['animal', 'snack', 'beverage', 'city', 'vehicle']
apple
['cookie', 'biscuit']
'''

#Code
def add_to_dict(dictionary,key,value,act=0):
    if act == 0:
        already = dictionary.get(key, False)
        if already == False:
            dictionary[key] = value
            return dictionary[key]
        else:
            if value in already:
                return 'This word already exists.'
            else:
                dictionary[key].append(value)
                return dictionary[key]

    elif act == 1:
        ref = dictionary[key].index(value)
        del dictionary[key][ref]
        return dictionary[key]

    elif act == 2:
        del dictionary[key]
        return list(dictionary.keys())


dictionary = {'fruit': ['apple', 'banana', 'pineapple', 'melon', 'kiwi'],
				'animal':['dog','cat'],
				'snack': ['cookie','biscuit','sable'],
				'beverage':['juice','coffee','wine'],
				'city':['Daegu','Seoul','Busan']}
print(add_to_dict(dictionary,'animal','panda'))
print(add_to_dict(dictionary,'vehicle','car',0))
print(add_to_dict(dictionary,'fruit','apple'))
print(add_to_dict(dictionary,'fruit','kiwi',2))
print(add_to_dict(dictionary,'fruit','apple'))
print(add_to_dict(dictionary,'snack','sable',1))
