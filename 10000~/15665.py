# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

#1
# from itertools import product
#
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().strip().split())
# A = list(map(int, input().strip().split()))
# A = set(product(A, repeat = M))
# A = sorted(A)
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

def recursive():
    if len(res) == M:
        print(" ".join(map(str, res)))
        return 0
    else:
        flag = 0
        for i in range(len(li)):
            if flag != li[i]:
                res.append(li[i])
                flag = li[i]
                recursive()
                res.pop()
recursive()