# 세준이는 N개의 영어 단어를 이용해 길이가 M인 새로운 단어를 만들려고 한다. 새로운 단어는 N개의 단어를 순서대로 이어 붙이고, 각 단어의 사이에 _을 넣어서 만든다. 이렇게 만든 새로운 단어의 길이가 M이 아닌 경우 _를 추가해서 길이가 M이 되게 만들어야 한다.
#
# _는 단어와 단어 사이에만 추가할 수 있다. 따라서, 새로운 단어는 _으로 시작하거나, _로 끝날 수 없다.
# 단어와 단어 사이에 있는 _의 개수는 모두 같아야 한다.
# 모두 같게 만드는 것이 불가능한 경우 단어와 단어 사이에 있는 _의 개수의 최댓값과 최솟값의 차이는 1이 되어야 한다.
# 새로운 단어 중 사전 순으로 가장 앞서는 단어를 구해보자.

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
words = []
temp = 0
for i in range(N):
    words.append(input().strip())
    temp += len(words[i])

# 사전 순으로 가장 앞서는 단어를 출력하려면?
# 알파벳 대문자, 소문자, 밑 줄의 순서는 'A' < 'B' < 'C' < ... < 'Z' < '_' < 'a' < 'b' < 'c' < ... < 'z' 이다.
# 따라서 사전 순으로 앞선 단어를 만들려면 가장 맨 첫 글자가 대문자인 경우 _의 개수가 적어야 함
# 사전 순으로 앞선 단어를 만들려면 가장 맨 첫 글자가 소문자인 경우 _의 개수가 많아야 함

diff = M - temp
gap = N - 1
quotient, remain = divmod(diff, gap)
result = words[0]
for i in range(1, N):
    if words[i][0].islower() and remain != 0:
        remain -= 1
        result += "_" * (quotient + 1) + words[i]
    elif words[i][0].isupper() and i + remain > gap:
        remain -= 1
        result += "_" * (quotient + 1) + words[i]
    else:
        result += "_" * quotient + words[i]
print(result)