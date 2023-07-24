# 정수 s가 주어진다. 정수 s의 값을 t로 바꾸는 최소 연산 횟수를 구하는 프로그램을 작성하시오.
#
# 사용할 수 있는 연산은 아래와 같다.
#
# s = s + s; (출력: +)
# s = s - s; (출력: -)
# s = s * s; (출력: *)
# s = s / s; (출력: /) (s가 0이 아닐때만 사용 가능)

from collections import deque
import sys
input = sys.stdin.readline

def BFS(start, result):
    queue = deque()
    if s == t:
        return 0
    queue.append((start, ""))
    visited.add(start)
    while queue:
        v, op = queue.popleft()
        if v == t:
            return op

        if v * v <= 1e9 and v * v not in visited:
            visited.add(v * v)
            queue.append((v * v, op + "*"))

        if v + v <= 1e9 and v + v not in visited:
            visited.add(v + v)
            queue.append((v + v, op + "+"))

        if 0 not in visited:
            visited.add(0)
            queue.append((v - v, op + "-"))

        if s != 0 and s >= 1 and 1 not in visited:
            visited.add(1)
            queue.append((v // v, op + "/"))
    return -1


s, t = map(int, input().strip().split())
visited = set()
print(BFS(s, ""))