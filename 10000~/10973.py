# 1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 바로 이전에 오는 순열을 구하는 프로그램을 작성하시오.
#
# 사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.
#
# N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.
#
# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1

import sys

N = int(input())
li = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if li[i-1] > li[i]:
        for j in range(N-1, 0, -1):
            if li[i-1] > li[j]:
                li[i-1], li[j] = li[j], li[i-1]
                li = li[:i] + sorted(li[i:], reverse=True)
                for i in li:
                    print(i, end = " ")
                sys.exit()
print(-1)