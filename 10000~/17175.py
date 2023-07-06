# 혁진이는 알고리즘 문제를 만들라는 독촉을 받아 스트레스다. 하지만 피보나치 문제는 너무 많이 봐서 지겹기 그지없다. 그러나 문제를 만들 시간이 없는 혁진이는 피보나치 문제를 응용해서 문제를 만들려 한다.
#
# int fibonacci(int n) { // 호출
#   if (n < 2) {
#     return n;
#   }
#   return fibonacci(n-2) + fibonacci(n-1);
# }
# 위와 같이 코딩하였을 때 fibonacci(n)를 입력했을 때에 fibonacci 함수가 호출되는 횟수를 계산해보자.

#1
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

try:
    dp[0] = 1
    dp[1] = 1
except:
    dp[0] = 1

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007
print(dp[N])