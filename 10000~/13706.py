# 정수 N이 주어졌을 때, N의 제곱근을 구하는 프로그램을 작성하시오.

N = int(input())

start = 1
end = N
while True:
    mid = (start + end) // 2
    if N == 0:
        print(0)
        break
    if mid**2 == N:
        print(mid)
        break
    elif mid**2 > N:
        end = mid - 1
    else:
        start = mid + 1
