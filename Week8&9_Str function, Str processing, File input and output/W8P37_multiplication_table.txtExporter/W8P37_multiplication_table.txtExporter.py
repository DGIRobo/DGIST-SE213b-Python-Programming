# 구구단 파일 출력

'''
Description

이전 실습 문제인 구구단 전체 출력을 화면이 아닌 인자로 넘겨 받은 텍스트 파일에 출력해 보시오. 본문의 코드를 실행하면 파일로 부터 값을 읽어와서 화면에 출력함.

함수 write_file(f_name) 는 반환값이 없는 함수로 인자로 받은 파일이름(예:multiplication_table.txt)으로 파일을 열고 구구단을 파일에 출력후 종료되는 함수를 작성하시오.

Lab #6에서 사용한 함수를 복사해서 재사용 가능합니다. 다만, 출력형태를 아래와 같이 바꿔야합니다. 출력시, string format(or f String)을 이용하여 최소길이를 3으로 주면 해결됩니다.

Hint

함수동작
구구단을 파일(f_name)에 출력

매개변수
f_name: (str) 파일 이름

반환값
없음(None)
'''

'''
실행결과 함수 read_file(f_name)을 통해서 저장된 파일 내용을 출력함

  1  2  3  4  5  6  7  8  9
  2  4  6  8 10 12 14 16 18
  3  6  9 12 15 18 21 24 27
  4  8 12 16 20 24 28 32 36
  5 10 15 20 25 30 35 40 45
  6 12 18 24 30 36 42 48 54
  7 14 21 28 35 42 49 56 63
  8 16 24 32 40 48 56 64 72
  9 18 27 36 45 54 63 72 81
'''

# Code
""" 파일에 구구단을 출력하는 함수 wirte_file을 작성하시오. """
def write_file(f_name):
    with open(f_name, "wt") as f:
        for left in range(1,10):
            for right in range(1, 10):
                print('%3d' % (right*left), end='', file=f)
            print("", file=f)

def read_file(f_name):
    with open(f_name, "rt") as f:
        print(f.read())

f_name = "multiplication_table.txt"
write_file(f_name)
read_file(f_name)
