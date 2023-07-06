# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())

not_hear = set()
for _ in range(N):
    not_hear.add(input())

not_see = set()
for _ in range(M):
    not_see.add(input())

intersection = not_see.intersection(not_hear)
intersection = sorted(intersection)
print(len(intersection))
for i in intersection:
    print(i)