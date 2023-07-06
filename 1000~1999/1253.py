# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
#
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
#
# 수의 위치가 다르면 값이 같아도 다른 수이다.

import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
# 이분탐색을 수행하기 위해서는 배열이 오름차순으로 정렬된 상태여야함
A.sort()

ans = 0
def binary_search(target, data):
    global ans
    start = 0
    end = len(data) - 1
    while True:
        if start >= end:
            break

        res = data[start] + data[end]
        if res == target:
            ans += 1
            break
        elif res > target:
            end -= 1
        else:
            start += 1


for i in range(N):
    binary_search(A[i], A[:i] + A[i + 1:])
print(ans)
