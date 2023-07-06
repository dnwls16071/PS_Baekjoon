# 피보나치 비스무리한 수열은 f(n) = f(n-1) + f(n-3)인 수열이다. f(1) = f(2) = f(3) = 1이며 피보나치 비스무리한 수열을 나열하면 다음과 같다.
#
# 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, ...
#
# 자연수 n을 입력받아 n번째 피보나치 비스무리한 수열을 구해보자!

n = int(input())

fibonacci = [1, 1, 1]
for i in range(3, 117):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-3])

print(fibonacci[n-1])