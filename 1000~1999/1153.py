# 임의의 자연수가 주어지면, 이를 네 개의 소수의 합으로 분해하는 프로그램을 작성하시오. 예를 들어 38 = 5 + 7 + 13 + 13이 된다.

import sys
input = sys.stdin.readline

def solve(x):
    prime = []
    arr = [True] * (N+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, N+1):
        if arr[i]:
            prime.append(i)
            for j in range(i*i, N+1, i):
                arr[j] = False

    flag = False
    for a in prime:
        if flag:
            break
        for b in prime:
            if flag:
                break
            for c in prime:
                if flag:
                    break
                for d in prime:
                    if a + b + c + d > N:
                        break
                    if a + b + c + d == N:
                        flag = True
                        ans = f"{a} {b} {c} {d}"
                        break
    if flag == False:
        return -1
    return ans

N = int(input())
print(solve(N))