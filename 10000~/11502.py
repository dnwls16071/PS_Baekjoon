# 정수론(수학)에서, 세 개의 소수 문제(3-primes problem) 는 다음과 같은 추측을 말한다.
#
# '5보다 큰 임의의 홀수는 정확히 세 개의 소수들의 합으로 나타낼 수 있다. 물론 하나의 소수를 여러 번 더할 수도 있다.'
#
# 예를 들면,
#
# 7 = 2 + 2 + 3
# 11 = 2 + 2 + 7
# 25 = 7 + 7 + 11
# 5보다 큰 임의의 홀수를 입력받아서, 그 홀수가 어떻게 세 소수의 합으로 표현될 수 있는지 (또는 불가능한지) 알아보는 프로그램을 작성하시오.

prime_number = [True] * 1000
prime_number[0] = False
prime_number[1] = False
li = []
for i in range(2, 1000):
    if prime_number[i]:
        li.append(i)
        for j in range(2*i, 1000, i):
            prime_number[j] = False

def prime_number_sum(x):
    result = []
    for a in range(len(li)):
        for b in range(len(li)):
            for c in range(len(li)):
                if li[a] + li[b] + li[c] == x:
                    result.append([li[a], li[b], li[c]])
    result = sorted(result, key = lambda x : (x[0], x[1], x[2]))
    if len(result) == 0:
        print(0)
    else:
        print(*result[0])

T = int(input())
for _ in range(T):
    K = int(input())
    prime_number_sum(K)