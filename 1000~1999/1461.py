# 세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
book = list(map(int, input().strip().split()))

plus_book = []
minus_book = []
temp = 0
for i in book:
    if i >= 0:
        plus_book.append(i)
    else:
        minus_book.append(i)

    if abs(i) > temp:
        temp = abs(i)

plus_book.sort(reverse=True)
minus_book.sort()
distance = 0
for i in range(0, len(plus_book), M):
    if plus_book[i] != temp:
        distance += plus_book[i] * 2

for i in range(0, len(minus_book), M):
    if abs(minus_book[i]) != temp:
        distance += abs(minus_book[i]) * 2

distance += temp
print(distance)