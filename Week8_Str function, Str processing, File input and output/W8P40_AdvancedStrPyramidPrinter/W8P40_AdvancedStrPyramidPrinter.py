# 문자열 피라미드

'''
Description

문자열 피라미드를 만드는 pyramid(char, n, alignment=-1) 함수를 구현하시오.

같은 동작을 하는 프로그램을 문자열 서식화를 이용하지 않고 만들어보고, 문자열 서식화를 이용해서 만들어 보면 도움이 됨.

함수동작
피라미드 출력
   - 표시하고자 하는 문자(char)와 행(n)을 인자로 받아서 n줄 만큼 char를 피라미드 형태로 출력
   - 피라미드 출력은 week4의 21번과 동일하나 alignment값에 따라서 정렬함.
   - char이 한글자 이상인 경우 None를 반환.

매개변수
char: 한 글자를 포함한 문자열
   - 한 글자가 아닌 경우에는 반환값에 나타난대로 None을 반환해야 함
n: 0 이상의 정수
   - 문자열 피라미드를 몇 칸에 맞추어서, 그리고 몇 줄에 걸쳐 만들 것을 지정
alignment: -1, 0, 1 중 하나의 값
   - -1: 왼쪽에 char를 맞추어 문자열 피라미드를 만듦 (기본값)
   - 0: 가운데에 char를 맞추어 문자열 피라미드를 만듦
   - 1: 오른쪽에 char를 맞추어 문자열 피라미드를 만듦

반환값
문자열: 아래 조건에 맞춘 문자열 피라미드를 포함하는 문자열
   -문자열 char에 포함된 문자의 수가 1이 아닐 때: None (문자열 'None'이 아닌 None값)
   -문자열 cahr에 포함된 문자의 수가 1일 때: n개의 줄을 가지는 문자열을 반환함
   -1번째 줄에 char 1개, 2번째 줄에 char 2개, ..., n번째 줄에 char를 n개 포함
   -각 줄은 (공백을 포함한) n개의 문자열로 만드는데, 이 때 char들을 alignment의 값에 따라 포함함. alignment의 의미는 인자에 있는 내용을 참고할 것.

주의
왼쪽 또는 가운제 정렬인 경우, 오른쪽에 빈 공간이 있어야함
'''

'''
함수 사용 예시

print("Output of pyramid('**', 3)")
print(pyramid('**', 3))
print("Output of pyramid('+', 3)")
print(pyramid('+', 3))
print("Output of pyramid('*', 5)")
print(pyramid('*', 5))
print("Output of pyramid('*', 5, 0)")
print(pyramid('*', 5, 0))
print("Output of pyramid('*', 5, 1)")
print(pyramid('*', 5, 1))
'''

'''
실행결과

Output of pyramid('**', 3)
None
Output of pyramid('+', 3)
+
++
+++

Output of pyramid('*', 5)
*
**
***
****
*****

Output of pyramid('*', 5, 0)
  *
 **
 ***
****
*****

Output of pyramid('*', 5, 1)
    *
   **
  ***
 ****
*****
'''

#Code

def pyramid(char, n, alignment=-1):
    """Return text pyramid"""
    result = ''
    space = ' '
    if len(char) == 1:
        if alignment == -1:
            for row in range(n):
                result = result + char*(row+1) + space*(n-row-1) + '\n'

        elif alignment == 0:
            for row in range(n):
                if (n-row)%2 == 0:
                    result = result + space*int((n-row-2)/2) + char*int(row+1) + space*int((n-row)/2) + '\n'
                else:
                    result = result + space*int((n-row-1)/2) + char*(row+1) + space*int((n-row-1)/2) + '\n'

        else:
            for row in range(n):
                result = result  + space*(n-row-1) + char*(row+1) + '\n'
        return result

    else: return None

print("Output of pyramid('**', 3)")
print(pyramid('**', 3))
print("Output of pyramid('+', 3)")
print(pyramid('+', 3))
print("Output of pyramid('*', 5)")
print(pyramid('*', 5))
print("Output of pyramid('*', 5, 0)")
print(pyramid('*', 5, 0))
print("Output of pyramid('*', 5, 1)")
print(pyramid('*', 5, 1))
