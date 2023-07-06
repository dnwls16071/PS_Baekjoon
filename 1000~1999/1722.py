# 1부터 N까지의 수를 임의로 배열한 순열은 총 N! = N×(N-1)×…×2×1 가지가 있다.
#
# 임의의 순열은 정렬을 할 수 있다. 예를 들어  N=3인 경우 {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}의 순서로 생각할 수 있다. 첫 번째 수가 작은 것이 순서상에서 앞서며, 첫 번째 수가 같으면 두 번째 수가 작은 것이, 두 번째 수도 같으면 세 번째 수가 작은 것이….
#
# N이 주어지면, 아래의 두 소문제 중에 하나를 풀어야 한다. k가 주어지면 k번째 순열을 구하고, 임의의 순열이 주어지면 이 순열이 몇 번째 순열인지를 출력하는 프로그램을 작성하시오.

# import sys
# input = sys.stdin.readline
#
# N = int(input().strip())
# homework = []
# for i in range(N):
#     a, b = map(int, input().strip().split())
#     homework.append([a, b])
# homework.sort(key = lambda x : x[1], reverse=True)
#
# time = homework[0][1]
# for i in range(N):
#     s = homework[i][0]
#     d = homework[i][1]
#
#     if time >= d:
#         time = d - s
#     else:
#         time = time - s
# print(time)

import sys
input = sys.stdin.readline

