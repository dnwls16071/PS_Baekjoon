# Z 대학교 학생은 입학할 때 학번을 받게 된다. 학번은 0보다 크거나 같고, 106-1보다 작거나 같은 정수이다. Z 대학의 김상근 교수는 학번으로 학생들을 구분한다. 상근이는 학생들을 조금 더 쉽게 기억하기 위해서 자신이 가르치는 학생들의 학번을 m으로 나누었을 때, 나머지가 모두 다른 가장 작은 양의 정수를 찾으려고 한다.

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    li = []
    n = int(input())
    for __ in range(n):
        li.append(int(input()))
    if n == 1:
        print(1)
    else:
        cnt = 2
        while 1:
            res = []
            for i in range(len(li)):
                res.append(li[i] % cnt)
            dd = set(res)
            dd = list(dd)
            if len(li) == len(dd):
                print(cnt)
                break
            else:
                cnt += 1