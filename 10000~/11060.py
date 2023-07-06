# 재환이가 1×N 크기의 미로에 갇혀있다. 미로는 1×1 크기의 칸으로 이루어져 있고, 각 칸에는 정수가 하나 쓰여 있다. i번째 칸에 쓰여 있는 수를 Ai라고 했을 때, 재환이는 Ai이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프할 수 있다. 예를 들어, 3번째 칸에 쓰여 있는 수가 3이면, 재환이는 4, 5, 6번 칸 중 하나로 점프할 수 있다.
#
# 재환이는 지금 미로의 가장 왼쪽 끝에 있고, 가장 오른쪽 끝으로 가려고 한다. 이때, 최소 몇 번 점프를 해야 갈 수 있는지 구하는 프로그램을 작성하시오. 만약, 가장 오른쪽 끝으로 갈 수 없는 경우에는 -1을 출력한다.

#1
# import sys
# input = sys.stdin.readline
#
# N = int(input().strip())
# dp = [N+1] * (N+1)
# dp[0] = 0
# li = list(map(int, input().strip().split()))
#
# if N == 1:
#     print(0)
#     sys.exit()
#
# for i in range(N):
#     for j in range(1, 1+li[i]):
#         if i + j < N:
#             dp[i+j] = min(dp[i]+1, dp[i+j])
#
# if dp[N-1] != N+1:
#     print(dp[N-1])
# else:
#     print(-1)

#2
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
visited = [0] * N
li = list(map(int, input().strip().split()))

if N == 1:
    print(0)
    sys.exit()

def BFS():
    queue = deque()
    queue.append((0, li[0]))
    while queue:
        start, jump_cnt = queue.popleft()
        for i in range(1, jump_cnt + 1):
            if start + i >= N or visited[start + i]:
                continue
            visited[start + i] = visited[start] + 1
            queue.append((start + i, li[start + i]))

BFS()
if visited[-1] == 0:
    print(-1)
else:
    print(visited[-1])