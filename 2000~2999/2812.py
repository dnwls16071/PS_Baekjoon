# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
li = input().strip()
stack = []
t = K

for i in range(N):
    while stack and t > 0 and stack[-1] < int(li[i]):
        stack.pop()
        t -= 1
    stack.append(int(li[i]))

print(''.join(map(str, stack[:N-K])))


