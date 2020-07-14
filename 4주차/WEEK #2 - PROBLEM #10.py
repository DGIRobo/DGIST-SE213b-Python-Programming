# 성적표 프로그램

'''
Description
사용자에게 성적을 입력받아서, 해당되는 학점을 출력하도록 작성할 것. 단, 성적이 90점 ~ 100점일 경우, A+ 부여한다. 성적이 80점 ~ 89점일 경우, B+ 부여한다. 성적이 70점 ~ 79점일 경우, C+ 부여한다. 성적이 69점 밑일 경우, F 부여한다.
'''

'''
실행예시
Enter your score: 100
Your grade is A+
'''

# Code
score = float(input('Enter your score: '))

if score>=90:
    print('Your grade is A+')
elif score>=80:
    print('Your grade is B+')
elif score>=70:
    print('Your grade is C+')
elif score<=69:
    print('Your grade is F')