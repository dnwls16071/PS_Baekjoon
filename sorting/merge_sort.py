# Divide and Conquer algorithm
# Breaks down problem into multiple subproblems recursively until they become simple to solve
# Solutions are combined to original problem
# O(N log N)의 시간복잡도
# 병합 정렬 : 재귀, 분할 정복 알고리즘

# General Principle
# 1. Split arrau in half(배열을 반으로 쪼갬)
# 2. Call Merge sort on each half to sort them recursively(반으로 나누어진 각 배열에 대해 merge sort를 호출(재귀))
# 3. Merge both sorted halves into one sorted array(정렬된 두 배열을 하나의 정렬된 배열로 병합)

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0
        j = 0
        k = 0   # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
