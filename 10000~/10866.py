# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여덟 가지이다.
#
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
import sys

li = deque([])
N = int(input())
for _ in range(N):
    command = list(map(str, sys.stdin.readline().strip().split()))
    if len(command) == 2:
        if command[0] == "push_front":
            li.appendleft(int(command[1]))
        elif command[0] == "push_back":
            li.append(int(command[1]))
    else:
        if command[0] == "pop_front":
            if li == deque([]):
                print(-1)
            else:
                temp = li.popleft()
                print(temp)
        elif command[0] == "pop_back":
            if li == deque([]):
                print(-1)
            else:
                temp = li.pop()
                print(temp)
        elif command[0] == "size":
            print(len(li))
        elif command[0] == "empty":
            if li == deque([]):
                print(1)
            else:
                print(0)
        elif command[0] == "front":
            if li == deque([]):
                print(-1)
            else:
                print(li[0])
        elif command[0] == "back":
            if li == deque([]):
                print(-1)
            else:
                print(li[-1])