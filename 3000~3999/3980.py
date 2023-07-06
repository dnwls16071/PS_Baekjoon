# 챔피언스 리그 결승전을 앞두고 있는 맨체스터 유나이티드의 명장 퍼거슨 감독은 이번 경기에 4-4-2 다이아몬드 전술을 사용하려고 한다.
#
# 오늘 결승전에 뛸 선발 선수 11명은 미리 골라두었지만, 어떤 선수를 어느 포지션에 배치해야 할지 아직 결정하지 못했다.
#
# 수석코치 마이크 펠란은 11명의 선수가 각각의 포지션에서의 능력을 0부터 100까지의 정수로 수치화 했다. 0은 그 선수가 그 포지션에 적합하지 않다는 뜻이다.
#
# 이때, 모든 선수의 포지션을 정하는 프로그램을 작성하시오. 모든 포지션에 선수를 배치해야 하고, 각 선수는 능력치가 0인 포지션에 배치될 수 없다.

import sys
input = sys.stdin.readline

def recursive(idx, score):
    global Max_score
    if idx == 11:
        if score > Max_score:
            Max_score = score
        return Max_score

    for i in range(11):
        if visited[i] or not stats[i]:
            continue
        if stats[idx][i] > 0:
            visited[i] = True
            recursive(idx + 1, score + stats[idx][i])
            visited[i] = False

T = int(input())
for _ in range(T):
    stats = []
    Max_score = 0
    visited = [False] * 11
    player = [0] * 11
    for i in range(11):
        stats.append(list(map(int, input().split())))
    recursive(0, 0)
    print(Max_score)