# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        if start > end:
            return 0
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

N = int(input())
A_li = list(map(int, input().split()))
M = int(input())
B_li = list(map(int, input().split()))

A_li.sort()
for i in B_li:
    if binary_search(i, A_li) == 1:
        print(1)
    else:
        print(0)
