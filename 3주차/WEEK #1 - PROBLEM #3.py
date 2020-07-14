'''
Description
사용자에게 성과 이름을 입력받아, 아래와 같은 형식으로 출력하는 프로그램을 작성할 것.

- 이름, 성
- 성, 이름
'''

'''
실행예시
Enter your last name: Bond
Enter your first name: James
James Bond
Bond , James
'''

last_name = str(input('Enter your last name: '))
first_name = str(input('\nEnter your first name: '))
print('\n',first_name, last_name)
print(last_name ,',', first_name)