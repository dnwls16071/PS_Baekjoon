# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

while True:
    try:
        n = int(input())

        num = 0
        while True:
            num = num * 10 + 1
            if num % n == 0:
                print(len(str(num)))
                break
        num = 0
    except EOFError:
        break