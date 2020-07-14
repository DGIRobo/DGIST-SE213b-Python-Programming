#나만의 사전 만들기

'''
Description

영어 공부에 사용되는 단어장을 만드는 함수 make_dictionary(document)를 작성하오.
논문, 영화자막 등 영어로 작성되어 있는 문자열(document)을 parameter로 받아서 영어 단어를 분리하고 웹사전으로 부터 단어의 뜻을 가져와서 key:단어 value:뜻으로 구성된 사전을 만드시오.
http://10.180.2.80/dict.html?query=단어 로 이루어진 url을 부르면, 단어의 뜻을 가져올 수 있습니다.

주의: 외부에서 확인시 주소는 114.71.103.80를 사용하나 코드에서는 그대로 10.180.2.80을 사용함.
'''

'''
make_dictionary(document) 함수

함수동작
문자열(document)를 받아서 마침표(".")와 쉼표(",")를 제거하고 공백(space)를 기준으로 단어를 나눔.
(영단어의 복수형이나 동사의 변형등은 고려하지 말고 공백으로 분할한 단어를 그래도 사용함.)
각 단어(word)를 http://10.180.2.80/dict.html?query=word 형태로 구성된 url을 통해 definition에 해당하는 부분을 크롤링함.
단어(word)와 크롤링한 definition을 사전형태로 만들어서 저장하고 이를 반환함.

매개변수
document: (str) 영어로 되어 있는 문장

반환값
(dict) 단어와 단어의 뜻으로 이루어진 사전형 데이터 반환
'''

'''
함수 사용예시

data = "first, solve the problem. then, write the code."
print(make_dictionary(data))
'''

'''
실행결과 (사전의 순서는 달라질수 있음, 사전에 단어가 다 들어있고, 뜻이 다 들어있으면 OK)

{'problem': 'A question proposed for solution; a matter stated for\n   examination or proof; hence, a matter difficult of solution or\n   settlement; a doubtful case; a question involving doubt.', 'write': 'To set down, as legible characters; to form the\n   conveyance of meaning; to inscribe on any material by a suitable\n   instrument; as, to write the characters called letters; to write\n   figures.', 'then': 'At that time (referring to a time specified, either past or\n   future).', 'solve': 'To explain; to resolve; to unfold; to clear up (what is\n   obscure or difficult to be understood); to work out to a result or\n   conclusion; as, to solve a doubt; to solve difficulties; to solve a\n   problem.', 'code': 'A body of law, sanctioned by legislation, in which the rules\n   of law to be specifically applied by the courts are set forth in\n   systematic form; a compilation of laws by public authority; a digest.', 'the': 'See Thee.', 'first': 'Preceding all others of a series or kind; the ordinal of\n   one; earliest; as, the first day of a month; the first year of a reign.'}
'''

#Code
from urllib.request import urlopen
import re

def make_dictionary(document):
    word_dictionary = {}
    word_list = document.split()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip(',.')
        with urlopen(f'http://10.180.2.80/dict.html?query={word_list[i]}') as f: #내부접속시 http://10.180.2.80/dict.html?query={word_list[i]}, 외부접속시 http://114.71.103.80/dict.html?query={word_list[i]}
            allTxt = f.read().decode('utf-8')
            definition = re.findall('<tr><td>Definition: </td><td>[\D0-9]+</td>', allTxt)
            word_dictionary[word_list[i]] = definition[0][29:-5]
    return word_dictionary

if __name__ == '__main__':
    data = "first, solve the problem. then, write the code."
    print(make_dictionary(data))
    data = "other"
    print(make_dictionary(data))
