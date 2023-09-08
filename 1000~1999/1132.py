# N개의 수가 주어진다. 이 숫자는 모두 자연수이고, 알파벳 A부터 J가 자리수를 대신해서 쓰여 있다. 이 알파벳은 모두 한 자리를 의미한다. 그리고, 각 자리수는 정확하게 알파벳 하나이다. 0으로 시작하는 수는 없다. 이때, 가능한 수의 합 중 최댓값을 구해보자.

import sys
input = sys.stdin.readline

N = int(input())
answer = []
first = []
my_dict = {}
for _ in range(N):
    i = 1
    word = input().strip()
    answer.append(word)
    first.append(word[0])
    for t in range(len(word)):
        if word[t] not in my_dict:
            my_dict[word[t]] = 10 ** (len(word) - i)
        else:
            my_dict[word[t]] += 10 ** (len(word) - i)
        i += 1

if len(list(my_dict.keys())) < 10:
    result = 0
    val = 9
    values = sorted(my_dict.items(), key = lambda x : -x[1])
    for i in values:
        result += i[1] * val
        val -= 1
    print(result)
# 맨 앞자리에 0이 나올 수 있는 경우
else:
    result = 0
    m = 9
    values = sorted(my_dict.items(), key = lambda x : -x[1])
    for i in values:
        if i[0] not in first:
            # ABCDEFGHIJ → I
            tmp = i[0]

    for i in values:
        # 만약 tmp 즉, I가 나오면 계산하지않고 넘어간다.
        # 그게 아니라면 합을 계속 누적한다.
        if i[0] != tmp:
            result += i[1] * m
            m -= 1
        else:
            continue
    print(result)