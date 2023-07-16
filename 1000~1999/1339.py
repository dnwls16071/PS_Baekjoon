# 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.
#
# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
#
# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.
#
# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
my_dict = {}
words = []
for _ in range(N):
    words.append(input().strip())

# 2
# GCF
# ACDEB
for word in words:
    i = 1
    for t in word:
        # G C F
        # A C D E B
        if t not in my_dict:
            my_dict[t] = 10 ** (len(word) - i)
        # t라는 문자가 my_dict에 존재하는 경우
        else:
            my_dict[t] += 10 ** (len(word) - i)
        i += 1

# A : 10000
# C : 1010
# D : 100
# G : 100
# E : 10
# F : 1
# B : 1

# key, value, items
# x[0] = key
# x[1] = value
temp = sorted(my_dict.items(), key=lambda x : x[1], reverse=True)
sorted_dict = dict(temp)

number_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(sorted_dict)):
    word, count = temp[i]
    val = count * number_list[i]
    sorted_dict[word] = val

ans = 0
for i in sorted_dict.values():
    ans += i
print(ans)