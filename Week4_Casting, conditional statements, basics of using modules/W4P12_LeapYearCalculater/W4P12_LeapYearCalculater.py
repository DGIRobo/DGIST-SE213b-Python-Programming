# Calculate the leap year

'''
Description
2월 29일은 4년에 한 번 돌아오는데 이렇게 2월 29일이 있는 해를 윤년(leap year)라고 합니다. 사용자에게 연도(year)를 입력받고 입력받은 연도가 윤년인지 아닌지 판단하는 프로그램을 작성할 것. 윤년을 판정하는 조건은 아래와 같다.

1. 기본적으로 연도 수가 4로 나누어떨어지면 윤년이다.
2. 그러나 100으로 나누어떨어지는 해는 윤년이 아니다.
3. 그러나 400으로 나누어 떨어지는 해는 윤년이다.
'''

'''
실행예시 1
Enter the year:2000
This year is a leap year.
'''

'''
실행예시 2
Enter the year:2019
This year is not a leap year.
'''

'''
실행예시 3
Enter the year:2020
This year is a leap year.
'''

# Code
year = int(input('Enter the year: '))
if year%400 == 0:
    print('This year is a leap year.')
elif year%100 ==0:
    print('This year is not a leap year.')
elif year%4 == 0:
    print('This year is a leap year.')
else:
    print('This year is not a leap year.')