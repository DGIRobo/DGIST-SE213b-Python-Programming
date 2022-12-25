# 숫자 맞추기 게임

'''
Description
프로그램 내부에서 0-99사이의 정수 중 하나를 random하게 정하고, 이것을 사용자가 맞추는 게임을 작성하시오.

random 모듈의 random.randrange() 함수를 사용하시오.

주의: 파이참 또는 pythontutor.com 등 에서 실행해보고 여기서는 채점만 가능함.


함수 guess_number() 설명
동작
프로그램을 실행하면, 난수 하나를 생성하고, 사용자에게 숫자 하나를 입력 받음
입력된 숫자와 생성된 난수를 비교하여 난수보다 크거나 작은 경우 각각 "Too big!", "Too small!"을 출력하고 사용자로 부터 다시 숫자를 입력 받음
입력된 숫자와 생성된 난수를 비교하여 같은 경우 "You got it!"을 출력하고 종료

인자 seed_num: 해당 값을 seed로 random을 수행한다.

반환값 없음
'''

'''
아래는 컴퓨터가 발생한 난수가 27인 경우의 실행 예시임. (숫자는 사용자가 입력한 값임)

Enter your guess: 50
Too big!
Enter your guess: 25
Too small!
Enter your guess: 37
Too big!
Enter your guess: 28
Too big!
Enter your guess: 24
Too small!
Enter your guess: 26
Too small!
Enter your guess: 27
You got it!
'''

# Codes
import random

def guess_number(seed_num=None):
    """Generate a random and tell user whether their guessed number is correct"""
    """ seed_num으로 seed값을 고정 후 진행 """
    random.seed(seed_num)
    randNum = random.randint(0, 100)
    while True:
        guess = int(input('Enter your guess: '))
        if guess == randNum:
            print('You got it!')
            break
        elif guess > randNum:
            print('Too big!')
            continue
        elif guess < randNum:
            print('Too small!')
            continue

if __name__ == '__main__':
    guess_number()
