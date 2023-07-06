# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
#
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

#1
# from itertools import combinations
#
# N, M = map(int, input().split())
# li = list(map(int, input().split()))
#
# li.sort()
# for i in combinations(li, M):
#     print(*i)

#2
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
li = list(map(int, input().strip().split()))
li.sort()
res = []

def recursive(start):
    if len(res) == M:
        print(" ".join(map(str, res)))
        return 0
    else:
        for i in range(start, len(li)):
            res.append(li[i])
            recursive(i+1)
            res.pop()
recursive(0)