# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.
#
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
papers = []
for _ in range(N):
    papers.append(list(map(int, input().strip().split())))

def recursive(x, y, N):
    global result
    paper = papers[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if papers[i][j] != paper:
                for k in range(3):
                    for t in range(3):
                        recursive(x + k * N//3, y + t * N//3, N//3)
                return
    if paper == 0:
        result[0] += 1
    elif paper == 1:
        result[1] += 1
    else:
        result[-1] += 1

result = [0, 0, 0]
recursive(0, 0, N)
print(result[-1], result[0], result[1])