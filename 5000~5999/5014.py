# 강호는 코딩 교육을 하는 스타트업 스타트링크에 지원했다. 오늘은 강호의 면접날이다. 하지만, 늦잠을 잔 강호는 스타트링크가 있는 건물에 늦게 도착하고 말았다.
#
# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다. 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
#
# 보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 강호가 탄 엘리베이터는 버튼이 2개밖에 없다. U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다. (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)
#
# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오. 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.

from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().strip().split())
visited = [0] * 1000001
flag = False

def BFS():
    global flag
    queue = deque()
    queue.append(S)
    visited[S] = 1
    while queue:
        v = queue.popleft()
        if v == G:
            flag = True
            break

        up = v + U
        down = v - D
        for i in [up, down]:
            if 0 < i <= F and visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)
    if flag:
        print(visited[G] - 1)
    else:
        print("use the stairs")

BFS()