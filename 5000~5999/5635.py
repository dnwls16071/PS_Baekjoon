# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

import sys

n = int(input())
student = []
for _ in range(n):
    name, day, month, year = map(str, sys.stdin.readline().strip().split())
    day = int(day)
    month = int(month)
    year = int(year)
    student.append([name, day, month, year])
student.sort(key = lambda x : (x[3], x[2], x[1]))

print(student[n-1][0])
print(student[0][0])
