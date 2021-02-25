# 경로 개수 계산

'''
Description

n*n 맵을 입력 받아 시작점 0,0에서 종점 n-1, n-1까지 도달할 수 있는 경로의 개수를 반환하는 함수 calcPath()를 작성할 것

이동은 오른쪽, 아래쪽으로만 할 수 있으며, 해당 x, y 좌표에 나와있는 숫자만큼 한방향으로 이동해야한다.

이동후 맵을 벗어난 경우에는 더이상 경로가 존재하지 않는다고 설계한다.

재귀 함수 calcPath(inserted_map, x, y)를 작성하시오. (반드시 재귀방법을 이용하여 문제를 해결하시오.)
'''

'''
calcPath(inserted_map, x, y) 함수

함수동작
오른쪽 혹은 아래쪽으로 x, y 좌표에 나온 숫자만큼 이동
종점까지 도착하는 경우의 수가 없으면 0을, 있다면 가능한 경우의 수 반환
이동후 맵을 벗어난 경우도 0이라고 고려해야함.

매개변수
inserted_map: (2중 리스트) 입력된 n*n 맵으로 맵의 값은 이동해야하는 칸 수가 적혀있다.
숫자에 의해서 아래 또는 오른쪽 방향으로만 해당 숫자만큼 이동함
x: (int) x 좌표
y: (int) y 좌표

반환값
(int) 종점까지 도달할 수 있는 경우의 수
'''

'''
실행예시

input_map = [[1,2,9,4,9],
             [9,9,9,9,9],
             [9,3,9,9,2],
             [9,9,9,9,9],
             [9,9,9,1,0]]
print(calcPath(input_map, 0, 0))

input_map = [[1,1,1],
             [1,1,2],
             [1,2,0]]
print(calcPath(input_map, 0, 0))
'''

'''
실행결과

2
0
'''

#Code
def calcPath(inserted_map, x, y):
    #Base case
    if inserted_map[y][x] == inserted_map[len(inserted_map)-1][len(inserted_map[0])-1]:
        return 1
    #Recursive case
    else:
        try:
            new_map = []
            for i in inserted_map:
                new_map.append(i[inserted_map[y][x]:])
            a = calcPath(new_map, 0, 0)
        except IndexError:
            a = 0
        try:
            b = calcPath(inserted_map[inserted_map[y][x]:], 0, 0)
        except IndexError:
            b = 0
        return a+b

if __name__ == '__main__':
    input_map = [[1,2,9,4,9],
                 [9,9,9,9,9],
                 [9,3,9,9,2],
                 [9,9,9,9,9],
                 [9,9,9,1,0]]
    print(calcPath(input_map, 0, 0))

    input_map = [[1,1,1],
                 [1,1,2],
                 [1,2,0]]
    print(calcPath(input_map, 0, 0))
