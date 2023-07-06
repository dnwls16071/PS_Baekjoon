# 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
#
# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
#
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
#
# 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.
#
# A+	4.5
# A0	4.0
# B+	3.5
# B0	3.0
# C+	2.5
# C0	2.0
# D+	1.5
# D0	1.0
# F	0.0
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
#
# 과연 치훈이는 무사히 졸업할 수 있을까?

import sys
input = sys.stdin.readline

result = 0
total = 0
for _ in range(20):
    subject, score, grade = map(str, input().strip().split())
    score = float(score)
    if grade == "P":
        continue
    elif grade == "A+":
        result += score * 4.5
        total += score
    elif grade == "A0":
        result += score * 4.0
        total += score
    elif grade == "B+":
        result += score * 3.5
        total += score
    elif grade == "B0":
        result += score * 3.0
        total += score
    elif grade == "C+":
        result += score * 2.5
        total += score
    elif grade == "C0":
        result += score * 2.0
        total += score
    elif grade == "D+":
        result += score * 1.5
        total += score
    elif grade == "D0":
        result += score * 1.0
        total += score
    else:
        result += score * 0.0
        total += score

print("%.6f" % (result / total))