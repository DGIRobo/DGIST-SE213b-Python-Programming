# 문자열에서 문자 찾기

'''
Description

문자열은 str.index(x)라는 문자열 함수를 제공하고 있다. index()는 x 문자가 문자열에 존재하지 않는 경우에 ValueError를 발생시킨다. 문자열 함수를 대신할 수 있는 함수 index()를 구현하시오.

주의

다양한 find, rfind, index, rindex 함수를 이용하지 말것
대소문자를 구분하지 않고 찾음

Hint

함수동작
함수는 sentence(문자열)과 찾고자하는 x라는 문자열을 인자로 받아서
sentence 안에 x라는 문자열이 대소문자 구분없이 처음 나오는 index 값을 반환
만약 x라는 문자열이 sentence 문자열에 없는 경우 -1을 반환

매개변수
sentence: (문자열) 검색하고자 하는 문자열
x : (문자열) sensntace 안에서 찾고자 하는 문자열

반환값
(int) sentence 문자열에서 x라는 문자열이 나오는 첫번째 index 반환 (없는 경우 -1 반환)
'''

'''
함수 사용 예시

print(index("First, solve the problem. Then, write the code.", "first"))
print(index("Without requirements or design, programming is the art of adding bugs to an empty text file.", "first"))
print(index("Computers are good at following instructions, but not at reading your mind.", "m"))
print(index("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.", "psychopath"))
'''

'''
실행결과

0
-1
2
78
'''

# Code
def index(sentence, x):
    reference = sentence.lower()
    pivot = x.lower()
    for alphabet in range(len(reference)):
        if reference[alphabet:alphabet + len(x)] == x:
            return alphabet
    return -1

print(index("First, solve the problem. Then, write the code.", "first"))
print(index("Without requirements or design, programming is the art of adding bugs to an empty text file.", "first"))
print(index("Computers are good at following instructions, but not at reading your mind.", "m"))
print(index("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.", "psychopath"))
