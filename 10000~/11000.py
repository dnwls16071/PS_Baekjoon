# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.
#
# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
#
# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
#
# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

import heapq
import sys
input = sys.stdin.readline

N = int(input())
timetable = []
for _ in range(N):
    S, T = map(int, input().strip().split())
    timetable.append([S, T])

timetable.sort(key = lambda x : x[0])
heap = []
heapq.heappush(heap, timetable[0][1])   # 첫 번째 강의 종료시간
for i in range(1, N):
    # 강의 종료시간이 다음 강의 시작시간보다 뒤에 있다면?
    if heap[0] > timetable[i][0]:
        heapq.heappush(heap, timetable[i][1])
    # 만약 강의 종료시간이 다음 강의 시작시간과 같거나 앞에 있다면?
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, timetable[i][1])
print(heap)
