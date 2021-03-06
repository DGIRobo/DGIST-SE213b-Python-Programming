#미로 탈출

'''
Description

미로를 탈출하는 함수 play()를 작성하오.
프로그래밍 교과의 첫번째 시간에 마리오가 미로를 탈출하는 예제에 대해서 각각 생각해본 바가 있다. 마지막 과제에서는 미로탈출을 생각했던 방식을 소스코드로 구현해본다.
아래 코드에서는 2개의 클래스가 정의되어 있다.
'''

'''
1. class Player

Player 클래스는 움직이는 캐릭터의 위치 정보를 담고 있는 자료형이다.
player는 지도상의 (x, y) 좌표로 자신의 위치를 기억하고 있고, 사용자가 move(방향) 인스턴스 메소드를 통해서 좌표를 좌/우/위/아래 중 한 방향으로 1칸 전진시킬수 있다.
get_position() 메소드를 통해서 현재 플레이어의 좌표를 튜플로 반환받는다.
'''

'''
2. class MazeGame
초기화 함수__init__(map)에서 map이라는 파라메터로 미로 지도를 받는다.
미로지도는 2차 리스트로 되어있고 길(0) 또는 벽(1)으로 구성되어 있다.
인스턴스 변수 map에 해당맵을 저장하고 인스턴스 변수 path에 탈출 경로를 저장할 빈리스트를 만들어준다.
현재 위치를 (0, 0)으로 새로운 player를 하나 생성하고 인스턴스 변수로 저장한다.
get_map() 인스턴스 지도 변수 map을 반환한다.
get_path() 탈출 경로를 생성후 만든 인스턴스 변수 path를 반환한다.
play() 메소드를 호출하면, self.player의 현재 위치를 리스트 self.pth에 넣어주고 탈출할수 있는 방법을 작성하여 palyer의 move함수를 통해서 이동하면서 추가되면 경로를 self.path에 넣고 최종적으로 (len(map)-1,len(map)-1)에 도달하는 경로가 생성되면 종료한다.
'''

'''
함수 사용예시

map=[ [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
      [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
      [ 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1 ],
      [ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
      [ 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1 ],
      [ 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1 ],
      [ 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1 ],
      [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
      [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
      [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1 ],
      [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1 ],
      [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
      [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
      [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ] ]

game1 = MazeGame(map)
game1.play()
print(game1.get_map())
print(game1.get_path())
'''

'''
실행결과 (좌표 (0,0)에서 좌표(map-1, map-1)까지 경로 - 코드에 따라 달라질수 있음.)

[[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
[(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 4), (12, 3), (12, 2), (12, 1), (11, 1), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (11, 7), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (13, 12), (13, 13)]
'''

'''
혹시, memory 관련 에러가 나는 경우는 어딘가 경로 생성이 무한하게 반복되어서 종료되지 못할수 있습니다.

코드에서 경로 생성 갯수를 제한하여 결과를 크롬에서 show 버튼으로 확인해보시면 이상을 발견하기 쉽습니다.

    def play(self):
        self.path.append(self.player.get_position())
        ...
        ...
        max_cnt=200
        while :
            if max_cnt == 0 : break
            else: max_cnt -= 1

            # 경로 append 코드 작성
'''

#Code
map=[[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
          [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1 ],
          [ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1 ],
          [ 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1 ],
          [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
          [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ] ]

m1=[ [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
          [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1 ],
          [ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1 ],
          [ 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1 ],
          [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
          [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ] ]

m2= [[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
          [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1 ],
          [ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1 ],
          [ 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1 ],
          [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
          [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],
          [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ] ]

m3=[ [ 0, 1, 1, 1, 1, 1],
          [ 0, 0, 0, 0, 0, 1 ],
          [ 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 0, 0, 0, 1 ],
          [ 1, 1, 1, 1, 0, 0 ],]

m4=[ [ 0, 1, 1, 1, 1, 1],
          [ 0, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 1, 1, 1 ],
          [ 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 1, 0, 1 ],
          [ 1, 1, 1, 1, 0, 0 ],]


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dir):
        if dir =='up':
            self.y += 1
        elif dir =='down':
            self.y -= 1
        elif dir =='left':
            self.x -= 1
        elif dir =='right':
            self.x += 1

    def get_position(self):
        return (self.x, self.y)


class MazeGame:
    def __init__(self, map=None):
        self.map = map
        self.player = Player()
        self.path = []

    def play(self):
        m = len(self.map)
        n = len(self.map[0])

        self.path.append(self.player.get_position())
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        right = [(0, 1), (0, -1), (-1 ,0), (1, 0)]

        def turn_right(d):
            if d[0] == 0:
                return (-d[1], 0)
            else:
                return (0, d[0])

        def turn_left(d):
            nd = turn_right(d)
            return (-nd[0], -nd[1])

        #Find initial direction
        for d in direction:
            nx, ny = d
            if 0<=nx<n and 0<=ny<m:
                if self.map[ny][nx] == 0:
                    curr_dir = d
                    break

        for x, y in self.path:
            if x == m-1 and y == n-1:
                break

            d = turn_right(curr_dir)

            while(True):
                nx = x + d[0]
                ny = y + d[1]
                if 0<=nx<n and 0<=ny<m:
                    if self.map[ny][nx] == 0:
                        self.path.append((nx, ny))
                        curr_dir = d
                        break
                    elif self.map[ny][nx] == 1:
                        d = turn_left(d)
                else:
                    d = turn_left(d)

    def get_map(self):
        return self.map

    def get_path(self):
        return self.path


if __name__ == "__main__" :
    game1 = MazeGame(map)
    game1.play()
    print(game1.get_map())
    print(game1.get_path())
