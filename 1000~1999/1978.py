# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

N = int(input())
number = list(map(int, input().split()))

prime_number = 0
for i in number:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        prime_number += 1
print(prime_number)
