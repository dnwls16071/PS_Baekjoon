# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
#
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys

M = int(input())
data_set = set()
for _ in range(M):
    input_command = list(map(str, sys.stdin.readline().strip().split()))
    if len(input_command) == 2:
        command, data = input_command[0], int(input_command[1])
        if command == "add":
            if data in data_set:
                continue
            else:
                data_set.add(data)
        elif command == "remove":
            if data in data_set:
                data_set.remove(data)
            else:
                continue
        elif command == "check":
            if data in data_set:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if data in data_set:
                data_set.remove(data)
            else:
                data_set.add(data)
    else:
        command = input_command[0]
        if command == "all":
            data_set = set([i for i in range(1, 21)])
        elif command == "empty":
            data_set.clear()