# M개의 우주가 있고, 각 우주에는 1부터 N까지 번호가 매겨진 행성이 N개 있다. 행성의 크기를 알고 있을때, 균등한 우주의 쌍이 몇 개인지 구해보려고 한다. 구성이 같은데 순서만 다른 우주의 쌍은 한 번만 센다.
#
# 두 우주 A와 B가 있고, 우주 A에 있는 행성의 크기는 A1, A2, ..., AN, 우주 B에 있는 행성의 크기는 B1, B2, ..., BN라고 하자. 두 우주의 행성 크기가 모든 1 ≤ i, j ≤ N에 대해서 아래와 같은 조건을 만족한다면, 두 우주를 균등하다고 한다.
#
# Ai < Aj → Bi < Bj
# Ai = Aj → Bi = Bj
# Ai > Aj → Bi > Bj

# 이중 반복문 or 좌표 압축
from collections import defaultdict
import sys
input = sys.stdin.readline

universe = defaultdict(int)
M, N = map(int, input().strip().split())
for _ in range(M):
    # 행성의 크기 입력값으로 받아옴
    planet = list(map(int, input().strip().split()))
    # 행성의 크기를 오름차순으로 정렬
    sorted_planet = sorted(planet)
    # 정렬된 행성의 크기를 순서대로 인덱싱
    sorted_ranks = {sorted_planet[i] : i for i in range(len(sorted_planet))}
    # 입력값 순서대로 다시 인덱싱을 해줘야 함
    ranks = tuple(sorted_ranks[i] for i in planet)
    universe[ranks] += 1

# 한 쌍 즉, 딕셔너리의 값이 2이상이면 nC2로 값을 가져오면 됨
result = 0
for val in universe.values():
    result += val * (val - 1) // 2
print(result)
