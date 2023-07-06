# 조(Joe)는 중앙대학교 교수이고, 논리회로 설계 과목을 담당하고 있다. 그는 수업을 하면서 7명의 학생을 제외한 나머지 학생들에게 좋은 학점을 주겠다고 약속을 하였다.
#
# Joe 교수님을 돕기 위해서 학생들의 최종 성적이 주어질 때, 그의 연구실인 You See Lab으로 데려갈 성적이 좋지 못한 7명의 학생, 칠무해의 성적을 뽑아보자.

import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    li.append(float(input()))

li.sort()
for i in range(7):
    print("{:.3f}".format(li[i]))