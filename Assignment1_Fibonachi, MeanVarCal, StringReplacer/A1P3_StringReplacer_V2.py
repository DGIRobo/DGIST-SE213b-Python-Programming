# 문자열 치환 함수

'''
Description

문자열과 치환 하고자 하는 문자열을 입력 받아서 치환된 문자열을 반환하는 함수replaced(original_str, old_str, new_str, cnt)를 구현하시오.

함수동작
치환하고자 하는 문자열 original_str을 매개변수로 받음
origianl_str의 앞에서부터 old_str을 찾아서 new_str로 치환
주의: 치환은 cnt만큼만 수행하고 cnt가 -1인 경우는 모든 old_str을 치환함
매개변수
original_str: 치환하고자 하는 문자열
old_str: (str) original_str에서 바꾸고자 하는 문자열
new_str: (str) old_str을 치환할 문자열
cnt: (int : 기본값 -1로 지정) 치환할 횟수
반환값
(str) original_str에서 old_str을 찾아서 new_str로 cnt만큼 치환하여 만든 문자열
'''

'''
함수 실행 예시

orig = "The apple is delicious. The apple is red."
print(replaced(orig, "apple", "tomato"))
print(replaced(orig, "apple", "banana", 1))
'''

'''
실행 결과 예시

The tomato is delicious. The tomato is red.
The banana is delicious. The apple is red.
'''

# Code

def replaced(original_str, old_str, new_str, cnt = -1):
    count = 0
    str_making = original_str
    for alphabet in range(len(str_making)):
        if str_making[alphabet:alphabet + len(old_str)] == old_str:
            str_making = str_making[:alphabet] + new_str + str_making[alphabet + len(old_str):]
            count=count+1
            if cnt == -1: continue
            elif count == cnt: break

    if count < cnt:
        return "There aren't " + old_str + " three times!"

    return str_making

orig = "The apple is delicious. The apple is red."
print(replaced(orig, "apple", "tomato"))
print(replaced(orig, "apple", "banana", 2))
