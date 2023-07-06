# 정우는 소문난 걸그룹 덕후이다. 정우의 친구 준석이도 걸그룹을 좋아하지만 이름을 잘 외우지 못한다는 문제가 있었다. 정우는 친구를 위해 걸그룹 개인과 팀의 이름을 검색하여 외우게 하는 퀴즈 프로그램을 만들고자 한다.

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
teams = {}

for _ in range(N):
    group_name = input().strip()
    C = int(input())
    teams[group_name] = [input().strip() for _ in range(C)]

for _ in range(M):
    name = input().strip()
    question_type = int(input())
    if question_type == 1:
        for group_name, members in teams.items():
            if name in members:
                print(group_name)
    else:
        for i in sorted(teams[name]):
            print(i, sep="\n")