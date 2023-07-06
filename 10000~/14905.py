# 모든 자연수를 4개의 소수의 합으로 나타낼 수 있을까? 이 물음에 대한 답은 '8 이상의 모든 자연수에 대해 그렇다'이지만, 데이빗은 그 사실을 알지 못했다. 데이빗은 프로그램을 돌려 4개의 소수의 합으로 표현할 수 없는 수를 찾아내 보기로 했다. 소수는 "두 개의 다른 자연수로만 나눠 떨어지는 자연수"이다. 예를 들어, 37은 37과 1로만 나눠 떨어지므로 소수이다.

import sys
input = sys.stdin.readline

def func(x):
    if x < 8:
        return "Impossible."
    else:
        prime = []
        sieve = [True] * (x+1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, x+1):
            if sieve[i]:
                prime.append(i)
                for j in range(i*i, x+1, i):
                    sieve[j] = False

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
                        if a + b + c + d > x:
                            break
                        if a + b + c + d == x:
                            ans = f"{a} {b} {c} {d}"
                            flag = True
                            break
        return ans

while True:
    N = input().strip()
    if N == "":
        sys.exit(0)
    else:
        print(func(int(N)))
