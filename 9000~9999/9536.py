# 고대 미스테리로 전해지는 여우의 울음소리를 밝혀내기 위해 한신이는 고성능 녹음기로 무장하고 숲으로 들어갔다. 하지만 숲에는 동물들이 가득해, 녹음된 음성에는 다른 동물들의 울음소리가 섞여 있다. 그러나 한신이는 철저한 준비를 해 왔기 때문에 다른 동물들이 어떤 울음소리를 내는지 정확히 알고 있다. 그러므로 그 소리를 모두 걸러내면 남은 잡음은 분명히 여우의 울음소리일 것이다.

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sound_lst = list(map(str, input().strip().split()))
    result = []
    temp = []
    while True:
        input_string = input().strip()
        if input_string == "what does the fox say?":
            break
        else:
            li = list(input_string.split(" "))
            temp.append(li[-1])

    for i in sound_lst:
        if i not in temp:
            result.append(i)
    print(*result)
