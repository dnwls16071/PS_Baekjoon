# 폴란드 왕자 구사과는 다음과 같은 수를 좋아한다.
#
# 0과 1로만 이루어져 있어야 한다.
# 1이 적어도 하나 있어야 한다.
# 수의 길이가 100 이하이다.
# 수가 0으로 시작하지 않는다.
# 예를 들어, 101은 구사과가 좋아하는 수이다.
#
# 자연수 N이 주어졌을 때, N의 배수 중에서 구사과가 좋아하는 수를 구하는 프로그램을 작성하시오.

from collections import deque
import sys
input = sys.stdin.readline

def BFS(N):
    queue = deque([(1, "1")])
    visited = [False] * 20001
    visited[1] = True

    while queue:
        current_num, current_str = queue.popleft()
        # 만약 만들어진 현재 숫자가 N의 배수라면?
        if current_num % N == 0:
            return current_str
        # 만약 구사과가 좋아하는 수의 길이가 100을 넘어선다면?
        if len(current_str) > 100:
            return "BRAK"
        # 1을 뒤에 붙이는 경우
        if not visited[((current_num * 10) + 1) % N]:
            visited[((current_num * 10) + 1) % N] = True
            queue.append([(((current_num * 10) + 1) % N), current_str + "1"])
        # 0을 뒤에 붙이는 경우
        if not visited[(current_num * 10) % N]:
            visited[(current_num * 10) % N] = True
            queue.append([((current_num * 10) % N), current_str + "0"])
    return "BRAK"

T = int(input())
for i in range(T):
    N = int(input().strip())
    print(BFS(N))