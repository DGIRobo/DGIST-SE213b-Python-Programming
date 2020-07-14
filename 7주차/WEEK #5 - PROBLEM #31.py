# 사전

'''
Description

단어 리스트에서 주어진 알파벳으로 시작하는 단어를 찾는 함수 search(alphabet,word_list)와 사전 순서로 정렬하는 함수 dictionary(word_list)를 구현하여라.

search(alphabet,word_list)
함수동작
단어들이 리스트로 저장되어 있는 word_list를 매개변수로 받아서,
단어의 첫 글자가 또다른 매개변수 alphabet과 동일한 경우
결과 리스트에 저장하고 출력 후 종료
매개변수
alphabet: (str) 알파벳 1글자
word_list: (list) 단어들이 저장되어 있는 리스트
반환값
없음
dictionary(word_list)
함수동작
단어들이 리스트로 저장되어 있는 word_list를 매개변수로 받아서,
알파벳의 오른 차순으로 정렬한 뒤 출력 후 종료
매개변수
word_list: (list) 단어들이 저장되어 있는 리스트
반환값
없음
'''

'''
함수 사용 예시

example = ['cap','gray','bear','book','pink','purple','apple','goat','doctor']
search('g',example)
dictionary(example)
'''

'''
실행결과

['gray', 'goat']
['apple', 'bear', 'book', 'cap', 'doctor', 'goat', 'gray', 'pink', 'purple']
'''

# Code

def search(alphabet,word_list):
    search_list = []
    for val in word_list:
        if alphabet == val[0]:
            search_list.append(val)
    print(search_list)

def dictionary(word_list):
    word_list.sort()
    print(word_list)

example = ['cap','gray','bear','book','pink','purple','apple','goat','doctor']
search('g',example)
dictionary(example)
