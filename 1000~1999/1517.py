# N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.
#
# 버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다. 예를 들어 수열이 3 2 1 이었다고 하자. 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다. 다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다. 그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.

import sys
input = sys.stdin.readline


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        left, inv_count_left = merge_sort(arr[:len(arr)//2])
        right, inv_count_right = merge_sort(arr[len(arr)//2:])
        merged, inv_count_merge = merge(left, right)

    inv_count = inv_count_left + inv_count_right + inv_count_merge
    return merged, inv_count

def merge(left_arr, right_arr):
    merged = []
    inv_count = 0
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1
            inv_count += len(left_arr) - i

    while i < len(left_arr):
        merged.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        merged.append(right_arr[j])
        j += 1

    return merged, inv_count

N = int(input())
arr = list(map(int, input().strip().split()))
merged_arr, swap = merge_sort(arr)
print(merged_arr)
print(swap)