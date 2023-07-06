# 생태학에서 나무의 분포도를 측정하는 것은 중요하다. 그러므로 당신은 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.

from collections import defaultdict
import sys
input = sys.stdin.readline

total = 0
dict = defaultdict(int)
while True:
    tree = input().rstrip()
    if tree == "":
        break
    dict[tree] += 1
    total += 1

li = list(dict.keys())
li.sort()
for i in li:
    print("%s %.4f" % (i, dict[i] * 100 / total))

#2
import sys
input = sys.stdin.readline

total = 0
dict = {}
while True:
    tree = input().rstrip()
    if tree == '\n':
        break
    if tree not in dict:
        dict[tree] = 1
    else:
        dict[tree] += 1
    total += 1

li = sorted(dict.keys())
for i in li:
    print("%s %.4f" % (i, dict[i] * 100 / total))