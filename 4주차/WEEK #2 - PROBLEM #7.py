# 2 혹은 3으로 나누어지는지 확인
'''
Description
사용자에게 정수를 입력받은 후, 그 수가 2 혹은 3으로 나눠지는지
혹은 2, 3으로 모두 나눠지는지 출력하는 프로그래을 작성하시오. (굵은 글씨는 사용자의 키보드 입력을 나타냄)

problem #7과 problem #8은 어떻게 if문을 구성하면 가장 간단하게 구현할 수 있는지 
생각해볼 것.
'''

'''
실행예시 1
Enter an integer number: 42
42 is divisible by 2.
42 is divisible by 3.
'''

'''
실행예시 2
Enter an integer number: 8
8 is divisible by 2.
'''

'''
실행예시 3
Enter an integer number: 9
9 is divisible by 3.
'''

'''
실행예시 4
Enter an integer number: 23
'''

# Code
number = int(input('Enter an integer number: \n'))
if  number % 2 == 0:
    print(number, 'is divisible by 2.')
    if number % 3 ==0:
        print(number, 'is divisible by 3.')
elif number % 3 == 0:
        print(number, 'is divisible by 3.')
