# 양의 정수 N이 주어졌을 때, 이 수를 소인수분해 한 결과를 출력하는 프로그램을 작성하시오.

T = int(input())
for _ in range(T):
    N = int(input())
    j = 2
    dict = {}

    while True:
        if N == 1:
            break

        if N % j == 0:
            N //= j
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
        else:
            j += 1

    for i in dict.items():
        if i[1] != 0:
            print(i[0], i[1])