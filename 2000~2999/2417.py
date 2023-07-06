# 정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램을 작성하시오.

n = int(input())

start = 0
end = n
while True:
    mid = (start + end) // 2
    if start > end:
        print(start)
        break
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1


