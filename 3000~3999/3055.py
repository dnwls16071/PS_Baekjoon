# 사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다. 이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.
#
# 티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.
#
# 매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다. 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.
#
# 티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.
#
# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.

from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().strip().split())
area = [list(input().strip()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]

water = deque()
animal = deque()

def flood():
    for _ in range(len(water)):
        x, y = water.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if area[nx][ny] == ".":
                    area[nx][ny] = "*"
                    water.append((nx, ny))

def move():
    flag = False
    for _ in range(len(animal)):
        x, y = animal.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if area[nx][ny] == ".":
                    flag = True
                    visited[nx][ny] = visited[x][y] + 1
                    animal.append((nx, ny))
                elif area[nx][ny] == "D":
                    return visited[x][y] + 1
    if not flag:
        return "KAKTUS"

for i in range(R):
    for j in range(C):
        if area[i][j] == "S":
            animal.append((i, j))
        elif area[i][j] == "*":
            water.append((i, j))

while True:
    flood()
    res = move()
    if res:
       break
print(res)