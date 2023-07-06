#     +---+
#     | D |
# +---+---+---+---+
# | E | A | B | F |
# +---+---+---+---+
#     | C |
#     +---+
# 주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.
#
# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.
#
# 지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
#
# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().strip().split()))

# 1면만 보이는 사각형의 개수
side_1 = 4 * (N-1) * (N-2) + (N-2)**2

# 2면만 보이는 사각형의 개수
side_2 = 4 * (N-1) + 4 * (N-2)

# 3면만 보이는 사각형의 개수
side_3 = 4

Sum = []
result = 0
if N == 1:
    number.sort()
    for i in range(5):
        result += number[i]
    print(result)
else:
    Sum.append(min(number[0], number[5]))
    Sum.append(min(number[1], number[4]))
    Sum.append(min(number[2], number[3]))
    Sum.sort()

    side_1_sum = Sum[0]
    side_2_sum = Sum[0] + Sum[1]
    side_3_sum = Sum[0] + Sum[1] + Sum[2]

    print(side_1_sum * side_1 + side_2_sum * side_2 + side_3_sum * side_3)
