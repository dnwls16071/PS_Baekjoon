# 지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다. 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.
#
# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input().strip())
weight_limit = list(map(int, input().strip().split()))
M = int(input().strip())
box = list(map(int, input().strip().split()))

weight_limit.sort(reverse=True)
box.sort(reverse=True)

time = 0
if max(box) > max(weight_limit):
    print(-1)
    sys.exit(0)
while True:
    if len(box) == 0:
        break
    time += 1
    for i in weight_limit:
        for j in range(len(box)):
            if i >= box[j]:
                box.remove(box[j])
                break
print(time)
