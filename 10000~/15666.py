# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

#1
# from itertools import combinations_with_replacement
#
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().strip().split())
# A = list(map(int, input().strip().split()))
# A.sort()
# A = list(combinations_with_replacement(A, M))
# A = sorted(list(set(A)))
#
# for i in A:
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
        flag = 0
        for i in range(start, len(li)):
            if flag != li[i]:
                res.append(li[i])
                flag = li[i]
                recursive(i)
                res.pop()
recursive(0)