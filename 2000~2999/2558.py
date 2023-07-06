# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
#
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# deque 자료구조의 특징 : 양쪽에서 데이터의 삽입과 삭제가 이루어진다.
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()
arr = deque(arr)
q = deque()
q.append(arr.pop())
ans = 0
for i in range(N-1):
    val1 = abs(arr[0] - q[0])
    val2 = abs(arr[0] - q[-1])
    val3 = abs(arr[-1] - q[-1])
    val4 = abs(arr[-1] - q[0])
    Max = max(val1, val2, val3, val4)
    if Max == val1:
        ans += val1
        q.appendleft(arr.popleft())
    elif Max == val2:
        ans += val2
        q.append(arr.popleft())
    elif Max == val3:
        ans += val3
        q.append(arr.pop())
    else:
        ans += val4
        q.appendleft(arr.pop())
print(ans)