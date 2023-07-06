# 악독한 코치 주혁은 선수들을 이름 순으로 세우는 것을 좋아한다. 더 악독한 것은 어떤 순서로 서야할지도 알려주지 않았다! 선수들의 이름이 주어질 때 어떤 순서로 이루어져있는지 확인해보자.

N = int(input())
player_name = []
for _ in range(N):
    player_name.append(input())

ascend_player_name = sorted(player_name)
descend_player_name = sorted(player_name, reverse=True)

if player_name == ascend_player_name:
    print("INCREASING")
elif player_name == descend_player_name:
    print("DECREASING")
else:
    print("NEITHER")