# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

from itertools import permutations

N = int(input())
arr = [i for i in range(1, N+1)]

for i in permutations(arr, N):
    print(*i)