# 0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다. 그 수열 안에서 연속해서 커지거나(같은 것 포함), 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라.
#
# 예를 들어 수열 1, 2, 2, 4, 4, 5, 7, 7, 2 의 경우에는 1 ≤ 2 ≤ 2 ≤ 4 ≤ 4 ≤ 5 ≤ 7 ≤ 7 이 가장 긴 구간이 되므로 그 길이 8을 출력한다. 수열 4, 1, 3, 3, 2, 2, 9, 2, 3 의 경우에는 3 ≥ 3 ≥ 2 ≥ 2 가 가장 긴 구간이 되므로 그 길이 4를 출력한다. 또 1, 5, 3, 6, 4, 7, 1, 3, 2, 9, 5 의 경우에는 연속해서 커지거나 작아지는 수열의 길이가 3 이상인 경우가 없으므로 2를 출력하여야 한다.

N = int(input())
N_lst = list(map(int, input().split()))
increase_max = 1
increase_length = 1
for i in range(len(N_lst)-1):
    if N_lst[i] <= N_lst[i+1]:
        increase_length += 1
    else:
        if increase_length > increase_max:
            increase_max = increase_length
            increase_length = 1
        else:
            increase_length = 1
if increase_length > increase_max:
    increase_max = increase_length

decrease_max = 1
decrease_length = 1
for i in range(len(N_lst)-1, 0, -1):
    if N_lst[i-1] >= N_lst[i]:
        decrease_length += 1
    else:
        if decrease_length > decrease_max:
            decrease_max = decrease_length
            decrease_length = 1
        else:
            decrease_length = 1
if decrease_length > decrease_max:
    decrease_max = decrease_length


print(max(increase_max, decrease_max))