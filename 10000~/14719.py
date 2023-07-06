# 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
#
#
#
# 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

import sys
input = sys.stdin.readline

H, W = map(int, input().strip().split())
block_height = list(map(int, input().strip().split()))

ans = 0
for i in range(1, W - 1):
    left_Max = max(block_height[i:])
    right_Max = max(block_height[:i + 1])
    Min_height = min(left_Max, right_Max)

    if Min_height - block_height[i] <= 0:
        continue
    else:
        ans += (Min_height - block_height[i])
print(ans)