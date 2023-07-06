# 세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때, 이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값을 구하고 싶다.

import sys

N = int(input())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline().strip()))

li.sort()
max_val = 0
for i in range(N-2):
    if li[i] + li[i+1] > li[i+2]:
        if max_val < li[i] + li[i+1] + li[i+2]:
            max_val = li[i] + li[i+1] + li[i+2]
    else:
        if max_val > 0:
            continue
        else:
            max_val = -1
print(max_val)