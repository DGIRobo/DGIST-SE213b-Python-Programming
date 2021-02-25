# 전화번호부

'''
Description

전화번호부
(예시: phonebook.txt 내부
     Alice, 01062601177
       Bob, 01184888723
     Carol, 01088889997
     Chuck, 01692712293
     Craig, 01900890072
       Dan, 01079210097
      Erin, 01076723465
       Eve, 01069238467
    Faythe, 01966116070
     Frank, 01988117664
     Grace, 01966317792
     Heidi, 01193934282
   Mallory, 01177128982
     Oscar, 01167336367
     Peggy, 01070118186
     Sybil, 01096239462
     Trent, 01067662261
     Trudy, 01085117490
    Victor, 01082006794
    Walter, 01067008486
     Wendy, 01097926600
)에서 전화번호를 읽어서 사전에 저장하는 함수 read_phonebook(filename = 'phonebook.txt') 를 작성하시오.
사전에 저장되어 있는 전화번호를 이름으로 검색하는 함수 find_phonenumber(phonebook, name) 를 작성하시오.
* 주의전화번호부에 동명인은 없다고 가정


함수 read_phonebook()

함수동작
파일 이름을 매개변수로 받아서 파일의 전화번호 데이터
(10칸의 공간에 오른쪽 정렬되어 있는 이름과 숫자 11자리로 이루어져있는 전화번호)를
읽어와서 사전에 이름을 키 값으로 전화번호는 000-0000-0000 형식의 문자열로 value에 저장
전화번호부에 기록된 사람수를 출력 ('{n} people on the list')

매개변수
filename: (str) 전화번호가 저장되어 있는 파일이름

반환값
(dict) {'이름': '010-1111-2222', } 와 같은 사전


함수 find_phonenumber()

함수동작
전화번호부와 이름을 매개변수로 받아서 해당 전화번호를 문자열로 반환

매개변수
phonebook: (dict) 사전 형태로 저장되어 있는 전화번호부
name: (str) 전화번호를 검색하고자 하는 사람이름

반환값
(str) 찾고자 하는 사람의 전화번호 반환
전화번호부에 name에 해당하는 사람이 없는 경우, '{name} is not on the list.' 반환
'''

'''
함수 사용예시

my_phonebook = read_phonebook('phonebook.txt')

#ex) my_phonebook = {'Alice':'010-1111-2222'}
print(find_phonenumber(my_phonebook, 'Alice'))
print(find_phonenumber(my_phonebook, 'Bob'))
'''

'''
실행결과

17 people on the list.
010-1111-2222
Bob is not on the list.
'''

# Code
def read_phonebook(file_name='phonebook.txt'):
    phonenumber_dict = {}
    with open(file_name, 'rt') as f:
        phonebook = f.read()
    phonenumbers = phonebook.split()
    for n in range(int(len(phonenumbers)/2)):
        phonenumber = phonenumbers[2*n+1][0:3] + '-' + phonenumbers[2*n+1][3:7] + '-' + phonenumbers[2*n+1][7:]
        phonenumber_dict[phonenumbers[2*n][:-1]] = phonenumber
    print(f'{n+1} people on the list')
    return phonenumber_dict

def find_phonenumber(phonebook, name):
    finding = phonebook.get(name, f'{name} is not on the list')
    return finding

my_phonebook = read_phonebook('phonebook.txt')

#my_phonebook = {'Alice':'010-1111-2222'}
print(find_phonenumber(my_phonebook, 'Alice'))
print(find_phonenumber(my_phonebook, 'Bob'))
