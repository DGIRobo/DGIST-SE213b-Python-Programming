# 전화번호 추가

'''
Description

이름과 전화번호를 사용자로부터 입력받아 저장하는 프로그램을 만드시오. 단, 사전(dict)을 사용할 것.
number_list = { '홍길동' : '010-1234-5678' }
단, 입력하려는 번호의 이름이 이미 있을 경우 아래와 같은 오류 메시지를 출력해야함.

number_adder 함수

함수동작
사전 인자 num_list에 name을 key로 num을 value로 하는 값을 추가하여 사전을 반환 함수
key인 name이 기존의 사전에 이미 존재하는 경우 문자열을 (name is already in num_list.) 반환

매개변수
num_list: (dict) 이름과 전화번호가 쌍으로 들어있는 사전
name : (문자열) 새롭게 입력받은 사람의 이름
num: (문자열) 새롭게 입력받은 사람의 전화번호

반환값
name, num이 추가된 사전 파일
단, 이미 사전에 있는 사람이 인자로 들어오는 경우는 문자열로 사전에 이미 있다는 내용을 반환
'''

'''
실행예시

Enter a name : 홍길동
Enter the phone number : 010-1234-5678
홍길동 is already in num_list.

Enter a name : 김삿갓
Enter the phone number : 010-5678-1234
{'홍길동': '010-1234-5678', '김삿갓': '010-5678-1234'}
'''

# Code
def number_adder(num_list, name, num):
    # Insert your code
    if name in num_list:
        return name + ' is already in num_list.'
    else:
        num_list[name] = num
        return num_list

number_list = {'홍길동': '010-1234-5678'}

# if 구문을 지우지 마시오.
if __name__ == '__main__':
    name = input('Enter a name : ')
    num = input('Enter the phone number : ')
    print(number_adder(number_list, name, num))
