# 9694번 한신이는 당내 최고의원을 선출하기 위한 사전 인기 투표의 결과를 받게 되었다.  하지만 공식 선거를 통해서 당내 최고의원이 되기위해선 과반수의 표를 받아야 하기 때문에 현재의 인기 투표 결과를 보고 본 최고의원 선거를 준비하려 한다. 한신이를 도와 누가 최고 득표자인지, 받은 투표수가 과반수득표인지 아닌지를 빠르게 판단할수 있도록 도와주자.

T = int(input())
for _ in range(T):
    n = int(input())
    vote_information = []
    total_vote = 0  # 모든 후보자들이 얻은 득표 수
    number = 1
    for _ in range(n):
        vote = int(input())
        vote_information.append([number, vote])
        number += 1
        total_vote += vote
    vote_information.sort(key=lambda x: (-x[1], x[0]))
    if vote_information[0][1] == vote_information[1][1]:
        print("no winner")
    elif vote_information[0][1] > total_vote * 0.5:
        print("majority winner", str(vote_information[0][0]))
    elif vote_information[0][1] <= total_vote * 0.5:
        print("minority winner", str(vote_information[0][0]))