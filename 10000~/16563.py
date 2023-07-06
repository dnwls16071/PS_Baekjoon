# 지원이는 대회에 출제할 문제에 대해서 고민하다가 소인수분해 문제를 출제해야겠다고 마음을 먹었다. 그러나 그 이야기를 들은 동생의 반응은 지원이의 기분을 상하게 했다.
#
# "소인수분해? 그거 너무 쉬운 거 아니야?"
#
# 지원이는 소인수분해의 어려움을 알려주고자 엄청난 자신감을 가진 동생에게 2와 500만 사이의 자연수 N개를 주고 소인수분해를 시켰다. 그러자 지원이의 동생은 기겁하며 쓰러졌다. 힘들어하는 지원이의 동생을 대신해서 여러분이 이것도 쉽다는 것을 보여주자!

#1
import sys
input = sys.stdin.readline

N = int(input())
k = list(map(int, input().strip().split()))

def solve(x):
    t = 2
    while True:
        if x == 1:
            break
        if x % t == 0:
            x //= t
            ans.append(t)
        else:
            t += 1
    return ans

for i in k:
    ans = []
    res = solve(i)
    print(" ".join(map(str, res)))

#2
import sys
input = sys.stdin.readline

N = int(input())
k = list(map(int, input().strip().split()))

Max = -1
for i in k:
    if Max < i:
        Max = i

arr = [True] * (Max + 1)
prime_number = []
arr[0] = False
arr[1] = False
for i in range(2, int(Max ** 0.5) + 1):
    if arr[i]:
        prime_number.append(i)
        for j in range(i * i, Max + 1, i):
            arr[j] = False


def solve(x):
    while True:
        if x == 1:
            break
        for i in prime_number:
            if x % i == 0:
                x //= i
                ans.append(i)
                break
    return ans


for i in k:
    ans = []
    res = solve(i)
    print(" ".join(map(str, res)))

#3
import sys
input = sys.stdin.readline

def SieveofEratosthenes(x):
    arr = [i for i in range(x+1)]
    i = 2
    while i * i <= x:
        if arr[i] == i:
            for j in range(i*i, x, i):
                if arr[j] == j:
                    arr[j] = i
        i += 1
    return arr

N = int(input())
temp = SieveofEratosthenes(5000001)
K = list(map(int, input().strip().split()))
for k in K:
    result = []
    while True:
        if k == 1:
            break
        result.append(temp[k])
        k //= temp[k]
    print(" ".join(map(str, result)))