# 학생관리 시스템

'''
Description

학생관리 함수 manage_students(st_list)와 이를 관리하는 함수 insert(st_list, student), modify_major(st_list, modi_SN, modi_major), delete(st_list, del_SN)을 작성할 것
is_valid(st_list, SN)함수는 수정 할 필요 없음

** 주의: 실행은 파이참 등을 활용하고, 혹시 온라인 환경밖에 시험 환경이 안되는경우에는 pythontutor 사이트를 활용할 것.
'''


'''
is_valid(st_list, SN) 함수

함수동작
인자 SN의 존재 여부
list에 동일한 SN이 존재하면 True 반환
그렇지 않으면 False 반환

매개변수
st_list: 학생 정보 리스트
SN: 학번

반환값
True, False
'''


'''
manage_students(st_list) 함수

함수동작
옵션에 따른 함수 호출
- 1: 학생 추가
- 2: 학생 수정
- 3: 학생 삭제
사용자가 0을 입력하면 학생 정보를 모두 출력하고 프로그램 종료
옵션 이외의 숫자를 입력하면 "Invalid value." 를 출력하고, 다시 입력받음

매개변수
st_list: 학생 정보 리스트

반환값
없음(None)
'''


'''
insert(st_list, student) 함수

함수동작
리스트에 student의 학번과 동일한 학생이 있으면 에러메시지 출력
그렇지 않으면:
student를 리스트 마지막에 추가
해당 학생 정보 출력

매개변수
st_list: 학생 정보 리스트
student: 추가할 학생정보 (dic 자료형)

반환값
없음(None)
'''


'''
modify_major(st_list, modi_SN, modi_major) 함수

함수동작
해당 modi_SN 학생의 전공 수정
리스트에 modi_SN과 동일한 학생이 있으면 :
- 해당 학생의 전공 수정
- 해당 학생 정보 출력
그렇지 않으면: 에러메시지 출력

매개변수
st_list: 학생 정보 리스트
modi_SN: 수정할 학번
modi_major: 수정할 전공

반환값
없음(None)
'''


'''
delete(st_list, del_SN) 함수

함수동작
해당 del_SN 학생 삭제
리스트에 del_SN과 동일한 학생이 있으면
- 해당 학생 삭제
- 모든 학생 정보 출력
그렇지 않으면: 에러메시지 출력

매개변수
st_list: 학생 정보를 가지는 리스트
del_SN: 삭제할 학번

반환값
없음(None)
'''


'''
실행결과 (정상 추가)

[1] Insert      [2] Modify      [3] Delete      [0] Exit: 1
[Insert] Student number: 2018
[Insert] Name: Kang
[Insert] Major: Science
{'SN': 2018, 'name': 'Kang', 'major': 'Science'}
'''


'''
실행결과 (동일한 학번 추가 할 때)

[1] Insert      [2] Modify      [3] Delete      [0] Exit: 1
[Insert] Student number: 1234
[Insert] Name: Kang
[Insert] Major: Science
[ERROR!!!] There is a student with the same SN.
'''


'''
실행결과 (정상 수정)

[1] Insert      [2] Modify      [3] Delete      [0] Exit: 2
[Modify] Student number: 8282
[Modify] Major: Biology
{'SN': 8282, 'name': 'Park', 'major': 'Biology'}
'''


'''
실행결과 (존재하지 않는 학생 수정 할 때)

[1] Insert      [2] Modify      [3] Delete      [0] Exit: 2
[Modify] Student number: 9999
[Modify] Major: Biology
[ERROR!!!] There is no student with SN 9999
'''


'''
실행결과 (정상 삭제)

[1] Insert      [2] Modify      [3] Delete      [0] Exit: 3
[Delete] Student number: 5678
[{'SN': 1234, 'name': 'Kim', 'major': 'Computer'}, {'SN': 1004, 'name': 'Lee', 'major': 'English'}, {'SN': 8282, 'name': 'Park', 'major': 'Math'}]
'''


'''
실행결과 (존재하지 않는 학생 삭제 할 때)

[1] Insert      [2] Modify      [3] Delete      [0] Exit: 3
[Delete] Student number: 3693
[ERROR!!!] There is no student with SN  3693
'''

# Code
def is_valid(st_list, SN):
    for st in st_list:
        if st['SN'] == SN:
            return True
    return False

def insert(st_list, student):
    if not(is_valid(st_list, student['SN'])):
        st_list.append(student)
        print(student)
    else:
        print('[ERROR!!!] There is a student with the same SN.')

def modify_major(st_list, modi_SN, modi_major):
    if is_valid(st_list, modi_SN):
        for st in st_list:
            if st['SN'] == modi_SN:
                st['major'] = modi_major
                print(st)
                break
    else:
        print(f'[ERROR!!!] There is no student with SN {modi_SN}')

def delete(st_list, del_SN):
    if is_valid(st_list, del_SN):
        for st in st_list:
            if st['SN'] == del_SN:
                del st_list[st_list.index(st)]
                print(st_list)
                break
    else:
        print(f'[ERROR!!!] There is no student with SN  {del_SN}')

def manage_students(st_list):
    option = int(input('[1] Insert \t [2] Modify \t [3] Delete \t [0] Exit: '))
    while option != 0:
        if option == 1:
            student = {}
            student['SN'] = int(input('[Insert] Student number: '))
            student['name'] =  input('[Insert] Name: ')
            student['major'] =  input('[Insert] Major: ')
            insert(st_list, student)

        elif option == 2:
            sn = int(input('[Modify] Student number: '))
            modi_major = input('[Modify] Major: ')
            modify_major(st_list, sn, modi_major)

        elif option == 3:
            sn = int(input('[Delete] Student number: '))
            delete(st_list, sn)
        else:
            print('Invalid value.')

    else:
        print(st_list)

# Don't delete the code below
if __name__ == '__main__':
    s1 = {'SN':1234, 'name':'Kim', 'major':'Computer'}
    s2 = {'SN':5678, 'name':'Yoon', 'major':'Robot'}
    s3 = {'SN':1004, 'name':'Lee', 'major':'English'}
    s4 = {'SN':8282, 'name':'Park', 'major':'Math'}
    students = [s1, s2, s3, s4]

    manage_students(students)
