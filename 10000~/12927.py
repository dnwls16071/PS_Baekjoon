# 강호는 전구 N개를 가지고 있다. 전구는 1번부터 N번까지 번호가 매겨져 있으며, 일렬로 놓여져 있다. 전구는 켜져있거나 꺼져있다.
#
# 강호는 모든 전구를 끄려고 한다. 강호는 전구를 켜고 끌 수 있는 스위치 N개를 가지고 있고, 스위치도 1번부터 N번까지 번호가 매겨져 있다. i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다.
#
# 현재 전구의 상태가 주어졌을 때, 모든 전구를 끄기 위해서 스위치를 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

light_bulb = [0] + list(input().strip())
N = len(light_bulb)
cnt = 0
for i in range(1, N):
    if light_bulb[i] == "Y":
        for j in range(i, N, i):
            if light_bulb[j] == "Y":
                light_bulb[j] = "N"
            else:
                light_bulb[j] = "Y"
        cnt += 1
    else:
        continue
print(cnt)