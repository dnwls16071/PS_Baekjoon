# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

#1
import sys
input = sys.stdin.readline

def add(li):
    return li[0] + li[1]

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    arr = [True] * (int(1e6) + 1)
    arr[0] = False
    arr[1] = False
    for i in range(2, N+1):
        if arr:
            for j in range(i*i, N+1, i):
                arr[j] = False
    li = []
    for i in range(len(arr)):
        if arr[i]:
            li.append(i)

    half = N // 2
    cnt = 0
    for i in range(half):
        first = half - i
        second = half + i
        if first in li and second in li:
            cnt += 1
    print(cnt)


#2
import sys
input = sys.stdin.readline

T = int(input().strip())
num = []
max_num = -1
for _ in range(T):
    N = int(input().strip())
    num.append(N)

max_num = max(num)
arr = [True] * (max_num+1)
arr[0] = False
arr[1] = False
for i in range(2, max_num+1):
    if arr[i]:
        for j in range(i*i, max_num+1, i):
            arr[j] = False

for i in num:
    cnt = 0
    for j in range((i//2) + 1):
        if arr[j] and arr[i-j]:
            cnt += 1
    print(cnt)
