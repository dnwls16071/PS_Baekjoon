# 최근 아시아 지역의 학생들만 참여하는 정보 올림피아드 대회가 만들어졌다. 이 대회는 온라인으로 치러지기 때문에 각 나라에서 이 대회에 참여하는 학생 수의 제한은 없다.
#
# 참여한 학생들의 성적순서대로 세 명에게만 금, 은, 동메달을 수여한다. 단, 동점자는 없다고 가정한다. 그리고 나라별 메달 수는 최대 두 개다.
#
# 예를 들어, 대회 결과가 다음의 표와 같이 주어졌다고 하자.
#
# 참가국	학생번호	점수
# 1	1	230
# 1	2	210
# 1	3	205
# 2	1	100
# 2	2	150
# 3	1	175
# 3	2	190
# 3	3	180
# 3	4	195
# 이 경우, 금메달 수상자는 1번 국가의 1번 학생이고, 은메달 수상자는 1번 국가의 2번 학생이며, 동메달 수상자는 3번 국가의 4번 학생이다. (1번 국가의 3번 학생의 성적이 동메달 수여자보다 높지만, 나라 별 메달 수가 두 개 이하 이므로 1번 국가 3번 학생은 동메달을 받을 수 없다.)
#
# 대회 결과가 입력으로 주어질 때, 메달 수상자를 결정하여 출력하는 프로그램을 작성하시오.

N = int(input())
olympiad = []
for _ in range(N):
    information = list(map(int, input().split()))
    olympiad.append(information)

olympiad.sort(key = lambda x : (-x[2]))
print(olympiad[0][0], olympiad[0][1])   # 금메달 수상자
print(olympiad[1][0], olympiad[1][1])   # 은메달 수상자
if olympiad[0][0] == olympiad[1][0]:    # 만약 금메달 수상자와 은메달 수상자의 국가 번호가 같다면?
    for i in range(2, N):
        if olympiad[i][0] == olympiad[0][0]:
            continue
        else:
            print(olympiad[i][0], olympiad[i][1])
            break
else:                                   # 만약 금메달 수상자와 은메달 수상자의 국가 번호가 다르다면?
    print(olympiad[2][0], olympiad[2][1])
