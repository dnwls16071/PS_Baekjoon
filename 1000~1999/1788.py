# 수학에서, 피보나치 수는 위의 점화식과 같이 귀납적으로 정의되는 수열이다. 위의 식에서도 알 수 있듯이, 피보나치 수 F(n)은 0 이상의 n에 대해서만 정의된다.
#
# 하지만 피보나치 수 F(n)을 n이 음수인 경우로도 확장시킬 수 있다. 위의 식에서 n > 1인 경우에만 성립하는 F(n) = F(n-1) + F(n-2)를 n ≤ 1일 때도 성립되도록 정의하는 것이다. 예를 들어 n = 1일 때 F(1) = F(0) + F(-1)이 성립되어야 하므로, F(-1)은 1이 되어야 한다.
#
# n이 주어졌을 때, 피보나치 수 F(n)을 구하는 프로그램을 작성하시오. n은 음수로 주어질 수도 있다.

n = int(input())

dp = [0, 1, 1]
for i in range(3, abs(n)+1):
    dp.append((dp[i-2] + dp[i-1]) % 1000000000)

if n < 0 and abs(n) % 2 == 0:
    if -dp[abs(n)] < 0:
        print(-1)
        print(dp[abs(n)] % 1000000000)
    elif -dp[abs(n)] > 0:
        print(1)
        print(dp[abs(n)] % 1000000000)
    else:
        print(0)
        print(0)
elif n < 0 and abs(n) % 2 != 0:
    if dp[abs(n)] < 0:
        print(-1)
        print(dp[abs(n)] % 1000000000)
    elif dp[abs(n)] > 0:
        print(1)
        print(dp[abs(n)] % 1000000000)
    else:
        print(0)
        print(0)
elif n > 0:
    print(1)
    print(dp[n] % 1000000000)
else:
    print(0)
    print(0)