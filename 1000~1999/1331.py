# 나이트 투어는 체스판에서 나이트가 모든 칸을 정확히 한 번씩 방문하며, 마지막으로 방문하는 칸에서 시작점으로 돌아올 수 있는 경로이다. 다음 그림은 나이트 투어의 한 예이다.
#
# 영식이는 6×6 체스판 위에서 또 다른 나이트 투어의 경로를 찾으려고 한다. 체스판의 한 칸은 A, B, C, D, E, F 중에서 하나와 1, 2, 3, 4, 5, 6 중에서 하나를 이어 붙인 것으로 나타낼 수 있다. 영식이의 나이트 투어 경로가 주어질 때, 이것이 올바른 것이면 Valid, 올바르지 않으면 Invalid를 출력하는 프로그램을 작성하시오.

visited = []
ans = "Valid"
for i in range(36):
    if i == 0:
        start = input()
        start_location = start
        visited.append(start)
    elif i < 35:
        now_location = input()
        if (abs(ord(start_location[0]) - ord(now_location[0])) == 2 and abs(int(start_location[1]) - int(now_location[1])) == 1) and now_location not in visited:
            pass
        elif (abs(ord(start_location[0]) - ord(now_location[0])) == 1 and abs(int(start_location[1]) - int(now_location[1])) == 2) and now_location not in visited:
            pass
        else:
            ans = "Invalid"
        visited.append(now_location)
        start_location = now_location
    else:
        now_location = input()
        if (abs(ord(now_location[0]) - ord(start[0])) == 2 and abs(int(now_location[1]) - int(start[1])) == 1) and now_location not in visited:
            pass
        elif (abs(ord(now_location[0]) - ord(start[0])) == 1 and abs(int(now_location[1]) - int(start[1])) == 2) and now_location not in visited:
            pass
        else:
            ans = "Invalid"
        visited.append(now_location)

visited = list(set(visited))
if len(visited) == 35:
    print(ans)
else:
    print(ans)
