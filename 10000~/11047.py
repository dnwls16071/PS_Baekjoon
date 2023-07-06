# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
#
# import sys
#
# N, K = map(int, sys.stdin.readline().strip().split())
# coin = []
# for _ in range(N):
#     coin.append(int(input()))
#
# coin.sort(reverse=True)
# cnt = 0
# money = 0
# while True:
#     if K == 0:
#         break
#     if coin[money] <= K:
#         K -= coin[money]
#         money = 0
#         cnt += 1
#     else:
#         money += 1
# print(cnt)


import sys

N, K = map(int, sys.stdin.readline().strip().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)
cnt = 0
while True:
    if K == 0:
        break
    else:
        for money in coin:
            if money <= K:
                cnt += (K // money)
                K -= (K // money) * money
print(cnt)