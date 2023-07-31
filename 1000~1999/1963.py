# 소수를 유난히도 좋아하는 창영이는 게임 아이디 비밀번호를 4자리 ‘소수’로 정해놓았다. 어느 날 창영이는 친한 친구와 대화를 나누었는데:
#
# “이제 슬슬 비번 바꿀 때도 됐잖아”
# “응 지금은 1033으로 해놨는데... 다음 소수를 무엇으로 할지 고민중이야"
# “그럼 8179로 해”
# “흠... 생각 좀 해볼게. 이 게임은 좀 이상해서 비밀번호를 한 번에 한 자리 밖에 못 바꾼단 말이야. 예를 들어 내가 첫 자리만 바꾸면 8033이 되니까 소수가 아니잖아. 여러 단계를 거쳐야 만들 수 있을 것 같은데... 예를 들면... 1033 1733 3733 3739 3779 8779 8179처럼 말이야.”
# “흠...역시 소수에 미쳤군. 그럼 아예 프로그램을 짜지 그래. 네 자리 소수 두 개를 입력받아서 바꾸는데 몇 단계나 필요한지 계산하게 말야.”
# “귀찮아”
# 그렇다. 그래서 여러분이 이 문제를 풀게 되었다. 입력은 항상 네 자리 소수만(1000 이상) 주어진다고 가정하자. 주어진 두 소수 A에서 B로 바꾸는 과정에서도 항상 네 자리 소수임을 유지해야 하고, ‘네 자리 수’라 하였기 때문에 0039 와 같은 1000 미만의 비밀번호는 허용되지 않는다.

from collections import deque
import sys
input = sys.stdin.readline

# BFS 완전 탐색
def BFS(A, B):
    global arr
    queue = deque()
    queue.append(A)
    visited[A] = True
    while queue:
        a = queue.popleft()
        if a == B:
            print(arr[a])
            return
        a = str(a)
        for i in range(4):
            for j in range(10):
                val = int(a[:i] + str(j) + a[i+1:])
                # 4자리 수이면서 소수여야 한다.(방문하지 않은 숫자의 경우만 탐색)
                if 1000 <= val <= 9999 and not visited[val] and arr[val] == 0:
                    arr[val] = arr[int(a)] + 1
                    visited[val] = True
                    queue.append(val)

T = int(input())
for _ in range(T):
    visited = [False] * 10001
    arr = [0] * 10001
    for i in range(2, 101):
        for j in range(2*i, 10001, i):
            arr[j] = 1
    A, B = map(int, input().strip().split())
    BFS(A, B)







