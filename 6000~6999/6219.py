# 농부 존은 소들에게 소수로 차례차례 번호를 매기는 중이다. 베시는 이 번호에서 숫자 D가 몇 번이나 등장하는지 궁금해졌다.
#
# 베시를 도와 범위 A..B(A와 B 포함)내에서 숫자 D를 포함하는 소수의 개수를 구해보자.
#
# 소수는 두개의 자연수(1과 자기자신)로만 나누어 떨어지는 자연수를 말한다. 소수의 예로는 2,3,5,7,11,13,17,19,23,29.. 가 있다.

import sys
input = sys.stdin.readline

A, B, D = map(int, input().strip().split())

prime_number = [True] * (B+1)
prime_number[0] = False
prime_number[1] = False
for i in range(2, B+1):
    if prime_number[i]:
        for j in range(i*i, B+1, i):
            prime_number[j] = False

cnt = 0
for i in range(A, B+1):
    # 선결조건 : 소수를 만족시켜야함
    if prime_number[i]:
        # 숫자 D가 해당 소수에 몇 개가 포함되어있느냐?
        if str(D) in str(i):
            cnt += 1
print(cnt)