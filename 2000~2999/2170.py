# 매우 큰 도화지에 자를 대고 선을 그으려고 한다. 선을 그을 때에는 자의 한 점에서 다른 한 점까지 긋게 된다. 선을 그을 때에는 이미 선이 있는 위치에 겹쳐서 그릴 수도 있는데, 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별할 수 없다고 하자.
#
# 이와 같은 식으로 선을 그었을 때, 그려진 선(들)의 총 길이를 구하는 프로그램을 작성하시오. 선이 여러 번 그려진 곳은 한 번씩만 계산한다.

import sys
input = sys.stdin.readline

N = int(input())
result = 0
arr = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    arr.append([x, y])
arr.sort()
start = arr[0][0]
end = arr[0][1]

for i in range(1, N):
    # 겹치는 경우
    # 1 3
    # 2 5
    # 3 5 → start = 1, end = 5
    if arr[i][0] <= end <= arr[i][1]:
        end = max(end, arr[i][1])
    # 겹치지 않는 경우
    # 6 7
    elif arr[i][0] > end:
        result += end - start
        # start : 6, end : 7
        start = arr[i][0]
        end = arr[i][1]
result += end - start
print(result)