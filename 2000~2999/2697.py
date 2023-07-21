# 어떤 수 A가 주어졌을 때, A의 다음수를 구하는 프로그램을 작성하시오.
#
# A의 다음수는 A와 구성이 같으면서, A보다 큰 수 중에서 가장 작은 수 이다.
#
# A와 B의 구성이 같다는 말은 A를 이루고 있는 각 자리수의 등장 횟수가, B를 이루는 각 자리수의 등장 횟수와 같을 때 이다.
#
# 예를 들어 123과 321은 구성이 같다. 왜냐하면 두 수 모두 1이 1번, 2가 1번, 3이 1번 나오기 때문이다. 마찬가지로 14232와 12243도 구성이 같다.
#
# 하지만, 14232와 14432는 구성이 같지 않다.

import sys
input = sys.stdin.readline

def next_permutations(nums):
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i == 0:
        msg = 'BIGGEST'
        return msg

    j = len(nums) - 1
    while nums[j] <= nums[i-1]:
        j -= 1

    nums[i-1], nums[j] = nums[j], nums[i-1]
    nums[i:] = reversed(nums[i:])
    return nums

T = int(input())
for _ in range(T):
    A = list(input().strip())
    result = next_permutations(A)
    print(''.join(map(str, result)))