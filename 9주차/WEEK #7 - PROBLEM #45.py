# 단어의 출현 횟수

'''
Description

주어진 text에서 2번이상 나오는 단어와 몇번 나왔는지 반환하는 함수를 작성하시오. 이 때 단어와 빈도를 원소로 가지는 튜플들의 리스트를 반환할 것.

dic()함수

함수동작
문자열을 인자로 받아서 공백으로 구분된 단어를 만들고,
문자열에서 그 단어가 나오는 빈도수를 계산하여 ('단어', 빈도수) 쌍의 튜플을 만들고
빈도수가 2이상인 튜플들을 리스트에 저장하여 반환

매개변수
words:(문자열) 공백으로 단어가 구분된 문자열

반환값
(list) 리스트의 엘리먼트는 단어와 빈도수로 이루어진 튜플로 이루어짐
빈도수가 2이상인 단어만으로 구성 [ ('you', 3), ]
'''

'''
함수 사용 예시

print(dic('you learn you learn you'))
'''

'''
실행결과

[('learn', 2), ('you', 3)]
'''

# Code
text="""
you are learning a programming class
today you have to learn dictionary grammar
i hope you will learn happily
"""

def dic(words):
    word_list = words.split()
    count = {}
    same_word = []
    for item in word_list:
        count[item] = count.get(item, 0) + 1
    for item in count:
        if count.get(item) >= 2:
            key = count.get(item)
            same_word.append((item, key))
    return same_word

print(dic(text)) #text안의 단어들은 공백으로 구분됨
