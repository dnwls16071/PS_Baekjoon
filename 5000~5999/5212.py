# 푸르고 아름다운 남해에는 많은 섬이 장관을 이루고 있다. 그림이 아니면 볼 수 없을 것 같은 아름다운 장관을 실제로 볼 수 있는 다도해로 상근이는 여행을 떠났다.
#
# 다도해에 도착한 상근이는 서울에서 보던 것과는 다른 풍경에 큰 충격을 받았다. 지구 온난화로 인해 해수면이 상승해 섬의 일부가 바다에 잠겨버렸다.
#
# 서울로 다시 돌아온 상근이는 이렇게 지구 온난화가 계속 될 경우 남해의 지도는 어떻게 바뀔지 궁금해졌다.
#
# 다도해의 지도는 R*C 크기의 그리드로 나타낼 수 있다. 'X'는 땅을 나타내고, '.'는 바다를 나타낸다.
#
# 50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다는 사실을 알았다.
#
# 상근이는 50년 후 지도를 그려보기로 했다. 섬의 개수가 오늘날보다 적어질 것이기 때문에, 지도의 크기도 작아져야 한다. 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다. 50년이 지난 후에도 섬은 적어도 한 개 있다. 또, 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.

import copy
import sys
input = sys.stdin.readline

R, C = map(int, input().strip().split())
Map = []
for i in range(R):
    Map.append(list(input().strip()))
new_Map = copy.deepcopy(Map)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for i in range(R):
    for j in range(C):
        sea_count = 0
        if Map[i][j] == ".":
            continue
        else:
            for t in range(4):
                nx = i + dx[t]
                ny = j + dy[t]
                if 0 <= nx < R and 0 <= ny < C:
                    if Map[nx][ny] == ".":
                        sea_count += 1
                else:
                    sea_count += 1
            if sea_count >= 3:
                new_Map[i][j] = "."

start = 0
end = 0
for i in range(R):
    if "X" in new_Map[i]:
        start = i
        break

for i in range(R-1, -1, -1):
    if "X" in new_Map[i]:
        end = i
        break

temp = []
for i in range(C):
    for j in range(start, end+1):
        if new_Map[j][i] == "X":
            temp.append(i)
            break

for i in range(start, end+1):
    print("".join(new_Map[i][temp[0]:temp[-1]+1]))
