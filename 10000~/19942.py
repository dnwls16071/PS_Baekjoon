# 식재료 N개 중에서 몇 개를 선택해서 이들의 영양분(단백질, 탄수화물, 지방, 비타민)이 일정 이상이 되어야 한다. 아래 표에 제시된 6가지의 식재료 중에서 몇 개를 선택해서 이들의 영양분의 각각 합이 최소 100, 70, 90, 10가 되도록 하는 경우를 생각해보자. 이 경우 모든 재료를 선택하면 쉽게 해결되지만, 우리는 조건을 만족시키면서도 비용이 최소가 되는 선택을 하려고 한다.
#
# 재료	단백질	지방	탄수화물	비타민	가격
# 1	30	55	10	8	100
# 2	60	10	10	2	70
# 3	10	80	50	0	50
# 4	40	30	30	8	60
# 5	60	10	70	2	120
# 6	20	70	50	4	40
# 예를 들어, 식재료 1, 3, 5를 선택하면 영양분은 100, 145, 130, 10으로 조건을 만족하지만 가격은 270이 된다. 대신 2, 3, 4를 선택하면 영양분의 합은 110, 130, 90, 10, 비용은 180이 되므로, 앞의 방법보다는 더 나은 선택이 된다.
#
# 입력으로 식재료 표가 주어졌을 때, 최저 영양소 기준을 만족하는 최소 비용의 식재료 집합을 찾아야 한다.

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
mp, mf, ms, mv = map(int, input().strip().split())
nutrients = [[]]
for _ in range(N):
    p, f, s, v, c = map(int, input().strip().split())
    nutrients.append((p, f, s, v, c))

min_price = 9999999999      # 최소 비용
for i in range(1, N+1):
    for comb in combinations(range(1, N+1), i):
        tp, tf, ts, tv, tc = 0, 0, 0, 0, 0
        for j in comb:
            tp += nutrients[j][0]
            tf += nutrients[j][1]
            ts += nutrients[j][2]
            tv += nutrients[j][3]
            tc += nutrients[j][4]
        if tp >= mp and tf >= mf and ts >= ms and tv >= mv:
            if min_price > tc:
                min_price = tc
                answer = comb
            elif min_price == tc:
                answer = sorted((answer, comb))[0]

if min_price == 9999999999:
    print(-1)
else:
    print(min_price)
    print(*answer)
