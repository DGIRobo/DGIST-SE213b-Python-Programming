#야구 게임 클래스

'''
Description

주의: 파이참 또는 pythontutor.com 등 에서 실행해보고 여기서는 제출만 가능함.

야구 게임은 다음과 같다.

1. 컴퓨터는 무작위로 숫자 3개를 선택하여 순서대로 저장한다. (3개의 숫자는 중복되면 안된다.)
2. 사용자로부터 3개의 숫자를 입력받아 저장한 숫자와 비교하여 순서와 숫자가 모두 동일한 경우, "You got it!!"을 출력하고 프로그램을 종료한다.
3. 사용자로 부터 입력받은 숫자 중에 순서와 값이 모두 일치하는 개수만큼 strike로 판정한다.
4. 순서는 틀렸지만 값이 존재하는 개수만큼 ball로 판정한다.
5. 사용자가 입력한 3개의 숫자의 순서와 값이 무작위로 발생시킨 숫자와 동일한 경우에, You got it!을 출력한다.
예시 랜덤하게 선택된 3개의 숫자가 다음 순으로 저장되었다고 가정한다.
0, 5, 2
사용자가 1 ,3, 4를 입력시 결과: 0S 0B
사용자가 5, 2, 0를 입력시 결과: 0S 3B
사용자가 0 ,6 , 5를 입력시 결과: 1S 1B
사용자가 0 , 5 , 6를 입력시 결과: 2S 0B
사용자가 0, 5, 2를 입력시 결과: You got it!!

tip: 테스트 때는 seed값을 고정해서 진행하면 편함
'''

'''
class BaseballGame

__init__(self, seed_num=None)

함수동작
매개변수 seed_num을 가지고 random 모듈의 seed값을 seed_num으로 고정함(week10-65참조.)
randrange를 사용하여 0-9사이의 숫자 3개를 list로 instance variable로 저장
주의: 3개의 숫자는 모두 달라야함

매개변수
self: instance 자신
seed_num (int: 디폴트 값은 None)

반환값
없음 - __init__() 함수는 반환값을 갖지 않음
'''

'''
input_check()

함수동작
"What is your guess: "를 출력후 사용자로 부터 3개의 숫자를 입력 받은 결과를 문자열 인자(input_data)로 받는다. 3개의 숫자는 컴마로 구분되어 있다고 가정한다. (예: "0 , 3, 8")
입력 받은 문자열에서 컴마로 분할하고, 공백을 제거한뒤, 3개의 숫자를 추출함
입력 결과 중 숫자가 아닌 문자가 있거나 중복되지 않는 숫자의 개수가 3개가 아닌경우 None을 반환
3개의 숫자가 모두 정상으로 확인 된 경우 list에 각 숫자를 요소로 저장한 뒤 반환

매개변수
없음. ** class method

반환값
None (문자열 아님/키워드임) : 입력값에 문제가 있는 경우
숫자 3개가 들어가 있는 list : 입력값에 문제가 없는 경우
'''

'''
check_count(self, usr)

함수동작
사용자가 input_check()함수를 통해서 (3개의 사용자 입력 숫자가 저장된) 생성된 리스트를 인자로 받아서,
instace가 생성될 때,(새로운 게임이 생성될때) 설정된 3개의 난수가 저장된 리스트와 비교하여 strike, ball을 판정하여 문자열로 반환
3개 리스트의 순서와 숫자가 모두 동일한 경우 "3S 0B" 반환
순서와 숫자에 따라 f"{n}S {m}B" 반환 (예: 0S 0B, 2S 1B, 0S 3B)
숫자만 맞고 순서가 다른 개수: m
숫자와 순서가 모두 같은 개수: n

매개변수
usr (list) : 사용자가 입력한 숫자 3개에 대한 리스트

반환값
strike, ball을 판정하는 문자열
'''

'''
실행 예시 1
if __name__ == "__main__":
    new_game1 = BaseballGame(1)
    new_game1.play()
'''

'''
실행 결과 1
What is your guess: 2, 9 , 1
You got it!!
'''

'''
실행 예시 2
if __name__ == "__main__":
    new_game2 = BaseballGame(2)
    new_game2.play()
'''

'''
실행 결과 2
What is your guess: a, 0, 1
Your input is not valid.
What is your guess: 1, 0, 1
Your input is not valid.
What is your guess: 1, 2, 3, 4, 5
Your input is not valid.
What is your guess: 1,2, 3
0S 1B
What is your guess: 5, 1, 2
1S 1B
What is your guess: 5, 0, 1
0S 3B
What is your guess: 0, 1,   5
You got it!!
'''

#Code
class BaseballGame:
    def __init__(self, seed_num=None):
        import random
        random.seed(seed_num)
        self.threeNums = []
        while len(self.threeNums) < 3:
            candidate = random.randrange(0, 9)
            if candidate not in self.threeNums:
                self.threeNums.append(candidate)

    def input_check():
        input_data = input('What is your guess: ')
        guess = input_data.split(', ')
        for i in range(len(guess)):
            if guess[i].isnumeric():
                guess[i] = int(guess[i])
            else: return None
        return guess

    def check_count(self, usr):
        n = 0
        m = 0
        for i in range(len(usr)):
            if self.threeNums[i] == usr[i]:
                n += 1
        for i in range(len(usr)):
            if usr[i] in self.threeNums:
                m += 1
        m = m - n
        return f"{n}S {m}B"

    def play (self):
        while True:
            usr = BaseballGame.input_check()
            if not usr:
                print("Your input is not valid.")
                continue
            else :
                result = self.check_count(usr)
            if result == "3S 0B":
                print("You got it!!")
                break
            else:
                print(result)

if __name__ == "__main__":
    new_game = BaseballGame()
    new_game.play()
