# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
memoization = [0]

for i in A:
    if memoization[-1] < i:
        memoization.append(i)
    else:
        left = 0
        right = len(memoization)
        while True:
            if left >= right:
                break
            mid = (left + right) // 2
            if memoization[mid] < i:
                left = mid + 1
            else:
                right = mid
        memoization[right] = i
print(len(memoization)-1)