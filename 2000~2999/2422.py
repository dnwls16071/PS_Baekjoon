# 한윤정과 친구들은 이탈리아로 방학 여행을 갔다. 이탈리아는 덥다. 윤정이와 친구들은 아이스크림을 사먹기로 했다. 아이스크림 가게에는 N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다. 어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다. 따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다. 이때, 선택하는 방법이 몇 가지인지 구하려고 한다.

import sys

N, M = map(int, input().split())
ice_cream = [[True] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    ice_cream[a][b] = False
    ice_cream[b][a] = False

method = 0
for a in range(1, N-1):
    for b in range(a+1, N):
        for c in range(b+1, N+1):
            if ice_cream[a][b] == False or ice_cream[a][c] == False or ice_cream[b][c] == False:
                continue
            else:
                method += 1
print(method)