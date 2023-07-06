# 한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다. 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.
#
# 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

K = int(input())
Class = []
cnt = 1
for i in range(K):
    Max_Gap = 0
    information = list(map(int, input().split()))
    information = sorted(information[1:])
    Class.append(information)

    max_score = max(Class[i])
    min_score = min(Class[i])
    for t in range(len(information) - 1):
        if abs(information[t] - information[t + 1]) > Max_Gap:
            Max_Gap = abs(information[t] - information[t + 1])
    print("Class", cnt)
    print("Max", str(max_score) + ",", "Min", str(min_score) + ",", "Largest gap", Max_Gap)
    cnt += 1