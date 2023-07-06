# 대열이는 욱제의 친구다.
#
# “야 백대열을 약분하면 뭔지 알아?”
# “??”
# “십대일이야~ 하하!”
# n:m이 주어진다. 욱제를 도와주자. (...)

import math
input_string = input()
lst = []
result = ""
for i in range(len(input_string)):
    if input_string[i] == ":":
        lst.append(int(result))
        result = ""
    else:
        result += input_string[i]
lst.append(int(result))

GCD = math.gcd(lst[0], lst[1])
lst[0] = lst[0] // GCD
lst[1] = lst[1] // GCD
print(str(lst[0]) + ":" + str(lst[1]))