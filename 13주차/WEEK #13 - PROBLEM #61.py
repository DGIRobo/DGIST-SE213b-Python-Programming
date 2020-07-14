# 휴대폰 번호 찾기

'''
Description
문자열에서 휴대폰 번호를 추출하는 함수 phone_number(contents)를 작성할 것

phone_number(contents) 함수

매개변수
contents: 휴대폰 번호가 0개 이상 존재하는 임의의 문자열

반환값
휴대폰 번호 리스트

함수의 동작
contents 안에 포함된 모든 휴대폰 번호를 추출하여 리스트로 저장 후 반환
휴대폰 번호의 양식은 숫자3-숫자3 혹은 4-숫자4
'''

'''
함수 사용예시

print(phone_number("please call the 010-1234-5678 or 016-123-1234"))
print(phone_number("123456-7890 is not phone number."))
'''

'''
실행결과

['010-1234-5678', '016-123-1234']
[]
'''

# Codes
import re

def phone_number(contents):
    """return the list of phone number"""
    phoneNums = re.findall('[0-9]{3}-[0-9]{3,4}-[0-9]{4}', contents)
    return phoneNums

print(phone_number("please call the 010-1234-5678 or 016-123-1234"))
print(phone_number("123456-7890 is not phone number."))
