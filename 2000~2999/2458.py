# 1번부터 N번까지 번호가 붙여져 있는 학생들에 대하여 두 학생끼리 키를 비교한 결과의 일부가 주어져 있다. 단, N명의 학생들의 키는 모두 다르다고 가정한다. 예를 들어, 6명의 학생들에 대하여 6번만 키를 비교하였고, 그 결과가 다음과 같다고 하자.
#
# 1번 학생의 키 < 5번 학생의 키
# 3번 학생의 키 < 4번 학생의 키
# 5번 학생의 키 < 4번 학생의 키
# 4번 학생의 키 < 2번 학생의 키
# 4번 학생의 키 < 6번 학생의 키
# 5번 학생의 키 < 2번 학생의 키
# 이 비교 결과로부터 모든 학생 중에서 키가 가장 작은 학생부터 자신이 몇 번째인지 알 수 있는 학생들도 있고 그렇지 못한 학생들도 있다는 사실을 아래처럼 그림을 그려 쉽게 확인할 수 있다. a번 학생의 키가 b번 학생의 키보다 작다면, a에서 b로 화살표를 그려서 표현하였다.
#
#
#
# 1번은 5번보다 키가 작고, 5번은 4번보다 작기 때문에, 1번은 4번보다 작게 된다. 그러면 1번, 3번, 5번은 모두 4번보다 작게 된다. 또한 4번은 2번과 6번보다 작기 때문에, 4번 학생은 자기보다 작은 학생이 3명이 있고, 자기보다 큰 학생이 2명이 있게 되어 자신의 키가 몇 번째인지 정확히 알 수 있다. 그러나 4번을 제외한 학생들은 자신의 키가 몇 번째인지 알 수 없다.
#
# 학생들의 키를 비교한 결과가 주어질 때, 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명인지 계산하여 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().strip().split())
    # a가 b보다 키가 작다.
    graph[a][b] = True

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][k] == True and graph[k][b] == True:
                graph[a][b] = True

answer = 0
for a in range(1, N+1):
    chk = 0
    for b in range(1, N+1):
        chk += graph[a][b] + graph[b][a]
    if chk == N-1:
        answer += 1
print(answer)