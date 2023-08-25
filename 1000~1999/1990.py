# 151은 소수이면서 동시에 팰린드롬이기 때문에 소수인 팰린드롬이다. 팰린드롬이란 앞으로 읽어나 뒤로 읽으나 같은 수를 말한다. 예를 들어 1234는 앞으로 읽으면 1234지만, 뒤로 읽으면 4321이 되고 이 두 수가 다르기 때문에 팰린드롬이 아니다. 두 정수 a, b가 주어졌을 때, a이상 b이하인 소수인 팰린드롬을 모두 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

A, B = map(int, input().strip().split())
if B > 10000000:
    B = 10000000
arr = [True] * (B+1)
arr[0] = False
arr[1] = False
for i in range(2, B+1):
    if arr[i]:
        for j in range(i*i, B+1, i):
            arr[j] = False

for i in range(A, B+1):
    if arr[i] and palindrome(i):
        print(i)
print(-1)