# 어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.
#
# 두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력한다.

import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())

arr = [True] * (int(B**0.5)+1)
arr[0] = False
arr[1] = False
for i in range(2, int(B**0.5)+1):
    if arr[i]:
        if i * i > int(B**0.5):
            break
        for j in range(i*i, int(B**0.5)+1, i):
            arr[j] = False

cnt = 0
for i in range(len(arr)):
    if arr[i]:
        prime_number = i * i
        while True:
            if prime_number < A:
                prime_number *= i
                continue
            if prime_number > B:
                break
            prime_number *= i
            cnt += 1
print(cnt)