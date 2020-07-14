# E-mail address 찾기

'''
Description

e-mail 주소는 id@website.(com/co.kr/net/ac.kr ..) 등의 양식을 갖고 있다. 주어진 문자열에서 e-mail 주소를 인식하여 리스트를 반환하는 getEmailAddr(txt)을 작성하시오.

getEmailAddr(txt) 함수

매개변수
txt: e-mail 주소가 0개 이상 포함되어 있는 문자열

반환값:
모든 e-mail 주소(문자열)를 포함한 리스트

함수의 동작
문자열에서 e-mail 주소를 찾아 리스트로 반환
단, e-mail 주소의 site 부분은 최소 하나의 . 문자를 포함
'''

'''
함수 사용예시

txt= "If you have any questions, please contact via abc@naver.com or abc@dgist.ac.kr"
print(getEmailAddr(txt))

txt= "No e-mail address aaa@bbb"
print(getEmailAddr(txt))
'''

'''
실행결과

['abc@naver.com', 'abc@dgist.ac.kr']
[]
'''

# Codes
import re

def getEmailAddr(txt):
    """return the list of id of e-mail"""
    emails = re.findall('[a-zA-Z0-9]{1,}@[a-z]{1,}[.]{1}[a-z.]{1,}', txt)
    return emails

if __name__ == '__main__':
	txt= "If you have any questions, please contact via abc@naver.com or abc@dgist.ac.kr"
	print(getEmailAddr(txt))

	txt= "No e-mail address aaa@bbb"
	print(getEmailAddr(txt))
