# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.

N, M = map(int, input().split())
square = []
for _ in range(N):
    square.append(list(input()))

result = []
for i in range(N):  # 세로
    for j in range(M):  # 가로
        for t in range(min(N, M)):
            if i + t < N and j + t < M and square[i][j] == square[i+t][j] == square[i][j+t] == square[i+t][j+t]:
                result.append((t+1)**2)
print(max(result))