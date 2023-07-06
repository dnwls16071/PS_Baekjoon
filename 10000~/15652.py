# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

#1
# from itertools import combinations_with_replacement
#
# N, M = map(int, input().split())
# arr = [i for i in range(1, N+1)]
#
# for i in combinations_with_replacement(arr, M):
#     print(*i)

#2
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
li = []

def recursive(start):
    if len(li) == M:
        print(" ".join(map(str, li)))
        return 0
    else:
        for i in range(start, N+1):
            li.append(i)
            recursive(i)
            li.pop()
recursive(1)