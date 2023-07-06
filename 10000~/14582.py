# 프로야구팀 울림 제미니스는 오늘도 졌다. 이번에는 스타트링크 걸리버스의 4번타자가 끝내기 홈런을 쳐서 졌다. 울림 제미니스의 열렬한 팬인 지수는 속으로 화를 참으며 어떤 선수 때문에 졌는지 생각해보았다. 지수는 팀이 역전패를 했다면 불펜 투수의 책임이고, 그렇지 않다면 타자와 선발 투수의 책임이라고 생각했다.
#
# 지수는 오늘 경기에서 울림이 어떻게 졌는지 생각해보려 했지만, 기분이 너무 더러워서 뭘 할 의욕이 나지 않았다. 지수를 도와 오늘 경기에서 울림 제미니스가 역전패를 했는지 구하는 프로그램을 작성하여라. 역전패가 성립하려면 경기 도중 울림 제미니스가 이기고 있는 순간이 있어야 한다.

jam_score_lst = list(map(int, input().split()))
startlink_score_lst = list(map(int, input().split()))

jam_score = 0
startlink_score = 0
flag = False
for i in range(9):
    jam_score += jam_score_lst[i]
    # 재미니스의 선공격으로 리드를 차지했다면?
    if jam_score > startlink_score:
        flag = True
    startlink_score += startlink_score_lst[i]

# 재미니스가 리드를 차지했지만 최종 스코어는 startlink_score가 더 높다면?
if flag == True and jam_score < startlink_score:
    print("Yes")
else:
    print("No")